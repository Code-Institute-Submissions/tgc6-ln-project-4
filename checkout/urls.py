from django.urls import path
import checkout.views

urlpatterns = [
    path('checkout/',checkout.views.index),

]