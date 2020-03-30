from django.urls import path
import steps.views

urlpatterns = [
    path('', steps.views.one, name='block_one'),
]
