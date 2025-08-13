from django.contrib import admin
from django.urls import path
from webhooks.views import WebhookOrderView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/V1/webhooks/order/', WebhookOrderView.as_view(), name='webhook-order'),
]
