import graphene
from .types import ActorType
from .models import Actor

# Create Input Object Types
class ActorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class CreateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required=True)

    ok = graphene.Boolean()
    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actor_instance = Actor(name=input.name)
        actor_instance.save()
        return CreateActor(ok=ok, actor=actor_instance)