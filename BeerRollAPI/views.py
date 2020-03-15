import rest_framework.response
import rest_framework.views as views
import BeerRollAPI.models as models
import BeerRollAPI.serializers as serializers
import django.db.models
import decimal
import typing


# Create your views here.

class BeerView(views.APIView):
    def get(self, request):
        beers = models.Beer.objects.all()
        serializer = serializers.BeerSerializer(beers, many=True)
        return views.Response(serializer.data)


class BeerOnStock(views.APIView):
    def get(self, request, pk):
        beers = models.BeerQuantity.objects.filter(beer_id=pk)
        serializer = serializers.BeerOnStockSerializer(beers, many=True)
        return views.Response(serializer.data)
