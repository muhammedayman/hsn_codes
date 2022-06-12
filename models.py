#django model sample

class HSNProduct(models.Model):
	code = models.CharField(max_length=100, null=True, blank=True)
	heading = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	cgst = models.FloatField(default=0.0)
	sgst = models.FloatField(default=0.0)
	igst = models.FloatField(default=0.0)
	cess = models.FloatField(default=0.0)
	gst = models.FloatField(default=0)
	price_ext_gst = models.FloatField(default=0)
	price_int_gst = models.FloatField(default=0)

	class Meta:
		db_table = 'hsn_products'