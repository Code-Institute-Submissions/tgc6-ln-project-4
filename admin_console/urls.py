from django.urls import path
import admin_console.views

urlpatterns = [
    path('', admin_console.views.admin_panel, name='admin_panel'),
    path('add/', admin_console.views.admin_add, name='admin_add'),
    path('edit/<product_id>', admin_console.views.admin_edit, name='admin_edit'),
    path('remove/<product_id>', admin_console.views.admin_remove, name='admin_remove'),
]
