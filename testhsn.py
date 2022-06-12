from hsn_codes import aa
def test_code():
    for j in range(10):
        for i,ii in aa[j]['tax_slab'].items():
            if ii==1:
                print('gst=',i,'hsn_code=',aa[j]['hsn_code'],'hsn_description=',aa[j]['hsn_description'])