from rest_framework import serializers 
from blog.models import *
from django.contrib.auth.models import  User


class SerializersAuthor(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User


class SerializersTags(serializers.ModelSerializer):
    # tags = serializers.CharField(read_only=True)

    class Meta:
        model = Tags
        fields = '__all__'


class SerializersGetPost(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title_post = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True) 
    resume_post = serializers.CharField(read_only=True)
    body = serializers.CharField(read_only=True) 
    post_image = serializers.CharField(read_only=True) 
    date_created = serializers.CharField(read_only=True) 
    date_updated = serializers.CharField(read_only=True) 
    tags = SerializersTags(many=True)
    author = SerializersAuthor()

    class Meta:
        model = BlogArticles




class SerializersPost(serializers.ModelSerializer):
    tags = SerializersTags(many=True)
    author = SerializersAuthor()

    class Meta:
        model = BlogArticles
        fields = '__all__'


class SerializersFormContact(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField() 
    email = serializers.CharField()
    phone = serializers.CharField() 
    message = serializers.CharField()

    class Meta:
        model = ContactModel

    def create(self, validated_data):
        contact =  ContactModel.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            message=validated_data.get('message'),
            phone=validated_data.get('phone')
            )
        return contact


class SerializersConectorCRM(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True) 
    last_name = serializers.CharField(read_only=True) 
    email = serializers.CharField(read_only=True) 
    message = serializers.CharField(read_only=True) 
    date_created = serializers.CharField(read_only=True) 
    date_updated = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)

    class Meta:
        model = ContactModel