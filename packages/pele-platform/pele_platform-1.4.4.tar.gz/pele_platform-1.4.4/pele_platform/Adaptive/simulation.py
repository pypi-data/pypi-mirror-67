import subprocess
import os
import shutil
import glob
import AdaptivePELE.adaptiveSampling as adt
import PPP.main as ppp
import pele_platform.Utilities.Helpers.plop_launcher as plop
from pele_platform.Utilities.Helpers import helpers
import pele_platform.Utilities.Parameters.pele_env as pele
import pele_platform.Utilities.Helpers.constraints as ct
import pele_platform.constants.constants as cs
import pele_platform.Utilities.Helpers.system_prep as sp
import pele_platform.Utilities.Helpers.missing_residues as mr
import pele_platform.Utilities.Helpers.simulation as ad
import pele_platform.Utilities.Helpers.center_of_mass as cm
import pele_platform.Utilities.Helpers.randomize as rd
import pele_platform.Utilities.Helpers.helpers as hp
import pele_platform.Utilities.Helpers.metrics as mt
import pele_platform.Utilities.Helpers.solventOBCParamsGenerator as obc
import pele_platform.Utilities.Helpers.calculatePCA4PELE as pc
import pele_platform.Analysis.plots as pt
import pele_platform.RNA.prep as pr




