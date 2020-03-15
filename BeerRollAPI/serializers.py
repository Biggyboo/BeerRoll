import rest_framework.serializers as serializers
import BeerRollAPI.models as models


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Origin
        fields = ['label']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['label', 'description']


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quantity
        fields = "__all__"


class BeerSerializer(serializers.ModelSerializer):
    origin = OriginSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    quantity = QuantitySerializer(many=True, read_only=True)

    class Meta:
        model = models.Beer
        fields = "__all__"


class BeerLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Beer
        fields = ['label']


class BeerOnStockSerializer(serializers.ModelSerializer):
    beer = BeerLabelSerializer(read_only=True)
    quantity = QuantitySerializer(read_only=True)

    class Meta:
        model = models.BeerQuantity
        fields = "__all__"
