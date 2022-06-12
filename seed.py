
#seeding hsn codes to HSNProduct table

from hsn_codes import aa
cc=len(aa)
for j in range(cc):
	for i,ii in aa[j]['tax_slab'].items():
		if ii==1:
			hh= HSNProduct.objects.filter(code=aa[j]['hsn_code'],gst=i).first()
			if not hh:
				HSNProduct.objects.create(code=aa[j]['hsn_code'],heading=aa[j]['hsn_code'],description=aa[j]['hsn_description'],gst=i)