from rest_framework.serializers import ModelSerializer

from core.models import Modelo

class ModeloGetSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
        depth = 1

class ModeloPostSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"