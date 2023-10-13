from setuptools import setup, find_packages
from distutils.command.install import INSTALL_SCHEMES
from os import sys, path
import os
import shutil
import re
from glob import glob
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

from imp import find_module

try:
    find_module('numpy')
except:
    sys.exit('### Error: python module numpy not found')

try:
    find_module('pyfits')
except:
    try:
        find_module('astropy')
    except:
        sys.exit('### Error: python module pyfits not found')

try:
    find_module('pyraf')
except:
    sys.exit('### Error: python module pyraf not found')

try:
    find_module('matplotlib')
except:
    sys.exit('### Error: python module matplotlib not found')


verstr = "unknown"
try:
    parentdir = os.getcwd() + '/'
    verstrline = open(parentdir + '/src/ntt/_version.py', "rt").read()
except EnvironmentError:
    pass  # Okay, there is no version file.
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise RuntimeError("unable to find version in " +
                           parentdir + "+src/ntt/_version.py")


setup(
    name='ntt',
    version=verstr,
    author='S. Valenti',
    author_email='stefano.valenti@oapd.inaf.it',
    scripts=['bin/PESSTOEFOSC1dSPEC', 'bin/PESSTOFASTSPEC',
                 'bin/PESSTOSOFI2dSPEC', 'bin/PESSTOEFOSC2dSPEC',
                 'bin/PESSTO', 'bin/PESSTOSOFIPHOT',
                 'bin/PESSTOEFOSCPHOT', 'bin/PESSTOSOFI1dSPEC',
                 'bin/PESSTOWISE', 'bin/PESSTOASTRO',
                 'bin/vizquery'],
    url='ftp.oapd.inaf.it',
    license='LICENSE.txt',
    description='NTT is a package to reduce efosc and sofi data',
    long_description=open('README.txt').read(),
    # ext_modules = [('standard',
    #   { 'include_dirs': ['standard'] }
    #  )]
    requires=['numpy', 'pyfits', 'pyraf', 'matplotlib'],
    packages=['ntt'],
    package_dir={'': 'src'},
    # include_package_data=True,
    package_data={'ntt' : ["standard/MAB/*", "standard/ident/*", "standard/cat/*", "standard/extinction/*",\
                           "standard/fits/*", "standard/sex/*", "standard/stdlist/*", "standard/flux/*",\
                           "archive/efosc/badpixels/*", "archive/efosc/arc/*/*/*/*fits", "archive/efosc/arc/*/*/*/*/id*",\
                           "archive/efosc/flat/*/*fits", "archive/efosc/sens/*/*/*fits", "archive/efosc/bias/*fits",\
                           "archive/sofi/illumination/*/*fits", "archive/sofi/flat/*/*fits",\
                           "archive/efosc/fringing/*/*fits", "archive/sofi/arc/*/*/*/*fits", "archive/sofi/arc/*/*/*/*/id*",
                           "archive/fors2/sens/*/*/*fits", "archive/fors2/arc/*/*/*/*fits", "archive/fors2/arc/*/*/*/*/id*",
                           "archive/afosc/sens/*/*/*fits", "archive/afosc/arc/*/*/*/*fits", "archive/afosc/arc/*/*/*/*/id*",
                           "archive/lrs/sens/*/*/*fits", "archive/lrs/arc/*/*/*/*fits", "archive/lrs/arc/*/*/*/*/id*"]}
    #    data_files = [('',["standard/*.txt"])]
)
