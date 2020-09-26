from django.urls import path
import products.views

urlpatterns = [
    path('', products.views.index, name='home_route'),
    path('about/', products.views.about, name='about_route'),
    path('details/<product_id>',
         products.views.view_details,
         name='view_details'),
]
