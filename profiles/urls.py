from django.urls import path

from profiles.views import ProfilesListView, ProfilesDetailsView


profile_patterns = ([
    path('', ProfilesListView.as_view(), name='profile_list'),
    path('<username>/', ProfilesDetailsView.as_view(), name='profile_details')
], 'profiles')
