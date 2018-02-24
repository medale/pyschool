# Guides
* Mark Lutz, "Learning Python, 5th edition", O'Reilly Media, Inc., 2013
* Google

# Set up environment

## Install Python 3
Mac Brew: http://docs.python-guide.org/en/latest/starting/install3/osx/

Note: Need GCC or [XCode](https://developer.apple.com/xcode/)

```bash
# Install Homebrew
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Ensure dependencies installed via Homebrew are first on PATH - in ~/.profile
export PATH=/usr/local/bin:/usr/local/sbin:$PATH

# Install Python 3 (as of Python 3.4 this should have pip also)
brew install python3

# for ipython %paste support need tkinter
# On Ubuntu: sudo apt-get install python3-tk
```
## Set up a virtual environment/libraries for pyschool
In order to use the libraries/versions that we want, rather than relying on the
installed system and its libraries, we can use pipevn to create an
isolated Python environment with the desired libraries.
See documentation at http://pipenv.readthedocs.io/en/latest/basics/

* First we install pipenv: `sudo pip3 install pipenv`
* We want to create .venv environment in local project dir: `export PIPENV_VENV_IN_PROJECT=true`
* In our project directory we want to specify that we want to use ipython shell in a Python 3 environment: `pipenv install ipython --three`
* Run Python with ipython dependencies installed: `pipenv shell`
* Run ipython shell: `ipython` - exit
* Exit pipenv shell from command prompt: `exit`
* Show where virtual environment for project was created: `pipenv --venv`
* Run command from virtual environment: `pipenv run <command>`

# IntelliJ Idea with Python plugin
* Settings - Plugins - make sure Python plugin is installed
* Project Structure - Platform Settings - SDKs - + Python SDK - Add Local - Virtualenv Environment - Existing Environment - pyschool/python/.venv - OK
* Project Structure - Project - Project SDK - select .venv Python SDK from previous step - OK
* If red squigglies under print method: File -> Invalidate Caches/Restart
* Tools - Python Console (starts ipython if we installed that module, python otherwise)
* Run - Edit configuration - + - Python
* Current line/(Highlight lines) - Right-click in Python file - Execute line/selection in Console

# Miscellaneous (to be distributed)
pip install -r requirements.txt

requirements.txt:
decorator==4.1.2
networkx==1.11
nltk==3.2.4
numpy==1.13.1
six==1.10.0

https://pypi.python.org

Specify private repo: https://docs.pipenv.org/advanced/#specifying-package-indexes

# Modules to cover
* datetime
* beautifulsoup4
* xml?
* json?
* http? requester?
```
# http://python-docs.readthedocs.io/en/latest/dev/virtualenvs.html
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
```
* numpy

## IPython tips and tricks
* %quickref
* %paste
