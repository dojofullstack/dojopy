from rest_framework import serializers 
from blog.models import *
from django.contrib.auth.models import  User
from phonenumber_field.serializerfields import PhoneNumberField


class AuthorSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # username = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email')


class TagsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tags = serializers.CharField()

    class Meta:
        model = Tags


class ListPostSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title_post = serializers.CharField(read_only=True)
    slug = serializers.CharField(read_only=True)
    resume_post = serializers.CharField(read_only=True) 
    author = AuthorSerializer()
    body = serializers.CharField(read_only=True) 
    post_image = serializers.CharField(read_only=True) 
    date_created = serializers.CharField(read_only=True) 
    date_updated = serializers.CharField(read_only=True)
    tags = TagsSerializer(many=True)

    class Meta:
        model = BlogArticles


class DetailPostSerializers(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagsSerializer(many=True)

    class Meta:
        model = BlogArticles
        fields = '__all__'


class ContactSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200) 
    email = serializers.EmailField(max_length=200) 
    phone = PhoneNumberField()
    message = serializers.CharField(max_length=500)

    class Meta:
        model = ContactModel

    
    def create(self, data_validated):
        print('save data', data_validated)
        contact =  ContactModel.objects.create(
            email=data_validated.get('email'),
            phone=data_validated.get('phone'),
            message=data_validated.get('message'),
            first_name=data_validated.get('first_name'),
            last_name=data_validated.get('last_name'),
        )
        return contact