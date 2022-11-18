import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()
                 

setuptools.setup(
   name='python_basic',
   version='1.0',
   description='Package description',
   author='Author Name',
   author_email='author@email.com',
   packages=['src'],
   install_requires=install_requires
)
