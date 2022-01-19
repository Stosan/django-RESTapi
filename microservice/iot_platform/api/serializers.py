from rest_framework import serializers
from iot_platform.models import PayloadDevice


class PayloadDeviceServeSerializer(serializers.ModelSerializer):
    #id = serializers.CharField(source='id_id.name')
    
    
    class Meta:
        model = PayloadDevice # this is the model that is being serialized
        fields = [
        'device',
        'time',
        'data',
        'seqNumber',
        'deviceTypeId'
        ]