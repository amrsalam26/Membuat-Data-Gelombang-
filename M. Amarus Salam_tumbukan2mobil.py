from vpython import *
#GlowScript 3.2 VPython
b1 = box( pos=vector(-1.5,0,1), size=vector(1.5,0.5,1), color=color.red )
bodi1 = box( pos=vector(-1.5,0.3,1), size=vector(1.5,0.5,1), color=color.red )
b2 = box( pos=vector(1.5,0,1),  size=vector(1.5,0.5,1), color=color.yellow ) 
bodi2 = box( pos=vector(1.5,0.3,1),  size=vector(1.5,0.5,1), color=color.yellow ) 
b3 = box( pos=vector(1,-0.2,1), size=vector(5,0.1,5), color=color.blue )
r1 = cylinder( pos=vector(-2,0,0), size=vector(2,0.5,0.5), axis=vector(0,0,1), color=color.white ) 
r2 = cylinder( pos=vector(-1,0,0), size=vector(2,0.5,0.5), axis=vector(0,0,1), color=color.white )
r3 = cylinder( pos=vector(1,0,0), size=vector(2,0.5,0.5), axis=vector(0,0,1), color=color.white ) 
r4 = cylinder( pos=vector(2,0,0), size=vector(2,0.5,0.5), axis=vector(0,0,1), color=color.white )

dx = 0.02


# Membuat tumbukan variable and ditambahkan untuk while condition.
tumbukan = False
while (not tumbukan):
    rate(100)
    b1.pos.x = b1.pos.x + dx
    bodi1.pos.x = bodi1.pos.x + dx
    b2.pos.x = b2.pos.x - dx
    bodi2.pos.x = bodi2.pos.x - dx
    r1.pos.x = r1.pos.x + dx
    r2.pos.x = r2.pos.x + dx
    r3.pos.x = r3.pos.x - dx
    r4.pos.x = r4.pos.x - dx
   
    # Pengecekan untuk Tumbukan 
    distance_x = abs(b1.pos.x-b2.pos.x)
    tumbukan = (distance_x < (b1.size.x+b2.size.x)/2)
    
while (not tumbukan):
    rate(100)
    b1.pos.x = b1.pos.x -dx
    bodi1.pos.x = bodi1.pos.x - dx
    b2.pos.x = b2.pos.x + dx
    bodi2.pos.x = bodi2.pos.x + dx
    r1.pos.x = r1.pos.x - dx
    r2.pos.x = r2.pos.x - dx
    r3.pos.x = r3.pos.x + dx
    r4.pos.x = r4.pos.x + dx
      # Pengecekan untuk Tumbukan. 
    distance_x = abs(b1.pos.x+b2.pos.x)
    tumbukan = (distance_x < (b1.size.x-b2.size.x)/2)

# lakukan sesuatu untuk momentum
print("Tumbukan Dua Mobil !")