import math
import matplotlib.pyplot as plt
import time
from wifi import Cell,Scheme
def calc_distance(s,f):
    #print(f)
    e=(27.55-(20*(math.log10(f*1000)))+abs(s))/20.0
    return 10**e

def scanForCells():
    cells=Cell.all('wlan0')
    r1=0
    r2=0
    r3=0
    for cell in cells:
        h=(map(int,cell.quality.split('/')))
        qlty=float(h[0])/float(h[1])
        cell.summary='SSID {} / Quality {} / Signal{} /Frequency {}'.format(cell.ssid,cell.quality,cell.signal,cell.frequency)
        distance=calc_distance(cell.signal,float(cell.frequency.split(' ')[0]))                    
        #distance=distance*qlty
        cell.summary=cell.summary+' / Distance {}'.format(distance)
        if cell.encrypted:
            enc_yes_no='*'
        else:
            enc_yes_no='()'

        cell.summary=cell.summary+' / Encryption {} '.format(enc_yes_no)

        print(cell.ssid,qlty)
        if(str(cell.ssid) == 'shaktimaan'):
            r1=distance
        if(str(cell.ssid) == 'Pra'):
            r2=distance
        if(str(cell.ssid) == 'Moto G5+'):
            r3=distance
    return r1,r2,r3
def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

def connectpoints1(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'r-')

hotspot=["shaktimaan","Pra","Moto G5+"]
d=int(input())
i=float(input())
j=float(input())

while True:
    r=list(scanForCells())
    #for cell in cells:
    #    print(cell.summary)
    print("---------------------------------------")
    for h in range(3):
        print(hotspot[h],r[h])


    x1,y1,x2,y2,x3,y3=[0,0,d,0,i,j]

    r1,r2,r3=r[0],r[1],r[2]

    x=(r1**2-r2**2+d**2)/(2*d)
    y=(r1**2-r3**2+i**2+j**2)/(2*j)-(i*x)/j
    z=(r1**2-x**2-y**2)**(1/2)
    xaxis=[0.0,d,i,x]
    yaxis=[0.0,0.0,j,y]




    plt.scatter(xaxis,yaxis, color=['Blue','Blue','Blue','Green'])
    plt.axis([min(i,0,x)-0.25, max(d,i,x)+0.25, min(0,j,y)-0.25, max(0,j,y)+0.25])

    for i in range(2):
        connectpoints(xaxis,yaxis,i,i+1)
        connectpoints1(xaxis,yaxis,3,i)
        
    connectpoints(xaxis,yaxis,2,0)
    connectpoints1(xaxis,yaxis,3,2)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')


    plt.show(block=False)
    time.sleep(5)
    plt.close()
    print(x,y,z)



