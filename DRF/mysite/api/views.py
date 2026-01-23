""" from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() # Esto trae todos los objetos de la clase BlogPost
    serializer_class = BlogPostSerializer
     """

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer
from datetime import datetime

@api_view(['GET'])
def get_post(request):
    blogPost = BlogPost.objects.all()
    serializer = BlogPostSerializer(blogPost, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid(): # is_valid sirve para verificar si un dato (para post o put) es válido, si cumple con las características definidas para cada campo de la entidad a manipular
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_individual_post(request, pk):
    # blogPost = get_object_or_404(BlogPost, pk=pk)
    try:
        blogPost = BlogPost.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print(blogPost)
    serializer = BlogPostSerializer(blogPost)
    print(serializer)
    blogPostDict = serializer.data
    print(blogPostDict)
    return Response(blogPostDict)


@api_view(['PUT'])
def update_post(request, pk):
    blogPost = get_object_or_404(BlogPost, pk=pk)
    serializer = BlogPostSerializer(blogPost, data=request.data, partial=True)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_post(request, pk):
    blogPost = get_object_or_404(BlogPost, pk=pk)
    blogPost.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)