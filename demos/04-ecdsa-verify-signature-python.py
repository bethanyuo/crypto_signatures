from pycoin.ecdsa import generator_secp256k1, sign, verify
import hashlib

def keccak_hash(msg) :
  hash_bytes = hashlib.sha3_256(msg.encode("utf8")).digest()
  return int.from_bytes(hash_bytes, byteorder="big")

msg = "some message"
msg_hash = keccak_hash(msg)
private_key = 9999999999999999999999999999999999999999999
signature = sign(generator_secp256k1, private_key, msg_hash)
print("signature = " + str(signature))


public_key = (generator_secp256k1 * private_key).pair()
print("public key: " + str(public_key))

valid = verify(generator_secp256k1,
  public_key, msg_hash, signature)
print("Signature valid? " + str(valid))

tampered_msg_hash = keccak_hash("tampered msg")
valid = verify(generator_secp256k1, public_key,
  tampered_msg_hash, signature)
print("Signature (tampered msg) valid? " + str(valid))
