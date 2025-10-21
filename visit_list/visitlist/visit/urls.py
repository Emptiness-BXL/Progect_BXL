from django.urls import path
from .views import visit, skills, hobbies, me, visit1, visit2, visit3

urlpatterns = [
    path('',visit,name = 'visit'),
    path('hobbies/',hobbies,name = 'hobbies'),
    path('skills/',skills, name = 'skills'),
    path('me/',me, name = 'me'),
    path('visit1/',visit1, name = 'hobbies'),
    path('visit2/',visit2, name = 'skills'),
    path('visit3/',visit3, name = 'me'),

]