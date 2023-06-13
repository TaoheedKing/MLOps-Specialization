Notes:

# To start up python debugger
pytest --pdb (filename.py)

# command for help
h

# gives context of error
l

# gives context of error on specified line number
l 10

# pulls up command menu
pytest --help

# only collects tests, don't execute them
pytest --collect-only

# runs large test and stops at first failure
pytest -x

# install a plugin called xdist
pip install pytest-xdist

# set four different test runner instances
pytest -n 4


