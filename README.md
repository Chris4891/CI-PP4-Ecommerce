# Django Shop

# Live Link

http://chris4891.pythonanywhere.com/

# Installation

`pip install django`

`virtualenv env`

# For Mac/ Linux

`source env/bin/activate`

# For Window

`./env/Scripts/activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python -m manage runserver`

# For Admin Login

```python
python manage.py createsuperuser
Username : admin
Password : 12345678
```


# Postgresql Configuration

Migrating from SQLite to PostgreSQL:
Prerequisites
Ensure you have PostgreSQL installed and running on your server.
Have your PostgreSQL credentials (database name, username, and password) ready.
Make sure you have a backup of your SQLite database in case anything goes wrong.
Step 1: Install Required Packages
Install the psycopg2 package, which is a PostgreSQL adapter for Django.
pip install psycopg2


'Creating a Postgresql Db'
createdb your_database_name
python manage.py migrate

'Creating user'
sudo -u postgres psql
createuser --interactive --pwprompt your_username
to exit => \q

OR 
for creating user other method:
CREATE USER your_username WITH PASSWORD 'your_password';
ALTER ROLE your_username SUPERUSER;
\q


