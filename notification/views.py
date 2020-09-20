from .models import Notif

from .serializers import NotifSerializer
from django.contrib.auth.models import User
from onesignal_sdk.client import Client
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




class NotifView(APIView):
    
    def get(self, request, format=None):
        notifications = Notif.objects.all()
        serializer = NotifSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NotifSerializer(data=request.data)
        if serializer.is_valid():
            client = Client(app_id="58e646c1-5dbb-4003-a0af-87c7e684334b", rest_api_key="YmRkYWIzZDgtZjZhNy00MGJjLTg2YTktODcxMGUzOTUzMDJm")
            notification_body = {
            'contents': {'en': request.data["corp_de_la_notification"] },
            "headings": {"en": request.data["titre"]},
            'included_segments': ['All'],}
            client.send_notification(notification_body)
            
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    

    

