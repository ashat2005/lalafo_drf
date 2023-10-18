from rest_framework import serializers

from apps.users.models import User
from apps.posts.serializer import PostSerializer
 
class UserSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name',
                  'email','date_joined','phone_number','profile_image','user_posts')
