### Simple DES
import itertools

import binary as binary

P10_index = [3,5,2,7,4,10,1,9,8,6]
P8_index = [6,3,7,4,8,5,10,9]

def listShift(lst,direction,n):
    vlist = lst
    if direction =='L':
        for i in range(0,n):
            tmp = vlist[0]
            for j in range(0,len(vlist)-1):
                vlist[j] = vlist[j+1]
            vlist[len(vlist)-1] = tmp
    return vlist

def textTo8BitBlockArr(inText):
    blockArr = []
    text = text8bitPadding(inText)
    textLen = len(text)
    for i in range(0,int(textLen/8)):
        blockArr.append(text[(i*8):((i+1)*8)])
    return blockArr

def text8bitPadding(inText):
    inTextLen = len(inText)
    inTextLenMod = inTextLen%8
    paddedText = inText
    if inTextLenMod != 0:
        addPadLen = 8-inTextLenMod
        for i in range(0,addPadLen):
            paddedText += '0'
    return paddedText

def getCryptoText(EncOrDec,encryptMode,mode,blockArr,key):
    decryptBlockArr = []
    if encryptMode=='S-DES':
        if mode=='ECB':
            for i in range(0,len(blockArr)):
                decryptBlockArr.append(sDesCrypt(EncOrDec,blockArr[i],key))
    return decryptBlockArr

def sDesCrypt(EncOrDec,text,key):
    getKey = getK1K2(key)
    Key1 = getKey['K1']
    Key2 = getKey['K2']
    print(Key1)
    print(Key2)
    return 0

def getK1K2(key):
    p10Key = []
    if(len(key)==len(P10_index)):
        for i in P10_index:
            p10Key.append(key[i-1])
    L_KeyArr = p10Key[0:5]
    R_KeyArr = p10Key[5:10]
    LS1Key = listShift(L_KeyArr,'L',1)+listShift(R_KeyArr,'L',1)
    K1 = []
    for i in P8_index:
        K1.append(LS1Key[i-1])
    LS2Key = listShift(L_KeyArr,'L',2)+listShift(R_KeyArr,'L',2)
    K2 = []
    for i in P8_index:
        K2.append(LS2Key[i-1])
    retKey = {'K1':K1, 'K2':K2}
    return retKey


# Text To Binary Block
cipherText="110010000100100110100111011111000000010010110000010101110101011101111100110111000000101000011001000010101011110001111100000010001101110001001001000001000111110010100111110111001111101010110000010101110111110011001000010010011010011101111100111110101011110011001000"
cipherBlockArr = textTo8BitBlockArr(cipherText)

# Make Test Key
key="1010110101"

# Decrypt (ECB)
decryptBlockArr = getCryptoText('D','S-DES','ECB',cipherBlockArr,key)
