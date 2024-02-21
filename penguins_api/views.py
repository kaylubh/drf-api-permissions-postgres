from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Penguin
from .serializers import PenguinSerializer


class PenguinList(ListCreateAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer

class PenguinDetail(RetrieveUpdateDestroyAPIView):
    queryset = Penguin.objects.all()
    serializer_class = PenguinSerializer
