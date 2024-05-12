import os, assnake

snake_module = assnake.SnakeModule(
    name = 'assnake-core-taxonomy', 
    install_dir = os.path.dirname(os.path.abspath(__file__)),
)
