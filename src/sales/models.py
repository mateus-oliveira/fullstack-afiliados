from django.db import models

class SalesTransaction(models.Model):
    TYPES = [
        (1, 'CREATOR_SALE'),
        (2, 'AFFILIATED_SALE'),
        (3, 'COMMISSION_PAID'),
        (4, 'COMMISSION_RECEIVED'),
    ]

    seller = models.ForeignKey('sales.Seller', verbose_name='Seller', on_delete=models.CASCADE)
    product = models.CharField('Product Description', max_length=30)
    price = models.PositiveIntegerField('Transaction value (in Cents)')
    purchased_date = models.DateTimeField('Purchased Date')
    sale_type = models.PositiveSmallIntegerField('Type', choices=TYPES)

    def save(self, *args, **kwargs):
        self.product = self.product.upper()
        super(Seller, self).save(args, kwargs)


class Seller(models.Model):
    TYPES = [
        (1, 'CREATOR'),
        (2, 'AFFILIATE'),
    ]
    name = models.CharField('Name', max_length=60)
    seller_type = models.PositiveSmallIntegerField('Type', choices=TYPES)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Seller, self).save(args, kwargs)
