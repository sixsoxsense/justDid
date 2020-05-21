# --*-- encoding: utf-8 --*--
'''
DES 알고리즘에 대한 분석 및 암복호 코드 제출
- DES 알고리즘에 대한 구조, 특징 분석 레포트 작성
- DES 알고리즘 구현 및 암복호 결과 제출
- Key : 난수로 8바이트(64비트) 생성
- Plaintext : 본인의 이름 영문 8byte 입력
- Output : Ciphertext 출력
- 다시 이를 복호화한 결과 출력
'''
a=[34, 67, 75, 216, 30, 21, 114, 114, 216, 214, 190, 102, 190, 234, 216, 240, 214, 67, 30, 216, 75, 214, 106, 21, 114, 216, 34, 67, 75, 216, 106, 234, 34]
b=[34, 107, 203, 245, 155, 121, 26, 26, 245, 251, 87, 174, 87, 199, 245, 240, 251, 107, 155, 245, 203, 251, 42, 121, 26, 245, 34, 107, 203, 245, 42, 199, 34]
for i in a:
    print(oct(i))
for i in b:
    print(oct(i))