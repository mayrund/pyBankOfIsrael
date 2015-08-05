from distutils.core import setup

setup(
    name='pyBankOfIsrael',
    version='0.1dev',
    author='Mayrun Digmi',
    author_email='mayrun@gmail.com',
    packages=['bankofisrael'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    install_requires=[
	'BeautifulSoup'
    ],
)
