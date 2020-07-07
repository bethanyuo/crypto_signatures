from pycoin.ecdsa import CurveFp, Point
from nummaster.basic import sqrtmod

def compress_key_pair(key_pair):
  return (key_pair.x(), key_pair.y() % 2)

def uncompress_key(curve, compressed_key):
  x, is_odd = compressed_key
  p, a, b = curve.p(), curve.a(), curve.b()
  y = sqrtmod(pow(x, 3, p) + a * x + b, p)
  if bool(is_odd) == bool(y & 1):
    return (x, y)
  return (x, p - y)


curve = CurveFp(17, 0, 7)
p = Point(curve, 10, 15)
print(f"original key = {p}")
compressed_p = compress_key_pair(p)
print(f"compressed = {compressed_p}")
restored_p = uncompress_key(curve, compressed_p)
print(f"uncompressed = {restored_p}")
