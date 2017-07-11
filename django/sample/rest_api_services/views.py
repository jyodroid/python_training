from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_api_services.serializers import UserSerializer, GroupSerializer

# API endpoint that allows users to be viewed or edited
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

# API endpoint that allows groups to be viewed or edited
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
