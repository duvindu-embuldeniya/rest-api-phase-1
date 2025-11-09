from . models import UserProfile, ProfileFeedItem
from rest_framework import serializers



class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""

    password = serializers.CharField(write_only=True,
                                     style={'input_type':'password'},
                                     min_length = 8)

    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'password']
    
    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            validated_data['email'],
            validated_data['name'],
            validated_data['password']
        )
        return 
    
    def update(self, instance, validated_data):
        """Handle updating user password senario"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)





class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeedItem
        fields = '__all__'

        extra_kwargs = {'user_profile': {'read_only':True}}