from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.KirokuView.as_view(), name='kiroku_list'),
    re_path('x/$', views.AjaxWriteView.as_view(), name='ajax_write'),
]

