from setuptools import setup, find_packages

setup(
    name='veckans_mat',             # The name of your package
    version='1.0.0',                # Version number of your package
    packages=find_packages(),       # Automatically finds all packages
    install_requires=[              # List your dependencies here
        # 'numpy',                  # Example dependencies
        # 'requests',
    ],
    author='Filip Holmberg',
    author_email='filip.holmberg.se@gmail.com',
    description='Package to get offers and match with recipes',
    url='https://github.com/FilipHolmbrg/veckans_erbjudanden',  # GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
