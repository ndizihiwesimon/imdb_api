from rest_framework.decorators import api_view

from user.api.serializers import RegistrationSerializer


@api_view(['POST', ])
def register_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
