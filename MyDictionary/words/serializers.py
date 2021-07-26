from rest_framework import fields, serializers

from .models import Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = (
            'user',
            'original_word',
            'translate_original_word',
            'transcription',
            'create_date',
            'slug',
            'get_absolute_url'
        )
