from django.shortcuts import redirect


#Token mixin
class AuthMixin():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("account:login")