def run_adaptive(args):
    if args.rna:
        args.system = pr.fix_rna_pdb(args.system)
        args.no_ppp = True
    # Build Folders and Logging and env variable that will containt
    #all main  attributes of the simulation
    env = pele.EnviroBuilder()
    env.software = "Adaptive"
    env.build_adaptive_variables(args)
    env.create_files_and_folders()
    shutil.copy(args.yamlfile, env.pele_dir) 

    if env.adaptive_restart and not env.only_analysis:
        with helpers.cd(env.pele_dir):
            adt.main(env.ad_ex_temp)
            env.logger.info("Simulation run succesfully (:\n\n")

    elif not env.only_analysis:


        env.logger.info("System: {}; Platform Functionality: {}\n\n".format(env.residue, env.software))
        
        if env.perturbation:
            syst = sp.SystemBuilder.build_system(env.system, args.mae_lig, args.residue, env.pele_dir)
        else:
            syst = sp.SystemBuilder(env.system, None, None, env.pele_dir)
        
        env.logger.info("Prepare complex {}".format(syst.system))
           
        ########Choose your own input####################
        # User specifies more than one input
        if env.input:
            env.inputs_simulation = []
            for input in env.input:
                input_path  = os.path.join(env.pele_dir, os.path.basename(input))
                shutil.copy(input, input_path)
                if env.no_ppp:
                    input_proc = input
                else:
                    input_proc = os.path.basename(ppp.main(input_path, env.pele_dir, output_pdb=["" , ],
                                charge_terminals=args.charge_ter, no_gaps_ter=args.gaps_ter,
                                constrain_smiles=env.constrain_smiles, ligand_pdb=env.ligand_ref)[0])
                env.inputs_simulation.append(input_proc)
                hp.silentremove([input_path])
            env.adap_ex_input = ", ".join(['"' + input + '"' for input in env.inputs_simulation]).strip('"')
        # Global exploration mode: Create inputs around protein
        elif args.full or args.randomize:
            ligand_positions, box_radius, box_center = rd.randomize_starting_position(env.ligand_ref, env.receptor,
                outputfolder=env.pele_dir, nposes=env.poses, test=env.test)
            env.box_center = box_center if not env.box_center else env.box_center
            env.box_radius = box_radius if not env.box_radius else env.box_radius
            if env.no_ppp:
                receptor = syst.system
            else:
                receptor = ppp.main(syst.system, env.pele_dir, output_pdb=["" , ],
                            charge_terminals=args.charge_ter, no_gaps_ter=args.gaps_ter,
                            constrain_smiles=env.constrain_smiles, ligand_pdb=env.ligand_ref)[0]
            inputs = rd.join(receptor, ligand_positions, env.residue, output_folder=env.pele_dir)
            env.adap_ex_input = ", ".join(['"' + os.path.basename(input) + '"' for input in inputs]).strip('"')
            hp.silentremove(ligand_positions)
            #Parsing input for errors and saving them as inputs

        ##########Prepare System################
        if env.no_ppp:
            missing_residues = []
            gaps = {}
            metals = {}
            env.constraints = ct.retrieve_constraints(env.system, gaps, metals, back_constr=env.ca_constr)
            if env.input:
                # If we have more than one input
                for input in env.input: shutil.copy(input, env.pele_dir)
            else:
                shutil.copy(env.system, env.pele_dir)
        else:
            env.system, missing_residues, gaps, metals, env.constraints = ppp.main(syst.system, env.pele_dir, output_pdb=["" , ], charge_terminals=args.charge_ter, no_gaps_ter=args.gaps_ter, mid_chain_nonstd_residue=env.nonstandard, skip=env.skip_prep, back_constr=env.ca_constr, constrain_smiles=env.constrain_smiles, ligand_pdb=env.ligand_ref)
        if env.external_constraints:
            # Keep Json ordered by having first title and then constraints
            env.constraints = env.constraints[0:1] + env.external_constraints + env.constraints[1:]
        if env.remove_constraints:
            env.constraints = ""
        env.logger.info(cs.SYSTEM.format(missing_residues, gaps, metals))
        env.logger.info("Complex {} prepared\n\n".format(env.system))


        ############Parametrize Ligand###############
        if env.perturbation:
            env.logger.info("Creating template for residue {}".format(args.residue))
            with hp.cd(env.pele_dir):
                plop.parametrize_miss_residues(args, env, syst)
            env.logger.info("Template {}z created\n\n".format(args.residue.lower()))
            if env.external_template:
                for template_file in env.external_template:
                    cmd_to_move_template = "cp {} {}".format(template_file,  env.template_folder)
                    subprocess.call(cmd_to_move_template.split())
            if env.external_rotamers:
                for rotamer_file in env.external_rotamers:
                    cmd_to_move_rotamer_file = "cp {} {}".format(rotamer_file, env.rotamers_folder)
                    subprocess.call(cmd_to_move_rotamer_file.split())

            #################Set Box###################
            env.logger.info("Generating exploration box")
            if not env.box_center:
                env.box_center = cm.center_of_mass(env.ligand_ref)
                env.logger.info("Box {} generated\n\n".format(env.box_center))
            else:
                env.logger.info("Box {} generated\n\n".format(env.box_center))
            env.box = cs.BOX.format(env.box_radius, env.box_center) if  env.box_radius else ""
        else:
            env.box=""

        ###########Parametrize missing residues#################
        for res, __, _ in missing_residues:
            if res != args.residue and res not in env.skip_ligand_prep:
                env.logger.info("Creating template for residue {}".format(res))
                with hp.cd(env.pele_dir):
                    mr.create_template(args, env, res)
                env.logger.info("Template {}z created\n\n".format(res))
    
        #########Parametrize solvent parameters if need it##############
        env.logger.info("Setting implicit solvent: {}".format(env.solvent))
        if env.solvent == "OBC":
            shutil.copy(env.obc_tmp, env.obc_file)
            for template in glob.glob(os.path.join(env.template_folder, "*")):
                obc.main(template, env.obc_file)
        env.logger.info("Implicit solvent set\n\n".format(env.solvent))
        


        #####Build PCA#######
        if env.pca_traj:
           if isinstance(env.pca_traj, str):
               pdbs = glob.glob(env.pca_traj)
           elif isinstance(env.pca_traj, list):
               pdbs = env.pca_traj
           pdbs_full_path = [os.path.abspath(pdb) for pdb in pdbs]
           with helpers.cd(env.pele_dir):
               pca = pc.main(pdbs_full_path)
           env.pca = cs.PCA.format(pca)

        
        ############Fill in Simulation Templates############
        env.logger.info("Running Simulation")
        #if env.adaptive:
        #    ext.external_adaptive_file(env)
        #if env.pele:
        #    ext.external_pele_file(env)
        adaptive = ad.SimulationBuilder(env.ad_ex_temp, env.pele_exit_temp, env)
        # Fill to time because we have flags inside flags
        adaptive.fill_pele_template(env)
        adaptive.fill_pele_template(env)
        adaptive.fill_adaptive_template(env)
        adaptive.fill_adaptive_template(env)
        if not env.debug:
            adaptive.run()
        env.logger.info("Simulation run succesfully (:\n\n")

    if env.analyse and not env.debug:
        report = pt.analyse_simulation(env.report_name, env.traj_name[:-4]+"_", 
            os.path.join(env.pele_dir, env.output), env.residue, cpus=env.cpus,
            output_folder=env.pele_dir, clustering=env.perturbation, mae=env.mae,
            nclusts=env.analysis_nclust, overwrite=env.overwrite, topology=env.topology,
            be_column=env.be_column, limit_column=env.limit_column, te_column=env.te_column)
        print("Pdf summary report succesfully writen to: {}".format(report))
    return env
