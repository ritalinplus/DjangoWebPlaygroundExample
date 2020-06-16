from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from registration.models import Profile


class ProfilesListView(ListView):
    model = Profile
    paginate_by = 10
    # form_class = UserCreationFormWithEmail
    template_name = 'profiles/profile_list.html'


class ProfilesDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
