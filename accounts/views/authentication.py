from accounts.models import Account
from ..serializers import UserSerializer, LoginSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register_view(request):
    # validate request data
    user_serializer = UserSerializer(data=request.data, context={'request': request})
    if not user_serializer.is_valid():
        return Response({
            'message': _('invalid'),
            'errors': user_serializer.errors
        }, status=422)

    # prepare response
    user = user_serializer.save()
    refresh_token = RefreshToken.for_user(user)

    return Response({
        'user': user_serializer.data,
        'tokens': {
            'access': str(refresh_token.access_token),
            'refresh': str(refresh_token),
        }
    }, status=201)


@api_view(['POST'])
def login_view(request):
    # validate request data
    login_serializer = LoginSerializer(data=request.data)

    if not login_serializer.is_valid():
        return Response({
            'message': _('invalid'),
            'errors': login_serializer.errors
        }, status=422)

    # check if not authenticated
    try:
        user = Account.objects.get(email=request.data['email'])
    except:
        user = None

    if not (user and user.check_password(request.data['password'])):
        return Response({
            'message': _('unauthenticated')
        }, status=401)

    # check if is not stuff
    if request.query_params.get('is_stuff') == 1 and user.is_staff == 0:
        return Response({'message': _('unauthorized')}, status=403)

    # prepare response
    user_serializer = UserSerializer(instance=user, context={'request': request})
    refresh_token = RefreshToken.for_user(user)

    return Response({
        'user': user_serializer.data,
        'tokens': {
            'access': str(refresh_token.access_token),
            'refresh': str(refresh_token),
        }
    }, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    user_serializer = UserSerializer(instance=request.user, context={'request': request})

    return Response({
        'message': _('success'),
        'user': user_serializer.data
    })
