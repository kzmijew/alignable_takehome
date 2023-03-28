# Alignable Data Science Take-Home




## Setup

### Pyenv

Set up pyenv

```
pyenv virtualenv 3.10.6 alignable
pyenv local alignable
```


### Poetry
Installs all dependencies using [Poetry](https://python-poetry.org/docs/).

```
poetry install
```




### Installing Postgres

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
`pgcli -U dev -h 127.0.0.1 -d postgres`



