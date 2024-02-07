# This Entire model is made for user registration and email otp and token..  



# we have to import AbstractUser
        * there are 2 types of users [abstractUser, AbstractBaseUser]
      * AbstractUser : we can define our own user class
      * AbstractBaseUser : there will be already a set of fields available using those as well if we need more fields we can add..


# In models.py file
* step1: import [AbstractUser] from [django.contrib.auth.models] 
* step2: create class by inheriting "AbstractUser"
* step3: add your fields
* step4: add USERNAME and REQUIRED_FIELDS
* step5: now we need to create [user_manager] file and class to tell that, 
    * from now i will manage the own User MOdel instead of [default_User_Model]


* step6: Create a new file [managers.py]
* step7: Import [BaseUserManager] from [django.contrib.auth.base_user]
* step8: Create a new class [CustomUserManager]

# Create createuser()
* step9: Create 2 methods [createuser] and [createsuperuser]
* step10: add the fields needed  in [createuser(self,email,password,**extra_fields)] and normalize email using[email=self.normalize(email)]
* step11: to Set the password to the model, use [user=self.model(email=email,**extra_fields)]
* step11: to Set the password to the , use [set_password(password)]
* step12: Save the user [user.save()]

# Create createsuperuser(self,email, password, **extra_fields)
* step13: add some default var as True to superuser, to differentiate from normal user like 
      * [**extra_fields.setdefault(is_superuser,is_active,is_staff),True] for all the fields..
* step14: Call the createuser() here.. [createuser(email,password,**extra_fields)]

# Go to main Settings.py

* step15:   AUTH_USER_MODEL = ['FILENAME.MODEL_NAME(in_models.py)']
    * EX: AUTH_USER_MODEL = ['create_user.CustomUser]

* cerate an instance of [objects=CustomUserManager()] in (models.py)


# if we have accessed [django.contrib.auth.models_import_User] 
    * anywhere in views or serializer we need to remove that and Use..

*  import [get_user_model] from [django.contrib.auth]
*  Create instance [User=get_user_model()] 



