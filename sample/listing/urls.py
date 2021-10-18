
from django.urls import path, include
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVirifyView
#from acc_app.views import RetriveUserView, RegisterView
from listing.views import ManagingListView
urlpatterns = [
    path('manage/', ManagingListView.as_view()),
    
]