from django.urls import path

from notification.views import home  # Importing basic home view
# Importing Notifications View
from notification.views import notification_test_page

urlpatterns = [
    path("", home, name="home"),
    path("notifications-test/", notification_test_page, name="notifications-test"),
]
