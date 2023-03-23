from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements():
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [dependency_name.replace("\n", "") for dependency_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    
    return requirement_list

setup(
    name = "wafer",
    version = "0.0.1",
    author = "Kushal Bhadra",
    author_email = "kushabhadra5@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)