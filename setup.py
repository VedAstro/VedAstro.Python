from setuptools import setup, find_packages

setup(
    name='VedAstro',
    version='1.22.20',
    description='An open source Python library for advanced astronomical calculations like planet longitude, house sign, shadbala, etc...',
    author='Tharaka Umayanga',
    author_email='tharakau@gmail.com',
    packages=find_packages(include=['vedastro']),
    install_requires=[
        'packaging',
        'colorama',
        'requests',
    ],
    python_requires='>=3.9,<3.13',
)
