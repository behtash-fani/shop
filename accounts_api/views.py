from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsSuperUserOrStaffReadOnly



class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.filter(is_admin=False)
    serializer_class = UserSerializer
    permission_classes = [IsSuperUserOrStaffReadOnly]