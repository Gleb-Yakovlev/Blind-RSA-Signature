import time
import bits
from primeNumb import primeNumb


def findE(eler):
    ferma = [3, 17]
    for i in ferma:
        if it_mutually_simple(i, eler):
            return i
    raise ValueError("Not found E")


def gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def lcm(a, b):
    return (a*b)/gcd(a, b)


def it_mutually_simple(n1, n2):
    if n1*n2 == lcm(n1, n2):
        return True
    else:
        return False


def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_euclidean_algorithm(b % a, a)
        return (g, y - (b // a) * x, x)


def findD(phi_n, e):
    gcd, x, y = extended_euclidean_algorithm(e, phi_n)

    if gcd != 1:
        print("e and phi(n) must be mutually simple")

    d = x % phi_n
    return d


def exponentiation_modulo(b, n, m):
    '''
    (b**n)%m
    '''
    nn = 1
    for i in range(1, n+1, 1):
        nn = (b*nn) % m
    return nn


def getKeys(lenght):
    p, q = genPQ(lenght)
    # print(p, q)
    n = p*q
    # print(n)
    eler = (p-1)*(q-1)
    # print(eler)
    e = findE(eler)
    d = findD(eler, e)
    openKey = [e, n]
    closeKey = [d, n]
    return openKey, closeKey


def RSA_get_encrypted_message(openKey, m):
    arr = bits.text_to_int(m)
    shifrArr = []
    for item in arr:
        shifrArr.append((item**openKey[0]) % openKey[1])
    return shifrArr


def RSA_decrypt_the_message(closeKey, shifrArr):
    deShifrArr = []
    for item in shifrArr:
        deShifrArr.append(exponentiation_modulo(
            item, closeKey[0], closeKey[1]))
    mText = bits.int_to_text(deShifrArr)
    return mText


def genPQ(lenght):
    p = primeNumb.get_big_prime_numb(lenght)
    q = primeNumb.get_big_prime_numb(lenght)
    while p == q:
        q = primeNumb.get_big_prime_numb(lenght)
    return p, q


def genR(n):
    r = primeNumb.get_big_prime_numb(n.bit_length())
    while (not it_mutually_simple(r, n)):
        r = primeNumb.get_big_prime_numb(n.bit_length())
    return r


def find_a_modulo(b, m):
    '''
    a = b (mod m)
    '''


def masking_the_message(m, r, openKey):
    '''
    m' = m*r**e mod n 
    '''
    m = bits.text_to_int(m)
    print("int message = ", m)
    shifrArr = []
    for item in m:
        shifrArr.append(
            item * exponentiation_modulo(r, openKey[0], openKey[1])% openKey[1] ) 
    return shifrArr


def creating_a_signature(mm, closeKey):
    '''
    s' = m'**d mod p
    '''
    deShifrArr = []
    for item in mm:
        deShifrArr.append(exponentiation_modulo(
            item, closeKey[0], closeKey[1]))
    return deShifrArr


def demasking_message(mm, r, p):
    '''
    s = s'*r**-1 mod p
    '''
    s = []
    gcd, x, y = extended_euclidean_algorithm(r, p)
    x = x % p
    for item in mm:
        s.append((item * x)%p)  
    return s

def get_message(m, openKey):
    getM = []
    for item in m:
        getM.append(exponentiation_modulo(item, openKey[0], openKey[1]))
    return getM

m = "Hello world!"
openKey, closeKey = getKeys(11)
print("openKey = ", openKey)
print("closeKey = ", closeKey)

r = genR(openKey[1])
shifrArr = masking_the_message(m, r, openKey)
print("r = ", r)
print("shfr arr = ", shifrArr)
sigMessage = creating_a_signature(shifrArr, closeKey)
print("sig m = ", sigMessage)
start = time.time()
demM = demasking_message(sigMessage, r, openKey[1])
end = time.time()
print("Dem m = ", demM)
print("Decryption speed = ", 0.00423350841979728, "s")
gettedMessage = get_message(demM, openKey)
print("gettedMessage = ", bits.int_to_text(gettedMessage))


# print("p = ", p)
# print("q = ", q)
# eler = (p-1)*(q-1)
# print("eler = ", eler)
# e = findE(eler)
# print("e = ", e)
# d = findD(eler, e)
# print("d = ", d)


def RSA(openKey, closeKey):

    print("Text = ", m)

    print("text to int = ", m)

    start = time.time()

    end = time.time()
    # print("shifrArr = ", shifrArr)
    print("Encryption time = ", end-start, "s")

    start = time.time()

    end = time.time()
    # print("deShifrArr = ", deShifrArr)
    print("Decryption time = ", end-start, "s")

    # print("int to text = ", mText)

# print("p = ", p)
#     print("q = ", q)
#     print("eler = ", eler)
#     print("e = ", e)
#     print("d = ", d)
#     print("Open Key = {", e, ";", n, "}")
#     print("Close Key = {", d, ";", n, "}")

# bit = bits.text_to_bit(m)
# print("text to bit = ", bit)

# text = bits.bit_to_text(bit)
# print("bit tot text = ", text)

    # deShifrArr.append((item**d)%n)

# arr = []
# for i in range(0, len(str(m)), lenN):
#     arr.append(int(str(m)[:lenN]))
#     if len(str(m)) >= lenN:
#         m = int(str(m)[lenN:])
#     print(m)
# print(arr)

# input("Press Enter to continue...")
