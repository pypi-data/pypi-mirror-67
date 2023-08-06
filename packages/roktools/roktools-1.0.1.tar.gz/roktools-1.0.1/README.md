# pyrok-tools

Python tools used in internal Rokubun projects. This repository contains the following modules:

- logger 


## Installation

pip install roktools


## Modules

### Logger

```python
from roktools import logger

logger.debug(message)

# expected 
message
```


## Deployment to PyPi

In order to deploy to PyPi

```bash
# Install twine if you do not have it already
pip install twine

# Update setuptools
python3 -m pip install --user --upgrade setuptools wheel

# Create the distribution wheel
python3 setup.py sdist bdist_wheel

# Upload the distribution wheels to the PyPi repo
python3 -m twine upload dist/*
```    

More details on deployment can be found at https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives

    
