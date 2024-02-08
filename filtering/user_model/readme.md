# In this we try to learn about Changing the old password to new password..

* [check_password(old_password)] using this function we check for the old_password from the table..

* [validate_password(new_password)] using this function we check for the parameters required for the password to set..

* Validate for [new_password] and [old_password] are same or not..

* Using [update(instance,validated_data] , [instance-data] [validated_data-new_data]  update the [instance.set_password(validated_data)]

* Save the Instance [instance.save()] 
* return it as well..
* 