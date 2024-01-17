from setuptools import find_packages, setup
from typing import List

# this variable is created to handle -e . not appearing in the requirements list below 
# as this might throw error while installing packages
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Sapthagirishwaran Thennal Sivaramakrishnan',
author_email='sgn1989@gmail.com',
packages=find_packages(),
#install_requires=['pandas', 'numpy', 'seaborn'] # this is not ideal if you have some many packages
install_requires=get_requirements('requirements.txt')
)