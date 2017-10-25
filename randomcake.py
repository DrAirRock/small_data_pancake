import pancake as p
import random as r

def R():
    return r.randint(0,10)


def random_pancake():
    sdp = p.Pancake()
    for z in range(0,2):
        sdp.set_val(0,0,z,R())
        for theta in range(0,6):
            sdp.set_val(1,theta,z,R())
    return sdp 


