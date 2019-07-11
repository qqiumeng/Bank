from django.urls import path
from first import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('save/', views.Save.as_view(), name='save'),
    path('take/', views.Take.as_view(), name='take'),
    path('move/', views.Move.as_view(), name='move'),
    path('exit/', views.exit, name='exit')
]
