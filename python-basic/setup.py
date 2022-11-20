import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()


setuptools.setup(
   name='python_basic',
   version='1.0',
   description='Package description',
   url='https://github.com/author/repository_name',
   author='Author Name',
   author_email='author@email.com',
   license='BSD 2-clause',
   packages=['python_basic'],
   install_requires=install_requires
)
