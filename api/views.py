# from django.shortcuts import render

# # Create your views here.
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from .serializers import RegisterSerializer,LoginSerializer ,ProfileSerializer , ChangePasswordSerializer,SendResetPassSerializer,ResetPasswordSerializer
# from .models import Register
# from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated


# #Creating tokens manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# class RegistrationView(APIView):
#     def post(self,request):
#         serializer = RegisterSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True )
#         user = serializer.save()
#         token = get_tokens_for_user(user)
#         return Response({'mes':'this user is created...   !' ,'token':token} ,  status=status.HTTP_201_CREATED)
        

# class LoginView(APIView):
   
#     def post(self,request):
#         serializer = LoginSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.data.get('email')
#         password = serializer.data.get('password')
#         user = authenticate(email = email, password = password)
#         if user is not None:
#             token=get_tokens_for_user(user)
#             return Response({'mes':'login successes fully','token':token},status=status.HTTP_200_OK)
#         else:
#             return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_400_BAD_REQUEST)
                
    
# class ProfileView(APIView):
    
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         serializer = ProfileSerializer(request.user)
#         return Response(serializer.data)
    
# class ChangePasswordView(APIView):
   
#     permission_classes = [IsAuthenticated]
#     def post(self , request):
#         serializer = ChangePasswordSerializer(data = request.data , context ={'user': request.user})
#         serializer.is_valid(raise_exception=True)
#         return Response('Password change success fully',status=status.HTTP_201_CREATED)
    
# class SendResetPasswordView(APIView):
  
#     def post(self , request):
#         serializer = SendResetPassSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response('Password reset link send. please check your email',status=status.HTTP_200_OK)



# class ResetPasswordView(APIView):
#     def post(self , request, uid , token ):
#         serializer = ResetPasswordSerializer(data = request.data , context = {'uid':uid , 'token':token})
#         serializer.is_valid(raise_exception=True)
#         return Response('Password Reset Successfully...!', status=status.HTTP_200_OK)



from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Register
from .serializers import SerializerStudent

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.core.cache import cache

class RetriveOneData(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(request, self , id):
        
        if cache.get(id):
            data = cache.get(id)
            print('data from cache')
        else:  
            stu = Register.objects.get(id = id)
            serializer = SerializerStudent(stu)
            data = serializer.data
            print('data from db')
            cache.set(id,data,20)
        return Response(data,status=status.HTTP_200_OK)
    
class RetriveAllData(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request):
        print('this is requset',request.user)
        all = Register.objects.all()
        serializer = SerializerStudent(all , many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        

class RegistrationView(APIView):
    def post(self,request):
        serializer = SerializerStudent(data = request.data)
        serializer.is_valid(raise_exception=True )
        serializer.save()
        return Response({'mes':'success fully data add'},  status=status.HTTP_201_CREATED)
        

    
