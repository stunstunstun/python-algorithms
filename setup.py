import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

setup(name='awesome-algorithms',
      version='0.1.0',
      description='Practices to solve problems with Python',
      long_description=long_description(),
      url='https://github.com/stunstunstun/awesome-algorithms',
      author='stunstunstun',
      author_email='agileboys.com@gmail.com',
      license='MIT',
      packages=find_packages(),
      python_requires='>=3',
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)