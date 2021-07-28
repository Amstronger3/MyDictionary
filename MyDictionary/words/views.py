from rest_framework.viewsets import ModelViewSet

from .models import Word
from .serializers import WordSerializer


# class WordView(APIView):
#
#     def get(self, request, format=None):
#         words = Word.objects.all()
#         serializer = WordSerializer(words, many=True)
#         return Response(serializer.data)


class WordViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


