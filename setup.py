from setuptools import setup, find_packages

setup(
    name='inverse-tree',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'inverse-tree=inverse_tree.inverse_tree:inverse_tree',
        ],
    },
)