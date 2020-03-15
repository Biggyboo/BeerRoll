import uuid

import django.db.models as models
import django.core.validators as validators
import decimal


class Category(models.Model):
    id_category = models.UUIDField(default=uuid.uuid4, primary_key=True)
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Origin(models.Model):
    id_origin = models.UUIDField(default=uuid.uuid4, primary_key=True)
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Quantity(models.Model):
    id_Quantity = models.UUIDField(default=uuid.uuid4, primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.quantity)


class Beer(models.Model):
    id_beer = models.UUIDField(default=uuid.uuid4, primary_key=True)
    label = models.CharField(max_length=50)
    brasserie = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    quantity = models.ManyToManyField(Quantity, through='BeerQuantity')
    alcohol_level = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    bitterness = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(150)])

    def __str__(self):
        return self.label


class BeerQuantity(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['beer', 'quantity'], name='unique beerquantity')
        ]

    stock = models.BooleanField(default=True, null=True)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
