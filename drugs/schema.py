import graphene
from graphene_django.types import DjangoObjectType
from drugs.models import Drug


class DrugType(DjangoObjectType):
    class Meta:
        model = Drug


class Query(object):
    all_drugs = graphene.List(DrugType)
    drug = graphene.Field(DrugType, id=graphene.Int())

    def resolve_all_drugs(self, info, **kwargs):
        return Drug.objects.all()

    def resolve_drug(self, info, **args):
        id = args.get('id')

        if id is not None:
            return Drug.objects.get(pk=id)

        return None
