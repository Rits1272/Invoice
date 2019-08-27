from django.db import models
# Create your models here.

class Invoice_Data(models.Model):
    description = models.CharField(max_length=50)
    hsn = models.CharField(max_length=30)
    pack = models.CharField(max_length=15)
    batch = models.CharField(max_length=20)
    exp_date = models.CharField(max_length=10)
    qty = models.IntegerField()
    free = models.CharField(max_length=20, blank=True)
    mrp = models.IntegerField()
    rate = models.IntegerField()
    gst = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.hsn
