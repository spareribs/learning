from rest_framework import serializers
from .models import Poem


class PoemSerializer(serializers.ModelSerializer):

    class Meta:
        # 制定元数据的model和fields
        model = Poem
        fields = ['author', 'title', 'type']
