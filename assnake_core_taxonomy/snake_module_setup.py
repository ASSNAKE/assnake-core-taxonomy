import os
import assnake
from assnake_core_taxonomy.metaphlan2.cmd_metaphlan2 import mp2_invocation
from assnake_core_taxonomy.metaphlan2.cmd_metaphlan2 import mp2_rare_invocation
from assnake_core_taxonomy.metaphlan2.init_metaphlan2 import mp2_init
from assnake_core_taxonomy.metaphlan2.loaders import load_metaphlan2

from assnake.utils import read_yaml


this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = assnake.SnakeModule(name = 'assnake-core-taxonomy', 
                           install_dir = this_dir,
                           snakefiles = ['./cat_bat/workflow.smk', './metaphlan2/workflow.smk'],
                           invocation_commands = [mp2_invocation, mp2_rare_invocation],
                           initialization_commands = [mp2_init],
                           dataset_methods = {'load_metaphlan2': load_metaphlan2},
                           wc_configs = [read_yaml(os.path.join(this_dir, './metaphlan2/wc_config.yaml'))])
