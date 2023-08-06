from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

includes = [
    "ansible.modules.viptela",
    "ansible.module_utils.viptela",
    "ansible.plugins.inventory",
]

setup(
    name="ansible-virl",
    version='0.0.1',
    packages=find_namespace_packages(include=includes),
    description="Cisco DevNet VIRL Ansible Modules",
    install_requires=['virl2_client'],
)
