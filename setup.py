from setuptools import setup, find_packages

install_requires = ["numpy>=1.17",
                    "meshio>=4.4.6",
                    "ipython>=7.9.0"]

setup(name='mesh_ops',
      version='0.0.1',
      description='Wrapper for meshio for common operations',
      author='Andy Howell',
      author_email='andrew.howell@canterbury.ac.nz',
      packages=find_packages(),
      install_requires=install_requires
      )
