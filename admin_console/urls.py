from django.urls import path
import admin_console.views

urlpatterns = [
    path('', admin_console.views.admin_panel, name='admin_panel'),
]
