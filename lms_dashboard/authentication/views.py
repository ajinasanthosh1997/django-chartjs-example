# authentication/views.py
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.shortcuts import redirect
from django.contrib.auth import logout


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def get_success_url(self):
        # Redirect to the dashboard page on successful login
        return reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Customize any additional actions you want to perform upon successful login
        # For example, you might want to log some information
        # logger.info(f"User '{self.request.user}' logged in.")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # Customize any additional actions you want to perform upon failed login
        # For example, you might want to log some information
        # logger.warning(f"Failed login attempt for user '{form.cleaned_data.get('username')}'.")
        return response

    def get(self, request, *args, **kwargs):
        # If the user is already authenticated, redirect them to the success URL
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

class LogoutView(RedirectView):
    # Note: reverse_lazy should not be called here
    # Instead, override the get_redirect_url method

    def get_redirect_url(self, *args, **kwargs):
        # Reverse the URL here
        return reverse_lazy('authentication:login')

    def get(self, request, *args, **kwargs):
        # Logout the user
        logout(request)
        # Call the parent class method
        return super().get(request, *args, **kwargs)