
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwarags):
        profile = Profile.objects.get(pk=kwarags['pk'])
        if not profile == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwarags)
    return decorated