from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoGetSerializer, VeiculoPostSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VeiculoGetSerializer
        return VeiculoPostSerializer