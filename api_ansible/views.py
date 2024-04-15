from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import subprocess

class ExecutePlaybookView(APIView):
    def post(self, request, *args, **kwargs):
        playbook = request.data.get('playbook')

        if not playbook:
            return Response({
                'status': 'Error',
                'message': 'No se especificó el nombre playbook'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            command = ['ansible-playbook', playbook]
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            return Response({
                'status': 'Success',
                'message': 'Playbook ejecutado con éxito',
                'output': result.stdout
            }, status=status.HTTP_200_OK)
        except subprocess.CalledProcessError as e:
            return Response({
                'status': 'Error',
                'message': 'Error al ejecutar el playbook',
                'error': e.stderr
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)