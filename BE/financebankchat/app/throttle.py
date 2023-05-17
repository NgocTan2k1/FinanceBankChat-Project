from django.contrib.auth.models import User
from rest_framework.throttling import SimpleRateThrottle
from financebankchat.services.gcaptcha import verify_recaptcha


class CaptchaThrottle(SimpleRateThrottle):
    scope = 'loginAttempts'

    def get_cache_key(self, request, view):
        user = User.objects.filter(username=request.data.get('username'))
        ident = user[0].pk if user else self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

    def check_recaptcha(self, request, view):
        if g_value := request.data.get('gcaptcha'):
            return verify_recaptcha(g_value)
        return False


    def allow_request(self, request, view):
        if self.rate is None:
            return True

        self.key = self.get_cache_key(request, view)
        if self.key is None:
            return True

        self.history = self.cache.get(self.key, [])
        self.now = self.timer()

        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()

        is_recaptcha_success = self.check_recaptcha(request, view)
        if len(self.history) >= self.num_requests or not is_recaptcha_success:
            return self.throttle_failure()

        return self.throttle_success()
