from graphene_django.types import DjangoObjectType
from .models import Actor, Movie

# Create a GraphQL type for the actor model

class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

# Create a GraphQL type for the movie model
class MovieType(DjangoObjectType):
    class Meta:
        model = Movie