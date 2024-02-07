#  This model is for adding Jwt Token auth for login and logout.. and while Registration as well ..

* Install [pip_install_djangorestframework-simplejwt]

# In setting.py 

* REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
} 

* INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]

* Create a serializer for [LoginSerializer] to take email and password #! dnt user model serializer [why? in serializer itself]
* create view and import [authentication] from [django.contrib.auth]
* pass the user details email and password form the serializer
* Add import  [RefreshToken] from [rest_framework_simplejwt.token]
* User the [RefreshToken.for_user(user)] to get the ['refresh'] and ['access_token']