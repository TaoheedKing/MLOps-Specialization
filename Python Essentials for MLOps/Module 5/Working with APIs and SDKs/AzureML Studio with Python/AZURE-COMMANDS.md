Installing Azure Command-Line Interface (CLI)
---------------------------------------------------------------------------------------------------------------------------------------

# check the location your azure command line interface is coming from
which az

# check the version of your azure command line interface
az --version

# install extensions (plugins)
az extension list

# add the machine learning extension to connect to visual studio
az extension add -n ml -y (-n means name) (-y means yes)

# verify if extension was downloaded
az extension list

# check what the ml extension does
az ml --help

# authenticate
az login

# list all azure accounts
az account list -o table

Install azure python SDK for python learning
# create a virtual machine
python -m venv venv

# activate vm
source venv/bin/activate

# install azure sdk
pip install azureml-core

# run python in terminal
python

# import into terminal
import azureml

# check where azure is coming from
print(azureml)