
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

from assnake_core_preprocessing.snake_module_setup import snake_module


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        snake_module.deploy_module()
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        snake_module.deploy_module()
        install.run(self)


setup(
    name='assnake-core-taxonomy',
    version='0.0.3',
    packages=find_packages(),
    entry_points = {
        'assnake.plugins': ['assnake-core-taxonomy = assnake_core_taxonomy:snake_module']
    },
    install_requires=[
        'assnake'
    ],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
)