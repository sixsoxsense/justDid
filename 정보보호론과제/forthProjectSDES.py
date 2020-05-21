import SDES

if __name__ == '__main__':
    ciphertexts = []
    f = open(file='text.txt', mode='w',encoding='utf-8')
    plaintext=open("Ciphertext.txt")

    for i in plaintext.readlines():
        ciphertexts.append(int(i[:8],2)) # 암호문을 파일로 읽어올때 주석까지 딸려와서 [:8]로 범위설정 및 str형바이너리를 int로 변환
    for key in range(0b0000000000,0b1111111111):
        for ciphertext in ciphertexts:
            decMSG = SDES.decrypt(key, ciphertext)
            f.write(chr(decMSG))
        f.write(" key: ")
        f.write(str(key))
        f.write("\n")
    f.close()

    '''
    print(bin(726))
    '''