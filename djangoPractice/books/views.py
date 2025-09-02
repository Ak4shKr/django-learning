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
from .models import Book, User
from .serializers import BookSerializer, UserSerializer
from .permissions import IsManager  
from rest_framework.permissions import IsAuthenticated

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

#delete all books at once
class DeleteAllBooksAPIView(APIView):
    permission_classes = [IsManager]
    def delete(self, request, *args, **kwargs):
        try:
            count, _ = Book.objects.all().delete()

            if count == 0:
                return Response(
                    {"message": "No books found to delete"},
                    status=status.HTTP_404_NOT_FOUND
                )

            return Response(
                {"message": f"Deleted {count} books"},
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {"error": "Unexpected error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CreateUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "message": "Users fetched successfully",
            "count": users.count(),
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
    
    
class UserDetailAPIView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({
                "message": f"User with id {id} not found"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response({
            "message": "User fetched successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
        
class UserLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Check if both fields are provided
        if not email or not password:
            return Response(
                {"error": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Compare password with given password
        if not (user.password == password):
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "is_manager": user.is_manager,
                }
            },
            status=status.HTTP_200_OK
        )

