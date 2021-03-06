"""
SimTextGen - ATC0225
License: GPLv3
"""

#Any files generated by this generator need to be shared under the GPLv3 agreement
#Any files generated by this generator need to be shared under the GPLv3 agreement
#Any files generated by this generator need to be shared under the GPLv3 agreement

import re
def splitR(r):
    return re.split(r" (?![^(]*\))", r)
def convertFL2FT(num):
    #print("1",num)
    return int(num.split("L")[1])*100

parkingsFile=open("Parking.txt","r")
routesFile=open("Routes.txt","r",encoding="utf-8")
appPlane=open("pos.txt","r")
#depFile=open("dep.txt","r")
parkingsStand=[]
routesStand=[]
depStand=[]
appStand=[]
nowParking=0
DEP_AIRPORT="ZGGG"
AIRPORT_ALT=49.8
print("Loading parkings...")
for i in parkingsFile:
    parkingsStand.append(i.replace("\n",""))
print("Parkings loaded, count=%d"%len(parkingsStand))
print("Loading routes...")
for i in routesFile:
    routesStand.append(i.replace("\n",""))
print("Routes loaded, count=%d"%len(routesStand))
print("Loading Deps...")
for i in appPlane:
    appStand.append(i)
'''
for i in depFile:
    depStand.append(i)
print("Deps loaded, count=%d"%len(depStand))
'''
print("-----------")
for i in routesStand:
    if i == "(S)":
        nowParking+=1
        pass
    else:
        info=splitR(i)
        #print(info)
        parking=parkingsStand[nowParking].split(" ")
        print("PSEUDOPILOT:ALL")
        print("@N:%s:0000:1:%s:%s:%s:0:0:0"%(info[1],parking[1],parking[2],str(AIRPORT_ALT)))
        print("$FP%s:*A:I:%s:400:%s:0000:0000:%d:%s:00:00:0:0::/v/:%s"%(info[1],info[2],DEP_AIRPORT,convertFL2FT(info[4]),info[0],info[3].replace("(","").replace(")","")))
        r=info[3].replace("(","").replace(")","").split(" ")
        route=""
        '''
        for i in depStand:
            if i.startswith(info[5]):
                route=i.replace("\n","").split(":")[1]+" "
        '''
        for i in r:
            if i[1:].isdigit():
                if i[0]=="P":
                    route+=i+" "
            else:
                route+=i+" "
        print("$ROUTE:%s"%route)
        print("DELAY:1:2")
        print("REQALT::4900")
        print("")
        nowParking+=1
for i in appStand:
    info = splitR(i)
    print("PSEUDOPILOT:ALL")
    print("@N:%s:0000:1:%s:%s:0:0:0"%(info[0],info[2],str(info[1])))
    print("$FP%s:*A:I:%s:400:%s:0000:0000:%d:%s:00:00:0:0::/v/:%s"%(info[0],info[-1],info[5],convertFL2FT(info[6]),"ZGGG","NULL"))
    print("$ROUTE:%s"%info[4].replace("(","").replace(")",""))
    print("DELAY:1:2")
    print("REQALT::4900")
    print("")
