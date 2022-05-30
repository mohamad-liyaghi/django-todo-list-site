from django.shortcuts import redirect


#Token mixin
class AuthMixin():
    '''
        This class let authenticated people to create new token
    '''
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("account:login")

class RegitsterMixin():
    '''
        dont let authenticated users to login/register
    '''
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("todo:home")