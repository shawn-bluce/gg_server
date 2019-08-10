from django.contrib.auth import models
from rest_framework import serializers
from rest_framework.serializers import Serializer


class UploadImageSerializer(Serializer):
    username = serializers.CharField(
        label='用户名',
        allow_blank=False,
        allow_null=False,
        help_text='用户名',
    )
    password = serializers.CharField(
        label='密码',
        allow_blank=False,
        allow_null=False,
        help_text='密码',
    )
    graph = serializers.ImageField(
        label='本次上传的图片',
        allow_null=False,
        allow_empty_file=False,
        help_text='本次上传的图片',
        ),

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = models.User.objects.filter(username=username).first()
        if user and user.check_password(password):
            return attrs
        else:
            raise serializers.ValidationError('用户名或密码错误')

    def create(self, validated_data):
        return None

    def update(self, instance, validated_data):
        # TODO: 将来要支持更新标签等操作
        raise serializers.ValidationError('该版本暂未支持put/patch')
