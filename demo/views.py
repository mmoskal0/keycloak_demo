from rest_framework import viewsets
from . import models, serializers


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    queryset = models.Question.objects.all()
    keycloak_roles = {
        'GET': ['director'],
    }