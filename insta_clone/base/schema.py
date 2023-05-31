import graphene

from graphene_django import DjangoObjectType

from .models import Post, User


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'


class Query(graphene.ObjectType):
    all_post = graphene.Field(PostType, id=graphene.Int())

    def resolve_all_post(root, info, id):
        return Post.objects.get(pk=id)


class CreateMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        username = graphene.String(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, text, username):
        user = User.objects.get(username=username)
        post = Post(text=text, user=user)
        post.save()


class PostMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        text = graphene.String(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, text, id):
        post = Post.objects.get(id=id)
        post.delete()
        return PostMutation(post=post)


class Mutation(graphene.ObjectType):
    update_post = PostMutation.Field()
    create_post = CreateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
