from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, mobile, password, **extra_fields):
        if not mobile:
            raise ValueError(('mobile number must be set'))
        user = self.model(mobile=mobile,**extra_fields)
        user.set_password(password)
        user.save()
        return user
