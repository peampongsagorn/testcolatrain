from django.db.models import Q
from snippets.serializers import HeroSerializer
from rest_framework import viewsets
from snippets.models import Hero
from django.http.response import Http404
from rest_framework.decorators import action
from rest_framework.response import Response



class HeroViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    
    @action(detail=False, methods=['GET'])
    def search(self, request, *args, **kwargs):
        search_post = request.GET.get('_name')
        if search_post or search_post == '':
            try:
                dataSet = self.queryset.filter(Q(name__icontains=search_post))
            except Hero.DoesNotExist:
                raise Http404("Heroes does not exist")
        else:
            dataSet = self.queryset.all()
        heroes = self.serializer_class(dataSet, many=True)
        return Response(heroes.data)

    

