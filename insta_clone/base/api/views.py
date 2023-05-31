from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import Post
from .serializers import PostSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def api_routes(request):
    routes = {
        "api/": "api home",
        "api/get-posts/": "get all posts",
        "api/get-posts/<id:int>/": "get single post",
    }
    return Response(routes)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_posts(request):
    post = Post.objects.all()

    serializer = PostSerializer(post, many=True)

    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_post(request, pk):

    post = Post.objects.get(id=pk)

    serializer = PostSerializer(post, many=False)

    return Response(serializer.data)
