from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone, nickname, password=None):
        if not phone:
            raise ValueError(('users must enter Phone'))

        user = self.model(phone=phone, nickname=nickname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, nickname, password=None):
        user = self.create_user(phone=phone, nickname=nickname, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user