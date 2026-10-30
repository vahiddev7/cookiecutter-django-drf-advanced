from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.authentication.serializers.register import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
    throttle_scope = "register"
