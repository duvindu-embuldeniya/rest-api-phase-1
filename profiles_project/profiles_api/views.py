from django.shortcuts import render

from rest_framework import viewsets

from . models import UserProfile
from . serializers import UserProfileSerializer

from rest_framework.authentication import TokenAuthentication
from . permissions import UpdateOwnProfile
from rest_framework import filters


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings





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