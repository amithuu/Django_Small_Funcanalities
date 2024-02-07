# In this Model We are Trying to Logout user using [simplejwtToken]

# In Setting.py

* ['rest_framework_simplejwt.token_blacklist'],

* In View.py Create a view for logout, collecting the [refresh_token] and adding [permission_class=(IsAuthenticated,)]
* add that [refresh_token] to [RefreshToken(refresh_token).blacklist()]
* Send message 

# In post man
* Login and collect the [access_token] and paste in [BearerToken]
* Collect the [refresh_token] and paste in [body]