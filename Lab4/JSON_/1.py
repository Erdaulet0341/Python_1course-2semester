import json
from textwrap import indent

with open("Sample-data.json", "r") as json_file:
    json_ = json.load(json_file)
    
print("\n")    
print("Interface status")
print('==========================================================================')
print("DN                                          Discription     Speed      MTU")          
print('----------------------------------------    --------------  ---------  ----')

imdata = json_["imdata"]
cnt = 10

for i in range(len(imdata)):
    for j in imdata[i]:
        for k in imdata[i][j]:
            cnt+=1
            speed= imdata[i][j][k]['speed']
            mtu = imdata[i][j][k]['mtu']
            print(F"topology/pod-1/node-201/sys/phys-[eth1/{cnt}]                  {speed}     {mtu}")