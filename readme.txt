# project creation
django-admin startproject smartstats

cd smartstats
python manage.py startapp data

# change admin password
python manage.py changepassword admin
forstats

# data migration for data
python manage.py makemigrations data
python manage.py sqlmigrate data 0002
python manage.py migrate
