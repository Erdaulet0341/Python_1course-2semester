import json

with open("Sample-data.json", "r") as json_file:
    json_ = json.load(json_file)
    
print("\n")    
print("Interface status")
print('='*70)
print("DN                                           Discription     Speed      MTU")          
print('-------------------------------------------  --------------  ------     ----')

imdata = json_["imdata"]
for i in range(len(imdata)):
    for j in imdata[i]:
        for k in imdata[i][j]:
            speed= imdata[i][j][k]['speed']
            mtu = imdata[i][j][k]['mtu']
            dn = imdata[i][j][k]['dn']
            if dn.find('33')>0 or dn.find('34')>0 or dn.find('35')>0:
                print(f'{dn}                   {speed}    {mtu}')