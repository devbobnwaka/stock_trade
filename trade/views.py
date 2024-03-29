from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, RedirectView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from .models import Trade, Trader
from .permissions import RedirectHomeIfLogInMixin

# Create your views here.
class Home(RedirectHomeIfLogInMixin, RedirectView):
    url = reverse_lazy('login')

class Login(RedirectHomeIfLogInMixin, LoginView):
    template_name = "accounts/login.html"


class Dashboard(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if self.request.user.is_admin:
            context = {}
            traders = Trader.objects.all()
            if pk:
                trades = Trade.objects.filter(trader = pk)
                context['trades'] = trades
                context['pk'] = True
            context['traders'] = traders
            # Use the template for admin template
            return render(request, 'trade/admin_dashboard.html', context)  
        else:
            if pk:
                return redirect('dashboard')
            trades = Trade.objects.filter(trader = self.request.user)
            context = {
                "trades": trades
            }
            # Use the template for users 
            return render(request, 'trade/user_dashboard.html', context) 



class Logout(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')
