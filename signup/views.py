from rest_framework import generics, permissions
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework import permissions
from knox.views import LoginView as KnoxLoginView
from profil.views import CreateProfile


class RegisterAPI(CreateProfile,generics.CreateAPIView,RegisterSerializer):
    # NB:: CETTE CLASS HERITE DE LA CLASS RegisterSerializer

    # ====== APPEL AU SEREALISER_CLASS ========#
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return super().query_set()

    # ====== Requete à la baSe de donnée ========#
    def post(self, request, *args, **kwargs):
        data = request.data
        #SEREALISATION
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # Appel au custom_create() de la RegisterSerializer avec le super() helper
        return super().custom_user_create(request, *args, **kwargs)


class LoginAPI(KnoxLoginView,LoginSerializer):
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        # Appel au custom_login() de la RegisterSerializer
        return LoginSerializer.custom_login(request)