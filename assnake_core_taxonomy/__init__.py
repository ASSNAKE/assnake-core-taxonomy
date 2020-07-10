import os
import assnake


from assnake_core_taxonomy.metaphlan2.init_metaphlan2 import mp2_init
from assnake_core_taxonomy.metaphlan2.loaders import load_metaphlan2



snake_module = assnake.SnakeModule(name = 'assnake-core-taxonomy', 
                           install_dir = os.path.dirname(os.path.abspath(__file__)),
                           initialization_commands = [mp2_init],
                           dataset_methods = {'load_metaphlan2': load_metaphlan2})
