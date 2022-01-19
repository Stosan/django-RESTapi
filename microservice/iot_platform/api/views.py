from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.permissions import SAFE_METHODS, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from iot_platform.models import PayloadDevice, PayloadGroup
from iot_platform.api.serializers import PayloadDeviceServeSerializer
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt



#classbased view for loading API model view controller
class ApiPaylView(APIView):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = PayloadDeviceServeSerializer
    throttle_scope = "api_payloader"
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return JsonResponse(f"IOT solution for Tranter-IT",safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        """
        This method creates a get request with parameters
        uses the try exception catch for erro handling
        It queries the model for database parameters using the filter query to find and order
        values based on relationship

        Values are serialized and returned as JSON objects
        """
        try:
            payload_data=request.query_params #transfer dict object into a variable
            new_payload =  PayloadDevice.objects.create(device=payload_data["id"],
                time=payload_data["time"],data=payload_data["data"],
                seqNumber=payload_data["seqNumber"],deviceTypeId=payload_data["deviceTypeId"])
            new_payload.save()
            serializer =PayloadDeviceServeSerializer(new_payload)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse(f"Closed",safe=False, status=status.HTTP_306_RESERVED)


class APIPaylCheckView(APIView):
    def get(self,request):
        snippets = PayloadDevice.objects.all()
        if snippets != None:
            serializer = PayloadDeviceServeSerializer(snippets, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(f"empty database", safe=False)