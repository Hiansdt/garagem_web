from rest_framework.viewsets import ModelViewSet

from core.models import Modelo
from core.serializers import ModeloPostSerializer, ModeloGetSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ModeloGetSerializer
        return ModeloPostSerializer