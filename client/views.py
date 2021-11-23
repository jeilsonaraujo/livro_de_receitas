
from receitas.models import ReceitaModel
from client.serializers import ReceitaSerializer
from rest_framework import viewsets, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

class ReceitasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReceitaModel.objects.all()
    serializer_class = ReceitaSerializer 
    filter_backends = [filters.SearchFilter]
    search_fields = ['receita']