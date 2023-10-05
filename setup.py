from setuptools import find_packages, setup
from typing import List
# In Python, setup.py is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package. 
HPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HPHEN_E_DOT in requirements:
            requirements.remove(HPHEN_E_DOT)
    return requirements

setup(
    name = 'Lang Chain Audio App',
    version='0.0.1',
    author='Sayed Mohd Asim',
    author_email='asim80822@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn'] 
    install_requires=get_requirements('requirements.txt')
 
    
)