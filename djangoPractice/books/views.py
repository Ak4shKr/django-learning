# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Book
# from .serializers import BookSerializer

# # GET all books
# @api_view(['GET'])
# def getBooks(request):
#     books = Book.objects.all()
#     count = books.count()
#     serializer = BookSerializer(books, many=True)
#     return Response({
#         "message": "Books fetched successfully",
#         "count": count,
#         "data": serializer.data
#     }, status=status.HTTP_200_OK)

# # POST create a book
# @api_view(['POST'])
# def createBook(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message":"Book created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #DELETE a book
# @api_view(['DELETE'])
# def deleteBook(request, id):
#     try:
#         book = Book.objects.get(id=id)
#     except Book.DoesNotExist:
#         return Response({"message": f"Book with id: {id} not found"}, status=status.HTTP_404_NOT_FOUND)

#     book.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# Handle GET (list all books) and POST (create book)
class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({
            "message": "Books fetched successfully",
            "count": books.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Book created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Handle DELETE (single book by id)
class BookDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({
                "message": f"Book with id {id} not found"
            }, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
