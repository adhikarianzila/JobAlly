
from django.urls import path
from . import views
from core.views import job, contact, register, user, intern


# router = routers.DefaultRouter()
# router.register(r'job', views.JobViewSet, basename='JobViewSet')
urlpatterns = [
    path('jobs/', job, name='job'),
    path('intern/', intern, name='intern'),
    path('register/', register, name='register'),
    path('user/', user, name='user'),
    path('contact/', contact, name='contact'),
]
