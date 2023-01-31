from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from datetime import datetime
from django.shortcuts import render

# Create your views here.


# Basic home view
def home(request):
    return render(request, 'notification/home.html')


# Django Channels


def notification_test_page(request):

    # Django Channels Notifications Test
    current_user = request.user
    channel_layer = get_channel_layer()
    data = "notification" + "...." + str(datetime.now())
    # Trigger message sent to group
    async_to_sync(channel_layer.group_send)(
        str(current_user.pk),  # Channel Name, Should always be string
        {
            "type": "notify",   # Custom Function written in the consumers.py
            "text": data,
        },
    )
    return render(request, 'notification/notification_test_page.html')
