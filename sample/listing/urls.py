
from django.urls import path, include
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVirifyView
#from acc_app.views import RetriveUserView, RegisterView
from listing.views import ManagingListView
from listing.listing_views import index

urlpatterns = [
    path('manage/', ManagingListView.as_view()),
    path('login/', index, name = 'index'),
    
]