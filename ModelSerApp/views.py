from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Emp
from .serializers import EmpSer
class EmpView(APIView):
    def get(self,request,format=None):
        emps=Emp.objects.all()
        ser=EmpSer(emps,many=True)
        return Response(ser.data)

    def post(self,request):
        ser=EmpSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'message':'create'})
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

class EmpDetail(APIView):
    def get(self,request,pk,format=None):
        e=Emp.objects.get(empid=pk)
        ser=EmpSer(e)
        return Response(ser.data)
    def put(self,request,pk,format=None):
        e=Emp.objects.get(empid=pk)
        ser=EmpSer(e,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'message':'updated'})
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        e=Emp.objects.get(empid=pk)
        e.delete()
        return Response({'message':'deleted'})