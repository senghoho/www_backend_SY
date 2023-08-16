from rest_framework import viewsets, mixins, status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate, login

from .serializers import  UserSerializer,  SocialUserSerializer
from .models import User


# 내가 생각하는 viewset
class SocialSignUpViewset(APIView):
    queryset = User.objects.all()
    serializer_class = SocialUserSerializer

    def put(self, request):
        # user = get_object_or_404(User, pk=pk)
        user = request.user
        if user.is_authenticated:  # 사용자가 로그인되어 있는지 확인
            user.nickname = request.data.get('nickname')
            user.country = request.data.get('country')
            user.city = request.data.get('city')
            user.save()
            
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            res = Response(
                {
                    "message": "회원가입 성공!"
                },
                status=status.HTTP_200_OK,
            )
        else:
            res = Response(
                {
                    "message": "로그인된 사용자가 아닙니다."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return res
    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)

class UserViewset(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
class FriendViewset(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        user = request.user
        serializer = self.serializer_class(user)
    
# class 

# class UserViewset(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'email'
    
# 궁금한점 -> mixin으로 구현하게 되면 retrieve에서 url에 pk 를 만드는데 프론트에서 pk를 모르잖아

# # 이거는 아예 새로운 User를 만드는거
# class SignUpViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer

#     def create(self, request):
#         password = request.data.get('password')

#         user_data = {
#             'email' : request.data['email'],
#             'nickname' : request.data['nickname'],
#             'country' : request.data['country'],
#             'city' : request.data['city']
#         }

#         user = User.objects.create(**user_data)
#         # user.set_password(password)
#         user.save()

#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)

#         res = Response(
#             {
#                 "message": "회원가입 성공!"
#             },
#             status=status.HTTP_200_OK,
#             )
#         return res\

# 이것도 지금 id, password 
# class LoginAPIView(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = User.objects.get(email=email)
#         user = authenticate(request, email=email,password=password)

#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
            
#             login(request, user)
#             res = Response(
#                 {
#                     "user": {
#                         'nickname': user.nickname,
#                         'email': user.email,
#                         'country' : user.country,
#                         'city': user.city,
#                         'password' : user.password
#                     },
#                     "message": "로그인 성공!",
#                     "token": {
#                         "access": access_token,
#                         "refresh": str(refresh),
#                     },
#                 },
#                 status=status.HTTP_200_OK,
#                 )
#             return res
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class SocialUserApplyViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
#     serializer_class = SocialUserSerializer

# class UserViewSet(viewsets.GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
    
    
    