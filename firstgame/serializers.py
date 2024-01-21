from rest_framework import serializers
from .models import DepAppeals

class Lglserializer(serializers.ModelSerializer):
    class Meta:
        model = DepAppeals
        fields = ('id', 'indate', "physinfo", 'depsource', 'promptinfo', 'promptfile')

class ApiFullSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        apimonthdata = [
        'catstat',
        'jan', 'feb', 'mart', 'kv1', 'sum1',
        'apr', 'may', 'jun', 'kv2', 'sum2',
        'jul', 'aug', 'sept', 'kv3', 'sum3',
        'oct', 'nov', 'dec', 'kv4', 'sum4'
        ]
        outarr = {}
        for curinst in apimonthdata:
            curattr = getattr(instance, curinst)
            outarr[curinst] = curattr
        return outarr