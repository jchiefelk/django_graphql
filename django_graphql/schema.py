import graphene

import drugs.schema

class Query(drugs.schema.Query, graphene.ObjectType):
  # This class will inherit from multiple Queries
  # as wee begin to add more apps to our project
  pass

schema = graphene.Schema(query=Query)
