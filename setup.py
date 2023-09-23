from setuptools import setup, find_packages

setup(
    name="VedAstro",
    version="1.0.0",
    license='MIT',
    description="An open source Python library for advanced astronomical calculations like planet longitude, house sign, shadbala, etc...",
    author="VedAstro",
    author_email="developer@vedastro.org",
    packages=find_packages(include=["vedastro"]),
    install_requires=[
        "packaging",
        "pythonnet",
    ],
    python_requires=">=3.9.*",
)
