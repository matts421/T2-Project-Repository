import numpy
import math
import matplotlib.pyplot as plt

#Constants
h= 3.05 #height of basket
d= 4.19 #distance to hoop
db= 4.57 #distance to backboard
g= 9.8 #acceleration due to gravity
c= 0.47 #drag coefficient of sphere
m= 0.625 #mass of basketball
x= 0 #initial distance

#Variables
a= 0*math.pi/180 #alpha, start angle
b= 180*math.pi/180 #beta, max angle
da= math.pi/360
v= 6 #speed
V= 20 # max speed
dv = 0.01
y = 2.02 #height of person
p = 2.02

#Altered Variables
vy= math.sin(a)*v 
vx= math.cos(a)*v

#Euler Operators
dt= 0.001 #timestep
t= 0 #initial time
T= 3 #final time

#Plotting regimen
xswish=[] #angle, swish
yswish=[] #speed, swish
xpbank=[] #angle, perfect bank
ypbank=[] #speed, perfect bank

while v < V:
        print ('v',v)
        a= math.pi/15 
        b= math.pi/3
        while a<b:
                x = 0
                y = p 
                vy= math.sin(a)*v 
                vx= math.cos(a)*v
                t = 0
                while t<T:
                        #Euler Projectile Motion Approximation
                        y = y + vy*dt
                        vy = vy - ((g +(c*vy/m))*dt)
                        x = x + vx*dt
                        vx = vx - c*vx/m*dt
                        
                        #---Exit clauses---

                        #Edge of rim fail
                        if abs(y-h) < 0.24 and (x-d) < 0.1:
                                t = t + dt
                        #Swish
                        if abs((x-d)) < 0.1 and abs(y-(h-p)) < 0.1:
                                xswish.append(a*180/math.pi)
                                yswish.append(v)
                                t = t + dt  
                        #Idealized bankshot
                        if abs((y-h)/vy) - (0.151/vx) < 0.01 and abs(x-db) < 0.1 and abs(y-h) < 0.1:
                                xpbank.append(a*180/math.pi)
                                ypbank.append(v)
                                t = t + dt
                        else:
                                t = t + dt
                a = a + da
        v = v + dv
plt.plot(xswish,yswish,".g")
plt.plot(xpbank,ypbank,".b")
plt.legend(['Swish','Bank'], loc='upper left')
plt.xlabel("Angle (deg)")
plt.ylabel("Speed (m/s)")
plt.title("Data Set 1 (height of 2.02m)")

plt.show()
