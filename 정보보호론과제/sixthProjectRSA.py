'''
RSA 암호문 해독 및 개인키 찾기

아래 내용과 같이 RSA 공개키 암호를 이용하여 암호문을 생성하였을 때 각각 사용된 개인키를 찾으시오.

각 방식에서 소수(Prime number) p와 q를 각각 11비트/12비트/13비트로 랜덤 생성하였음
동일한 평문을 사용하여 암호문을 생성하였음
Ciphertext 목록내 하나의 숫자는 하나의 문자를 의미함
각각의 암호문에 사용된 개인키를 찾아보고 이를 제시하시오(각각의 암호문에 각기 다른 공개키가 사용됨)
복호화하였을 경우 평문을 제시하시오 (복호화 결과 3개의 평문은 동일함)
각 암호문에 대해서 복호화 하는데 걸리는 시간을 제시하고, 만일 소수가 256비트라면 어느 정도 시간이 걸릴지 추정하여 제시하시오.
제출 방법 : 레포트(PDF), 소스코드 원본, 실행결과 제출
'''
from rsa import key
import time

plaintext = []
'''
p,q=  2027 1201
d=  2050883
'''
keySize1 = 11  # bits
publicKeyN1 = 2434427
publicKeyE1 = 1547
Ciphertext1 = [1723694, 2004664, 531108, 363271, 390408, 321608, 531108, 2325663, 390408, 531108, 83863, 390408,
               1905221,
               531108, 1965593, 177469, 2226439, 1210295, 531108, 1905221, 390408, 2325663, 177469, 363271, 291419,
               531108, 363271,
               390408, 321608, 531108, 1965593, 1272075, 2226439, 2226439, 531108, 1051348, 177469, 1247436, 1863310,
               531108,
               1905221, 390408, 531108, 1020793, 321608, 83863, 531108, 1905221, 390408, 2237877, 390408, 1020793,
               1020793, 390408,
               1965593, 167159]
privateKeyd1 = 0

'''
p,q=  3037 2143
d=  3810683
'''
keySize2 = 12  # bits
publicKeyN2 = 6508291
publicKeyE2 = 2867
Ciphertext2 = [1931324, 4591279, 2299455, 1900788, 4744716, 5353531, 2299455, 3099542, 4744716, 2299455, 6163283,
               4744716,
               4980818, 2299455, 2120635, 5691940, 3295860, 1517828, 2299455, 4980818, 4744716, 3099542, 5691940,
               1900788, 2716125,
               2299455, 1900788, 4744716, 5353531, 2299455, 2120635, 6027744, 3295860, 3295860, 2299455, 561287,
               5691940, 877777,
               4440192, 2299455, 4980818, 4744716, 2299455, 6485886, 5353531, 6163283, 2299455, 4980818, 4744716,
               5889378, 4744716,
               6485886, 6485886, 4744716, 2120635, 4100266]
privateKeyd2 = 0

'''
p,q=  7411 7789
d=  27961361
'''
keySize3 = 13  # bits
publicKeyN3 = 57724279
publicKeyE3 = 7721
Ciphertext3 = [5239498, 38590467, 12489631, 14786303, 8046416, 49186583, 12489631, 44080885, 8046416, 12489631,
               51573239,
               8046416, 38401634, 12489631, 40574611, 44665113, 19587051, 37020265, 12489631, 38401634, 8046416,
               44080885, 44665113,
               14786303, 25621157, 12489631, 14786303, 8046416, 49186583, 12489631, 40574611, 51838054, 19587051,
               19587051, 12489631,
               36264541, 44665113, 9316447, 28686759, 12489631, 38401634, 8046416, 12489631, 49414523, 49186583,
               51573239, 12489631,
               38401634, 8046416, 4264766, 8046416, 49414523, 49414523, 8046416, 40574611, 36215115]
privateKeyd3 = 0


def decrypt_local(ciphertexts, d, n):
    textarr = ""
    for ciphertext in ciphertexts:
        textarr+=chr(pow(ciphertext, d, n))
    return textarr


if __name__ == '__main__':
    '''
    11비트일때
    '''
    while True:
        p = key.find_p_q(11)[0]
        q = key.find_p_q(11)[1]
        if p * q == publicKeyN1:
            print("p,q= ", p, q)
            privateKeyd1 = key.calculate_keys_custom_exponent(p, q, publicKeyE1)[1]
            break
    print("d= ", privateKeyd1)

    start1 = time.time()
    plaintext = decrypt_local(Ciphertext1, privateKeyd1, publicKeyN1)
    print(plaintext)
    print("키 11비트 :", time.time() - start1)

    '''
    12비트일때
    '''

    while True:
        p = key.find_p_q(12)[0]
        q = key.find_p_q(12)[1]
        if p * q == publicKeyN2:
            print("p,q= ", p, q)
            privateKeyd2 = key.calculate_keys_custom_exponent(p, q, publicKeyE2)[1]
            break
    print("d= ", privateKeyd2)
    start2 = time.time()
    decrypt_local(Ciphertext2, privateKeyd2, publicKeyN2)
    print("키 12비트 :", time.time() - start2)

    '''
    13비트일때
    '''

    while True:
        p = key.find_p_q(13)[0]
        q = key.find_p_q(13)[1]
        if p * q == publicKeyN3:
            print("p,q= ", p, q)
            privateKeyd3 = key.calculate_keys_custom_exponent(p, q, publicKeyE3)[1]
            break
    print("d= ", privateKeyd3)
    start3 = time.time()
    decrypt_local(Ciphertext3, privateKeyd3, publicKeyN3)
    print("키 13비트 :", time.time() - start3)
