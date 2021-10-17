
from django.urls import path, include
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVirifyView
from acc_app.views import RetriveUserView, RegisterView

urlpatterns = [
    path('me/', RetriveUserView.as_view()),
    path('register/', RegisterView.as_view()),
    
]