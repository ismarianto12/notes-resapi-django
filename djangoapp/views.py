from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Notes
from .serializers import UserSerializer,NotesSerializer 

# Create your views here.

# get all users


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# get single user


@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# add user


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    response = {
        'messages': 'data berhasil di simpan',
        'data': serializer.data
    }

    return Response(response)

# update user


@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# delete user


@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response('Item successfully deleted!')


@api_view(['GET'])
def getNotes(request):
    notes = Notes.objects.all()
    serializer = NotesSerializer(notes, many=True)
    return Response(serializer.data)

# get single Notes


@api_view(['GET'])
def getNotes(request, pk):
    notes = Notes.objects.get(id=pk)
    serializer = NotesSerializer(notes, many=False)
    return Response(serializer.data)

# add Notes


@api_view(['POST'])
def addNotes(request):
    serializer = NotesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    response = {
        'messages': 'data berhasil di simpan',
        'data': serializer.data
    }

    return Response(response)

# update Notes


@api_view(['PUT'])
def updateNotes(request, pk):
    notes = Notes.objects.get(id=pk)
    serializer = NotesSerializer(instance=notes, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# delete Notes


@api_view(['DELETE'])
def deleteNotes(request, pk):
    notes = Notes.objects.get(id=pk)
    notes.delete()

    return Response('Item successfully deleted!')
