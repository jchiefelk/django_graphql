from django.http import JsonResponse
from rest_framework.decorators import api_view
from drugs.models import Drug


@api_view(['GET'])
def get_drugs(request):
    return JsonResponse({
        "data": list(Drug.objects.values())
    })
