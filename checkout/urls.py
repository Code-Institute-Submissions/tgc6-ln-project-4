from django.urls import path
import checkout.views

urlpatterns = [
    path('', checkout.views.charge, name='charge'),
    # path('success/', checkout.views.success, name='success'),
    # path('cancelled/', checkout.views.cancelled, name='cancelled'),
    # path('completed/', checkout.views.completed, name='completed'),
    # path('charge/', checkout.views.charge, name='charge'),
]