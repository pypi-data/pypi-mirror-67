# pip-grab

https://pypi.org/project/pip-grab/#description
https://github.com/QuantumNovice/pip-grab

# Installation
`pip install pip-grab`

# Motivation
`pip install this`, `pip install that`, `conda install this`, `conda install that`
and you never know when pip will break conda environment or conda will break pip.
That's why it's better to keep backup of your installed packages so you can revert
changes.


# Usage
```cmd
pip-grab.py [-h] [-s] [-g] [-t TICKER]

Grabs currently installed pip packages.

optional arguments:
  -h, --help            show this help message and exit
  -s, --save            Save packages
  -g, --grab            Display packages
  -t TICKER, --ticker TICKER
                        Save installed packages after N seconds
```


# Examples
`py pip-grab.py --ticker 590000`

# Output
```cmd
[+] Loop Started
[+] Enivronment grabs after every 2.7314814814814814 hours
```
