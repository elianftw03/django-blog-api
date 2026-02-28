from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, RegisterSerializer
from .permissions import IsManager


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content", "category", "author__username"]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]

        if self.action == "comments":
            if self.request.method == "POST":
                return [permissions.IsAuthenticated()]
            return [permissions.AllowAny()]

        return [IsManager()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["get", "post"], url_path="comments")
    def comments(self, request, pk=None):
        article = self.get_object()

        if request.method == "GET":
            qs = article.comments.all().order_by("-created_at")
            return Response(CommentSerializer(qs, many=True).data)

        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == "destroy":
            return [IsManager()]
        return [permissions.AllowAny()]

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Use /api/articles/<id>/comments/"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)