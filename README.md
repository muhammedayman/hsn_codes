# hsn_codes
test how the codes

from hsn.hsn_codes import aa
for j in range(10):
     for i,ii in aa[j]['tax_slab'].items():
         if ii==1:
             print('gst=',i,'hsn_code=',aa[j]['hsn_code'],'hsn_description=',aa[j]['hsn_description'])

example code blocks
Hsn codes help you to seed from file to database
from hsn.hsn_codes import aa
cc=len(aa)
for j in range(cc):
	for i,ii in aa[j]['tax_slab'].items():
		if ii==1:
			hh= HSNProduct.objects.filter(code=aa[j]['hsn_code'],gst=i).first()
			if not hh:
				HSNProduct.objects.create(code=aa[j]['hsn_code'],heading=aa[j]['hsn_code'],description=aa[j]['hsn_description'],gst=i)

Seeding indian State



#do in terminal
 import seeds.state_seeds
 bb = seeds.state_seeds.aa
 for i in bb:
     aa=State.objects.filter(name=i['name'])
     if not aa:
         State.objects.create(name=i['name'])
         print("success",i['name'])

seeding countries
#do in terminal
import seeds.country_seed
bb = seeds.country_seed.aa
 for i in bb:
     aa=Country.objects.filter(name=i['name'])
     if not aa:
         Country.objects.create(name=i['name'])
         print("success",i['name'])