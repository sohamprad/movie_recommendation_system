from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description  = fh.read()

AUTHOR_NAME = 'Soham Pradhan'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name= SRC_REPO,
    version='0.0.1',
    author= AUTHOR_NAME,
    author_email= 'sohampradhan04@gmail.com',
    description= 'A small python package for a movie recommender',
    long_description= long_description,
    long_description_content_type= 'text/markdown',
    #url=
    package = [SRC_REPO],
    python_version = '>=3.8',
    install_requires = LIST_OF_REQUIREMENTS
)
