from rest_framework.serializers import ModelSerializer

from core.models import Veiculo

class VeiculoGetSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1

class VeiculoPostSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"