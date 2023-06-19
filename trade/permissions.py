from django.shortcuts import redirect


class RedirectHomeIfLogInMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)