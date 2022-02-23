import json
from textwrap import indent

with open("Sample-data.json", "r") as json_file:
    json_ = json.load(json_file)
print("\n")    
print("Interface status")
print('==========================================================================')
print("DN                           Discription     Mode         Speed      MTU")          
print('---------------------------  --------------  -----------  ---------  ----')
imdata = json_["imdata"]
for i in range(len(imdata)):
    for j in imdata[i]:
        for k in imdata[i][j]:
            speed= imdata[i][j][k]['speed']
            mtu = imdata[i][j][k]['mtu']
            mode = imdata[i][j][k]['mode']
            print(F"imdata/l1PhysIf/attributes                   {mode}       {speed}     {mtu}")