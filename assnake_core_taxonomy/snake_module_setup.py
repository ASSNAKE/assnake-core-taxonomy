import os
from assnake.api.snake_module import SnakeModule
from assnake_core_taxonomy.metaphlan2.cmd_metaphlan2 import mp2_invocation
from assnake.utils import read_yaml


this_dir = os.path.dirname(os.path.abspath(__file__))
snake_module = SnakeModule(name = 'assnake-core-taxonomy', 
                           install_dir = this_dir,
                           snakefiles = ['./metaphlan2/metaphlan2.py'],
                           invocation_commands = [mp2_invocation],
                           wc_configs = [read_yaml(os.path.join(this_dir, './metaphlan2/wc_config.yaml'))])
