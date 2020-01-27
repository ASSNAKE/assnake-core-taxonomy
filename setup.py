from setuptools import setup, find_packages

setup(
    name='assnake-core-taxonomy',
    version='0.0.1',
    packages=find_packages(),
    entry_points = {
        'assnake.plugins': ['assnake-core-taxonomy = assnake_core_taxonomy.snake_module_setup:snake_module']
    }
)