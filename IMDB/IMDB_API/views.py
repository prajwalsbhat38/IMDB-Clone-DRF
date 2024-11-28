from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .permissions import ReviewUserOrReadOnly
from rest_framework import status

from .models import StreamingPlatform, WatchList, Reviews
from .serializer import StreamingPlatform_Serializer, WatchList_Serializer, Review_Serializer

# Create your views here.
class StreamingPLatform_View(APIView):
    def post(self, request):
        serializer = StreamingPlatform_Serializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk = None):
        if pk:
            try:
                data = StreamingPlatform.objects.get(pk = pk)
                serializer = StreamingPlatform_Serializer(data, context = {'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except StreamingPlatform.DoesNotExist:
                return Response({'error': 'Does Not Exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = StreamingPlatform.objects.all()
            if data:
                serializer = StreamingPlatform_Serializer(data, many = True, context = {'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No data found'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        try:
            data = StreamingPlatform.objects.get(pk = pk)
            serializer = StreamingPlatform_Serializer(data, data = request.data, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': 'Does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            data = StreamingPlatform.objects.get(pk = pk)
            serializer = StreamingPlatform_Serializer(data, data = request.data, partial = True, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': 'Does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            data = StreamingPlatform.objects.get(pk = pk)
            data.delete()
            return Response({'response': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

class WatchList_View(APIView):
    def post(self, request):
        serializer = WatchList_Serializer(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk =None):
        if pk:
            try:
                data = WatchList.objects.get(pk = pk)
                serializer = WatchList_Serializer(data, context = {'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except WatchList.DoesNotExist:
                return Response({'error': 'doesnotexist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = WatchList.objects.all()
            if data:
                serializer = WatchList_Serializer(data, many = True, context = {'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'no data found'})
    
    def put(self, request, pk):
        try:
            data = WatchList.objects.get(pk = pk)
            serializer = WatchList_Serializer(data, sata = request.data, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist:
            return Response({'error': 'doesnotexist'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            data = WatchList.objects.get(pk = pk)
            serializer = WatchList_Serializer(data, sata = request.data, partial = True, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist:
            return Response({'error': 'doesnotexist'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            data = WatchList.objects.get(pk = pk)
            data.delete()
            return Response({'response': 'deleted sucessfully'})
        except WatchList.DoesNotExist:
            return Response({'error': 'doesnotexist'}, status=status.HTTP_404_NOT_FOUND)

class Reviews_View(APIView):
    permission_classes = [ReviewUserOrReadOnly,]
    def get(self, request, pk):
        try:
            data = Reviews.objects.get(pk = pk)
            serializer = Review_Serializer(data, context = {'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Reviews.DoesNotExist:
            return Response({'error': 'doesnotexist'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            data = Reviews.objects.get(pk = pk)
            serializer = Review_Serializer(data, data = request.data, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Reviews.DoesNotExist:
            return Response({'error': 'does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            data = Reviews.objects.get(pk = pk)
            serializer = Review_Serializer(data, data = request.data, partial = True, context = {'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Reviews.DoesNotExist:
            return Response({'error': 'does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            data = Reviews.objects.get(pk = pk)
            data.delete()
            return Response({'response': 'deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)
        except Reviews.DoesNotExist:
            return Response({'error': 'does not exist'}, status= status.HTTP_404_NOT_FOUND)

@api_view(['GET',])
def get_watchlist_review(request, pk):
    try:
        watch = WatchList.objects.get(pk = pk)
        data = Reviews.objects.filter(watchlist = watch)
        if data:
            serializer = Review_Serializer(data, many = True, context = {'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'response': 'No reviews found'}, status=status.HTTP_204_NO_CONTENT)
    except WatchList.DoesNotExist:
        return Response({'error': 'invalid watch id'})