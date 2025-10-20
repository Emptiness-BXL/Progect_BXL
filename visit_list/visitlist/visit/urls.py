from django.urls import path
from .views import visit, skills, hobbies, me

urlpatterns = [
    path('',visit,name = 'visit'),
    path('hobbies/',hobbies,name = 'hobbies'),
    path('skills/',skills, name = 'skills'),
    path('me/',me, name = 'me')
]