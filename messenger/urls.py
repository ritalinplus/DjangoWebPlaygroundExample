from django.urls import path
from messenger.views import ThreadList, ThreadDetail, add_message, start_thread

messenger_patterns = ([
    path('', ThreadList.as_view(), name="thread_list"),
    path('thread/<int:pk>', ThreadDetail.as_view(), name="thread_detail"),
    path('thread/<int:pk>/add/', add_message, name="thread_add"),
    path('thread/start/<username>', start_thread, name="thread_start"),
], "messenger")
