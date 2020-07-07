from pycoin.ecdsa import Point
from pycoin.ecdsa import CurveFp

curve = CurveFp(17, 0, 7)
print("Curve = " + str(curve))

G = Point(curve, 15, 13)
print("G = " + str(G))

for k in range(0, 6) :
  print(str(k) + " * G = " + str(k * G))
