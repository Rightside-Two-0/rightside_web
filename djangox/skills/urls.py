from django.urls import path
import blockchain.views
import skills.views

urlpatterns = [
    path('', skills.views.skills, name='skills'),
]
