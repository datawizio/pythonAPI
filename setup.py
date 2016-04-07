import os.path
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

VERSION = "0.1dev"

setup(
    name = "python-dwapi",
    version = VERSION,
    description="Library to communicate with datawiz.io API",
    author='Victor Daniluk',
    author_email='unittest.co@gmail.com',
    maintainer='Victor Daniluk',
    maintainer_email='unittest.co@gmail@com',
    license = "http://www.gnu.org/copyleft/gpl.html",
    platforms = ["any"],    
    url="http://github.com/datawizio/pythonAPI/",
    packages=['dwapi', 'dwapi.test'],
    package_dir={'dwapi': 'dwapi'},
    install_requires = ["pandas", "httpsig", "requests", "nose"],
)