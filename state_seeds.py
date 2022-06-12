aa=[{"name":"Madhya Pradesh"},{"name":"Maharashtra"},{"name":"Uttar Pradesh"},{"name":"Gujarat"},{"name":"Karnataka"},{"name":"Andhra Pradesh"},{"name":"Odisha"},{"name":"Chhattisgarh"},{"name":"Tamil Nadu"},{"name":"Telangana"},{"name":"Bihar"},{"name":"West Bengal"},{"name":"Arunachal Pradesh"},{"name":"Jharkhand"},{"name":"Assam"},{"name":"Ladakh"},{"name":"Himachal Pradesh"},{"name":"Uttarakhand"},{"name":"Punjab"},{"name":"Haryana"},{"name":"Kerala"},{"name":"Meghalaya"},{"name":"Manipur"},{"name":"Mizoram"},{"name":"Nagaland"},{"name":"Tripura"},{"name":"Sikkim"},{"name":"Goa"},{"name":"Delhi"},{"name":"Jammu and Kashmir"},{"name":"Andaman and Nicobar Islands"},{"name":"Dadra and Nagar Haveli and Daman and Diu"},{"name":"Puducherry"},{"name":"Chandigarh"},{"name":"Lakshadweep"}]

#do in terminal
# import seeds.state_seeds
# bb = seeds.state_seeds.aa
# for i in bb:
#     aa=State.objects.filter(name=i['name'])
#     if not aa:
#         State.objects.create(name=i['name'])
#         print("success",i['name'])