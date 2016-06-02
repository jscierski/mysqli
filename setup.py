from distutils.core import setup

setup(
    name='mysqli',
    version='0.1.1',
    author='Jacek Szpot',
    author_email='maligree@gmail.com',
    url='https://github.com/exana/mysqli',
    scripts=['scripts/mysqli'],
    requires=['termcolor']
)
