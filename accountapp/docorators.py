from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwarags):
        user = User.objects.get(pk=kwarags['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwarags)
    return decorated