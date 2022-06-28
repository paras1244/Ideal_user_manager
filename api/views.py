
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
# from django.contrib.auth.models import 
from .models.custom_user import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    # authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdminUser, )

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class GetIdealUser(APIView):
    permission_classes = (AllowAny, )
    
    # pass the ideal user
    def get(self, request):
        from_ = request.GET['from']
        print(request.GET['to'])
        
        return Response({"msg" : "success"})