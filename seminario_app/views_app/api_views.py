from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from ..models import Inscrito, Institucion
from ..serializers import InscritoSerializer, InstitucionSerializer


@api_view(['GET'])
def autor_info(request):
    return Response({
        "Autor": "Victoria Saldaña",
        "Email": "victoria1236@gmail.com",
        "Carrera": "Analista Programador",
        "Nacionalidad": "Chilena",
    })


class InscritoAPI(ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InstitucionAPI(ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
