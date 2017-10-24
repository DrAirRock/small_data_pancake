import pancake as p
import random as r

def R():
    return r.randint(0,10)

sdp = p.Pancake()
for z in range(0,2):
    sdp.set_val(0,0,z,R())
    for theta in range(0,6):
        sdp.set_val(1,theta,z,R())


sdp.set_val(0,0,1,100)
sdp.print_cake()