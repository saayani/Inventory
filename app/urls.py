from django.urls import path, re_path
import app.views

urlpatterns = [
   re_path(r'^create-brand/', app.views.create_brand, name='create_brand'),
   re_path(r'^create-item/', app.views.create_item, name='create_item'),
   path('', app.views.index, name='index'),
]
