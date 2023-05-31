from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class UserProfileView(View):
    initial = {"key": "value"}
    template_name = "profile.html"

    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)
        user_pro = UserProfile.objects.get(user=user)

        return render(request, self.template_name, {"user": user,
                                                    "profile": user_pro})


class RegisterUser(FormView):
    template_name = "reguser.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        username = user.username.lower()
        first_name = user.first_name = form.cleaned_data['first_name']
        last_name = user.last_name = form.cleaned_data['last_name']
        email = user.email = form.cleaned_data['email']

        password = form.cleaned_data['password']

        user = User.objects.create_user(email=email,
                                        username=username,
                                        first_name=first_name,
                                        last_name=last_name)
        user.set_password(password)

        user.save()

        bio = form.cleaned_data['bio']
        image = form.cleaned_data['image']

        profile = UserProfile(user=user, bio=bio, image=image)
        profile.save()

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class UserLoginView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(request)

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("home")
        except:
            print("user dont exist")
        return render(request, self.template_name, {})


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ["username", "first_name", "last_name",
              "email"]
    template_name = 'update_user.html'
    success_url = reverse_lazy('home')


class UserLogout(View):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")
