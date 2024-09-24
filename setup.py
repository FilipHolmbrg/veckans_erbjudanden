from setuptools import setup, find_packages

setup(
    name='veckans_mat',
    version='0.1',
    packages=find_packages(),  # Automatically finds all packages (including veckans_mat)
    install_requires=[],
    author='Filip Holmberg',
    description='A package for veckans erbjudanden',
    url='https://github.com/FilipHolmbrg/veckans_erbjudanden',
    python_requires='>=3.6',
)
