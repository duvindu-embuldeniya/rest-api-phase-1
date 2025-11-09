from django.shortcuts import render
from rest_framework import viewsets

#1.......................................................................
from . models import UserProfile
from . serializers import UserProfileSerializer

from rest_framework.authentication import TokenAuthentication
from . permissions import UpdateOwnProfile
from rest_framework import filters

#2.......................................................................
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#3.......................................................................
from . models import ProfileFeedItem

from . serializers import ProfileFeedItemSerializer

from . permissions import UpdateOwnStatus

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # even we logged-in,need to pass Token Header
    authentication_classes = [TokenAuthentication]

    permission_classes = [UpdateOwnProfile]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']





class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




class ProfileFeedViewSet(viewsets.ModelViewSet):
    "handle creating, reading, updating profile feed items"
    queryset = ProfileFeedItem.objects.all()
    serializer_class = ProfileFeedItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnStatus, IsAuthenticated]

    def perform_create(self, serializer):
        """Sets the user profile to logged in user"""
        serializer.save(user_profile = self.request.user)
