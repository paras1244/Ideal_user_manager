
# Create your views here.
from multiprocessing import context
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import IdealUserSerializer, UserSerializer, RegisterSerializer
from .models import User, Events

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
        start_date = request.GET.get('start')
        end_date = request.GET.get('end')
        events_obj = Events.objects.filter(start_time__gte=start_date, end_time__lte=end_date)
        a = []
        for i in events_obj:
            a.append(i.user.id)
        users_obj = User.objects.exclude(id__in=a)
        serializer = IdealUserSerializer(users_obj, many=True, context={"start" : start_date, "end" : end_date})
        return Response(serializer.data)