from models import User
import arrow


class SubscriptionEnded(Exception):
    pass


class EmailAuth(object):
    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            # subscription_ended = arrow.get(user.subscription_end) < arrow.now()
            # if not subscription_ended:
            #     raise SubscriptionEnded()

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
