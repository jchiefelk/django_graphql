import graphene 

from graphene_django.types import DjangoObjectType

from drugs.models import Drugs

class DrugType(DjangoObjectType):
  class Meta:
    model = Drugs

class Query(object):
  all_drugs = graphene.List(DrugType)

  def resolve_all_drugs(self,info, **kwargs):
    return Drugs.objects.all()
