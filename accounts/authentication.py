from accounts.models import User,Token

class PasswordlessAuthenticationBackend(object):
    def authenticate(self, uid):
        try:
            token = Token.objects.filter(uid=uid).first()
            if not token:
                raise Token.DoesNotExist
            return User.objects.get(email=token.email)
        except User.DoesNotExist:
            return User.objects.create(email = token.email)
        except Token.DoesNotExist:
            return None

    def get_user(self,email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
