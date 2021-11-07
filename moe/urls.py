import path
from . import views

urlpatterns = [
    path('moe/', views.KirokuView.as_view(), name='kiroku_list'),
]

