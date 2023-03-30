# Alignable Data Science Take-Home
Kirk Zmijewski (2023)

## Overview 
This repository is a python package with a CLI that uses Click, but also contains two Jupyter notebooks which demonstrate some quick EDA and visualization of the data. A README in that folder has some summary information.

Additionally, the `sql` file contains `1_table_setup.sql` which sets up a schema and the data tables with appropriate typing and `ENUM` classes to ensure data integrity. The `2_events_wide.sql` file outputs a joined wide view of all of the data which allows for easy summarization which is done in `3_summary.sql`. The `.sh` script uploads the files to the appropriate tables after script #1 has been executed. This is a quick and dirty way to get data into a local postgres, but can also be accomplished using SQLAlchemy ORM.

Finally, a basic CLI was set up using Click to provide an interface to verify the data and get an output summary. 

### Assumptions Made
* A session uuid in sessions_events has multiple rows (possible duplicates) that represent multiple of the same action in a single session (i.e. a user accepts multiple connections in a single session).
* All clicked emails are also opened (you have to open an email to click any content...)

## CLI
There is a CLI interface using Click which can be accessed using Poetry or after installing the package with setuptools.

`poetry run emailtools {command}`

```
  Alignable email stats CLI.

Options:
  --verbose  Print verbose help messages.
  --help     Show this message and exit.

Commands:
  click_open_rates         Get click and open rates.
  connection_requests      Get connections.
  conversation_engagement  Get conversations.
  run                      Answers questions in plain text in the logger.
  summary                  Displays summary of email data.
```

## Environment Setup
This repo uses Poetry to handle packages and virtual environments.
### Pyenv

Set up pyenv

```
pyenv virtualenv 3.10.6 emailtools
pyenv local emailtools
```
### Poetry
Installs all dependencies using [Poetry](https://python-poetry.org/docs/).

```
poetry shell
poetry install

# if issues with lock file
poetry lock 
```

### Testing
`pytest -v`

### Postgres Setup for Linux

'''
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql

# Not necessary, but better CLI than psql
sudo apt-get install pgcli
'''

Start / status / restart DB service

'''
sudo service postgresql status
sudo service postgresql start
sudo service postgresql restart
'''

Connect to DB
`pgcli -U dev -h localhost -d postgres`



