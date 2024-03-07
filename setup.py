from setuptools import find_packages, setup

setup(
    name='mcqgenai',
    version='0.0.1',
    author='Mrinal Karmokar',
    author_email='mrinalkarmokar27@gmail.com',
    install_requires=['openai', 'langchain', 'PyPDF2'],
    packages=find_packages()
)
