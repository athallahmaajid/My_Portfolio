## Setup
The first thing to do is to clone the repository:

Install Postgres:
```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
```
Then enter the postgres shell with:
```
sudo -iu postgres
psql
```
Create the User and Database with:

```
CREATE DATABASE yourdbname;
CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;
```

setup the settings in project/project/settings.py:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yourdbname',
        'USER': 'youruser',
        'PASSWORD': 'yourpass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

```
$ git clone https://github.com/athallahmaajid/My_Portfolio.git
$ cd My_Portfolio
```
Create a virtual environment to install dependencies in and activate it:

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

 `pip` has finished downloading the dependencies:

```
(env)$ cd project
(env)$ python3 manage.py migrate
(env)$ python3 manage.py makemigrations apps
(env)$ python3 manage.py migrate
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.
