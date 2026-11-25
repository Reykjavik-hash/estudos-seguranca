"""
Implementação didática de TOTP (RFC 6238).
Uso: apenas para estudo.

ATENÇÃO: o segredo abaixo é PÚBLICO e serve só para teste.
Nunca use este segredo em uma conta real.
"""
import hmac
import hashlib
import struct
import time
import base64


def totp(segredo_b32, passo=30, digitos=6):
    chave = base64.b32decode(segredo_b32.upper())
    contador = int(time.time() // passo)        # muda a cada 30 segundos
    msg = struct.pack(">Q", contador)
    h = hmac.new(chave, msg, hashlib.sha1).digest()
    pos = h[-1] & 0x0F                          # "dynamic truncation"
    num = struct.unpack(">I", h[pos:pos + 4])[0] & 0x7FFFFFFF
    return str(num % 10 ** digitos).zfill(digitos)


if __name__ == "__main__":
    SEGREDO_DE_TESTE = "JBSWY3DPEHPK3PXP"
    print(totp(SEGREDO_DE_TESTE))
