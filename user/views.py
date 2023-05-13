from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterUserSerializer
from user.models import User
from user.serializers import UserSerializer, PasswordSerializer, CheckUserSerializer, VerifyAccountSerializer
from .emails import send_otp_via_email


class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                print("ha")
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'registration successfully check email',
                    'data': serializer.data,
                })

            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors,
            })
        except Exception as e:
            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': serializer.errors,
            })


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'status': 400,
                        'message': 'email does not exist',
                        'data': serializer.errors,
                    })
                if user[0].otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'otp is wrong',
                        'data': 'wrong otp'
                    })
                user = user.first()
                user.is_active = True
                user.save()
                return Response({
                    'status': 200,
                    'message': 'Account verified',
                    'data': {}
                })

            return Response({
                'status': 400,
                'message': 'something went wrong',
                'data': 'invalid email'
            })

        except Exception as e:
            print(e)


class UserViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'option']

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes=[])
    def login(self, request, pk=None):
        queryset = self.get_queryset()
        serializer = request.data
        try:
            user = queryset.get(username=serializer['username'])
            if not user.check_password(serializer['password']):
                return Response({'user': 'password is invalid'},
                                status=412)
            elif not user.is_active:
                return Response({'user': 'user is blocked', 'valid': False},
                                status=412)
            else:
                return Response({'username': user.username,
                                 'role': user.user_type,

                                 'fullname': user.get_full_name()
                                 })
        except User.DoesNotExist:
            return Response('user not found',
                            status=status.HTTP_404_NOT_FOUND)

