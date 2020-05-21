##HONG KILDONG/YONGIN
import numpy  ##Numpy를 굳이 쓰는이유 : 열계산하기 편하려고


def makeSum(InputlistWords):
    """
    valueList 값임시저장리스트
    charValues 아스키값에서 16진법로 변환된 값이 저장되는 리스트
    verificList sumResult + checkResult 저장 즉 FFFFFFFF 이 되는지 확인하기위해 저장하고 출력되는 리스트
    """
    valueList, charValues, verificList = [], [], []
    for i in InputlistWords:  ##문자를 16진법로 변환 하는 부분
        if ord(i) == 48:  ## 아스키코드'0'의 16진법는 30이기에 리스트에 '3','0'으로 저장됨 따라서 '0' '0' 넣어줌
            charValues += ''.join('0''0')
        else:  ## 그외엔 정상적으로 16진법 변환
            charValues += ''.join(format(ord(i), 'X'))
        if (len(charValues) == 8):
            valueList.append(list(charValues))  ##16진법배열에 2차원형식으로 저장
            del charValues[:]
    strHexlist = valueList[:]  ##list, str형식의 16진법 계산하기 위해서 생성
    intNpArr = numpy.array(valueList[:])  ## 2차행렬 출력위해서 int 형 numpy 배열 생성
    del valueList[:]

    for i in range(len(strHexlist)):
        for j in range(len(strHexlist[i])):
            if strHexlist[i][j].isalpha():
                '''
                아스키코드의의 문자를 10진법으로 바꾼뒤 16진법로 변환해서 저장 
                ex) 'B'=66 - 55  11(16) -> '11'
                '''
                strHexlist[i][j] = ord(strHexlist[i][j]) - 55

    strNpArr = numpy.array(strHexlist[:])  ## 리스트를 배열로 변환
    strNpArr = strNpArr.astype(int)  ## 배열의 형식을 int형으로 바꿔냄 열 계산하기위해서
    sumRow = strNpArr.sum(axis=0)  ## 1차원배열 열끼리 덧셈

    sumIntResult = carryOver16(sumRow[:])  ##sumrow의캐리연산한결과
    checkIntResult = oneComple(sumIntResult[:], valueList)  ##sumResult 1의 보수
    sumHexPrint = ToHexList(sumIntResult[:])  ##sumrow의캐리연산한결과 16진법출력
    checkHexPrint = ToHexList(checkIntResult[:])  ##sumResult 1의 보수 16진법출력
    del valueList

    print("16진법 변환 출력", "\n", intNpArr, '\n', sumHexPrint)
    for i in range(len(sumIntResult)):
        verificList.append(format(sumIntResult[i] + checkIntResult[i], 'X'))

    if verificList.count('F') == 8:  ## F가 8개 있으면 성공
        print("검증결과", "\n", intNpArr, "\n", checkHexPrint, '\n', verificList)
    else:
        print("변환실패")


def ToHexList(List):  ##파라미터리스트값을 16진법으로 변경후 반환하는 함수
    for i in range(len(List)):
        List[i] = format(List[i], 'X')
    return list(List)


def carryOver16(arr):
    '''
    sum 값이 15넘으면 16빼준뒤 앞의배열에 1 더해준다 (캐리연산)
    파이썬은 리스트에서 i가 0일시 i-1 은 -1 리스트의 마지막을 가리킨다.
    그후 i값 1 증가 시켜주고 아닐때도 i값 1 증가시켜줌
    '''
    i = 0
    while True:
        try:
            if arr[i] > 15:
                arr[i] -= 16
                arr[i - 1] += 1
                i += 1
            elif arr[i] <= 15:
                i += 1
        except:  ## i 값이 8이 되어버려서 arr범위 초과하니깐 오류남 그래서 수동으로 0 지정해줌
            i = 0
            pass
        if numpy.all(arr < 16):  ##리스트값들이 16미만인경우 즉 캐리안해줘도 될경우 리스트값 반환
            return list(arr)  ##arr을 나누어서 배열값 하나하나 반환


def oneComple(arr, valuelist):  ##numpy배열 파라미터대입 1의 보수
    for i in range(len(arr)):
        arr[i] = 15 - arr[i]
        valuelist.append(arr[i])
    return list(valuelist)

def printInputWords(list):
    for i in range(0,len(list),4):
        print(list[i:i+4])

if __name__ == '__main__':
    words = str(input("이름과주소를입력하세요"))  ## 문자입력
    words = words.replace("", "")  ##공백제거
    result_word = ""
    for word in words:  ##특수문자제거
        if word.isalnum():
            result_word += word

    InputlistWords = list(result_word)  ## 입력받은 문자 나눠서 저장
    list_lenth = len(InputlistWords)  ##입력문자들 길이

    if list_lenth % 4 == 0:  ## 나머지 0바이트로 딱떨어질시
        print("입력값")
        printInputWords(InputlistWords)
        makeSum(InputlistWords)

    elif list_lenth % 4 == 1:  ##나머지 1바이트로 떨어질시
        for i in range(3):
            InputlistWords.append('0')
        print("입력값")
        printInputWords(InputlistWords)

        makeSum(InputlistWords)

    elif list_lenth % 4 == 2:  ##나머지 2바이트로 떨어질시
        for i in range(2):
            InputlistWords.append('0')
        print("입력값")
        printInputWords(InputlistWords)

        makeSum(InputlistWords)

    elif list_lenth % 4 == 3:  ##나머지 3바이트로 떨어질시
        for i in range(1):
            InputlistWords.append('0')
        print("입력값")
        printInputWords(InputlistWords)
        makeSum(InputlistWords)

    else:  ## ???????????????????????
        print('오류')