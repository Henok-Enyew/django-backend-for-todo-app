from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from first_app.models import Task
from first_app.serializers import TaskSerializer

@api_view(['GET', 'POST', 'DELETE','PUT']) 
def taskApi(request, id=0):
    if(request.method == 'GET'):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)  
        return JsonResponse(serializer.data, safe=False)
    elif(request.method == 'POST'):
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=200)
    elif(request.method == 'PUT'):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return JsonResponse({"detail": "Task not found"}, status=404)
        
        task.is_done = not task.is_done
        task.save()  
        task_serializer = TaskSerializer(task)
        return JsonResponse(task_serializer.data, status=200)
    elif request.method == 'DELETE':
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse("Deleted Succesfully", safe=False)