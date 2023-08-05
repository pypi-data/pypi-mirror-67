# GETDEP

[![codecov](https://codecov.io/gh/remiflavien1/getdep/branch/master/graph/badge.svg)](https://codecov.io/gh/remiflavien1/getdep)  [![PyPI version](https://badge.fury.io/py/getdep.svg)](https://badge.fury.io/py/getdep) [![Requirements Status](https://requires.io/github/remiflavien1/getdep/requirements.svg?branch=master)](https://requires.io/github/remiflavien1/getdep/requirements/?branch=master) [![Code Coverage](https://github.com/remiflavien1/getdep/workflows/Code%20coverage/badge.svg)](https://github.com/remiflavien1/getdep/actions?query=workflow%3A%22Code+coverage%22) [![Quality check](https://github.com/remiflavien1/getdep/workflows/Quality%20check/badge.svg)](https://github.com/remiflavien1/getdep/actions?query=workflow%3A%22Quality+check%22) 

Get dependencies for a given package management system and a given package. 

## Install

You can install ```getdep``` either via pip (PyPI) or from source.
To install using pip:
```bash
python3 -m pip install getdep
```
Or manually:
```
git clone https://github.com/remiflavien1/getdep 
cd getdep   
./install.sh   
python3 setup.py install   
```

For ```apt``` dependencies you need to install ```apt-rdepends```:
```bash
sudo apt install apt-rdepends
```

## Use

```bash 
>>> from getdep import getdep
>>> getdep.get_pip_dependencies("requests")
['chardet', 'idna', 'urllib3', 'certifi', 'pyOpenSSL', 'cryptography', 'PySocks', 'win-inet-pton']
>>> getdep.get_apt_dependencies("nano")
['nano', 'libc6', 'libncursesw5', 'libtinfo5', 'libgcc1', 'gcc-8-base']

# Supported package management system
>>> from getdep import utility
>>> utility.print_supported_pms()
Supported PMS are : 
         apt        
         apt-get    
         composer   
         gem        
         npm        
         yarn       
         brew       
         pip        
         choco      
         dotnet     
```

## Note 
You must have the package management system, which you are requesting, installed on your system.
