from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso,Avaliacao
from .serializers import CursoSerializer,AvaliacaoSerializer
from rest_framework import status

class CursoAPIView(APIView):
    """
    API DE CURSOS DA GEEK
    """
    def get(self,request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg":'Criou com sucesso'},serializer.data,status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API DE AVALIAÇÕES DA GEEK
    """
    def get(self,request):
        avaliacaoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacaoes,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)