from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from iot_platform.models import PayloadDevice, PayloadGroup
from iot_platform.api.serializers import PayloadDeviceServeSerializer
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = PayloadDevice.objects.all()
        serializer = PayloadDeviceServeSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer =PayloadDeviceServeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status = status.HTTP_400_BAD_REQUEST)




#classbased view for loading API model view controller
class ApiPaylView(APIView):
    permission_classes = [
        AllowAny,
    ]
    #function to pass parameterized get query request for device id
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        """
        This method creates a get request with parameters
        uses the try exception catch for erro handling
        It queries the model for database parameters using the filter query to find and order
        values based on relationship

        Values are serialized and returned as JSON objects
        """
        try:
            if request.GET.get("id", ""):
                dev_id = request.GET.get("id", "")
                try:
                    id_payloadDevice = PayloadDevice.objects.filter(device__contains=dev_id)
                except PayloadDevice.MultipleObjectsReturned:
                     id_payloadDevice = PayloadDevice.objects.filter(device__contains=dev_id).order_by('seqNumber').first()
                serializer = PayloadDeviceServeSerializer(id_payloadDevice, many=True)
                return JsonResponse(serializer.data, safe=False)
            elif request.GET.get("time", "") and request.GET.get("data", ""):
                dev_time = request.GET.get("time", "")
                dev_data= request.GET.get("data", "")
                try:
                    qpam_payload = PayloadDevice.objects.filter(time__contains=dev_time, data__contains=dev_data)
                except PayloadDevice.MultipleObjectsReturned:
                    qpam_payload = PayloadDevice.objects.filter(time__contains=dev_time, data__contains=dev_data).order_by('device').first()
                serializer = PayloadDeviceServeSerializer(qpam_payload, many=True)
                return JsonResponse(serializer.data,safe=False)
            return JsonResponse(
                "Either provide the device name or the data and time in the query parameters!"
            )

        except Exception as e:
            return JsonResponse(f"IOT solution for Tranter-IT",safe=False)
            #JsonResponse(f"{e}",safe=False)
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        try:
            if request.POST.get("id", "") and request.POST.get("time", "") and request.POST.get("data", "") and request.POST.get("seqNumber", "") and request.POST.get("deviceTypeId", ""):
                dev_id = request.POST.get("id", "")
                dev_time = request.POST.get("time", "")
                dev_data = request.POST.get("data", "")
                dev_seq = request.POST.get("seqNumber", "")
                dev_type = request.POST.get("deviceTypeId", "")
                serializer = PayloadDeviceServeSerializer(dev_id,dev_time,dev_data,dev_seq,dev_type, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data,  status=status.HTTP_201_CREATED,safe=False)
            return JsonResponse(
                "Either provide the device name or the data and time in the query parameters!", safe=False
            )
        except Exception as e:
            return JsonResponse(f"{e}", safe=False)