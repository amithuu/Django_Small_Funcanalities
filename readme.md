# create folder.. 
To start the project - django-admin startproject 'projectname'
    cd projectname
    [no we will get manage.py file ]

install: pip install django and pip install rest_framework

add the rest_framework into [settings.app_labels ['rest_framework',]]

# To create admin user:
    python manage.py createsuperuser

# name:
# email: 'optional'
# password:
# confirm_password: 

admin_user_name='amith'
psw = 'amith'

To create app:
    python manage.py createapp 'appname'
    In settings.urls add [path('',include(appname.urls')]

# create models
# create serializers
# create urls.py
# create views

# python manage.py makemigrations or makemigrations 'appname'[for specific app]
# python manage.py migrate or migrate 'appname' [for specific app]
# python manage.py runserver

