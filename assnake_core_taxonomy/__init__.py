import os
import assnake
# from assnake_core_taxonomy.metaphlan2.cmd_metaphlan2 import mp2_invocation
# from assnake_core_taxonomy.metaphlan2.cmd_metaphlan2 import mp3_invocation
# from assnake_core_taxonomy.centrifuge.result import centrifuge_invocation
# from assnake_core_taxonomy.metaphlan2.cmd_metaphlan2 import mp2_rare_invocation


import assnake_core_taxonomy.metaphlan2.result as metaphlan

from assnake_core_taxonomy.metaphlan2.init_metaphlan2 import mp2_init
from assnake_core_taxonomy.metaphlan2.loaders import load_metaphlan2

from assnake.utils.general import read_yaml


this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = assnake.SnakeModule(name = 'assnake-core-taxonomy', 
                           install_dir = this_dir,
                           snakefiles = [],
                           results= [metaphlan],
                           initialization_commands = [mp2_init],
                           dataset_methods = {'load_metaphlan2': load_metaphlan2},
                           wc_configs = [])
