from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobSerializer, ContactSerializer, InternshipSerializer, RegistrationSerializer, UserSerializer
from .models import JobModel, InternshipModel
from .models import RegistrationModel, UserModel, ContactModel
# Create your views here.


def front(request):
    context = {
    }

    return render(request, "index.html", context)

# jobapi


@api_view(['GET', 'POST'])
def job(request):

    if request.method == 'GET':
        job = JobModel.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def job_detail(request, pk):
#     try:
#         job = JobModel.objects.get(pk=pk)
#     except JobModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'DELETE':
#         job.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# internshipapi


@api_view(['GET', 'POST'])
def intern(request):

    if request.method == 'GET':
        intern = InternshipModel.objects.all()
        serializer = InternshipSerializer(intern, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InternshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# registerapi


@api_view(['GET', 'POST'])
def register(request):

    if request.method == 'GET':
        register = RegistrationModel.objects.all()
        serializer = RegistrationSerializer(register, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# loginapi


@api_view(['GET', 'POST'])
def user(request):

    if request.method == 'GET':
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# contactapi


@api_view(['GET', 'POST'])
def contact(request):

    if request.method == 'GET':
        contact = ContactModel.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
