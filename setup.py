from setuptools import setup, find_packages

setup(
    name='silk',
    version='0.1',
    url='https://github.com/sjdv1982/silk.git',
    author='Sjoerd de Vries',
    author_email='sjdv1982@gmail.com',
    description='Library for schema validation, object-oriented API wrappers (like ECMAS prototypes), and mixed JSON/binary serialization.',
    packages=find_packages(),
    #install_requires=['numpy', 'jsonschema==3.*'], # disabled for conda
)