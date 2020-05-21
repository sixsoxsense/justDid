def insert_sort_title(self):
    '''
    삽입정렬 제목순
    '''
    for i in range(1, len(self)):
        while i > 0:
            if self[i - 1][0] > self[i][0]:
                self[i - 1], self[i] = self[i], self[i - 1]
                i -= 1
            else:
                i -= 1
    return self


def insert_sort_year(self):
    '''
    삽입정렬 연도내림차순
    '''
    for i in range(1, len(self)):
        while i > 0:
            if self[i - 1][1] > self[i][1]:
                self[i - 1], self[i] = self[i], self[i - 1]
                i -= 1
            else:
                i -= 1
    return self


def insert_sort_yeardowntitle(self):
    '''
    삽입정렬 연도내림차순정렬후 같은 연도는 제목순
    '''
    for i in range(1, len(self)):
        while i > 0:
            if self[i - 1][1] <= self[i][1]:
                self[i - 1], self[i] = self[i], self[i - 1]
                i -= 1
            else:
                i -= 1
    for i in range(1, len(self)):
        while i > 0:
            if self[i - 1][1] == self[i][1]:
                if self[i - 1][0] > self[i][0]:
                    self[i - 1], self[i] = self[i], self[i - 1]
                    i -= 1
                else:
                    i -= 1
            else:
                break
    return self


def partition(self, low, high):
    pivot = self // 2
    low = self[1]
    high = self[len(self)]
    while low<high:
        continue
    return high


def quick_sort(self, low, high):
    if low >= high:
        return
    pivot = partition(self, low, high)
    quick_sort(self, low, pivot - 1)
    quick_sort(self, pivot + 1, high)

    return self


def quick_sort_title(self):
    """
    제목순 정렬
    """
    if len(self) <= 1:
        return self
    pivot = self[len(self) // 2][0]
    left, equal, right = [], [], []
    for i in range(len(self)):
        if self[i][0] < pivot:
            left.append(self[i])
        elif self[i][0] > pivot:
            right.append(self[i])
        else:
            equal.append(self[i])
    return quick_sort_title(left) + equal + quick_sort_title(right)


def quick_sort_year(self):
    """
    연도오름차순 정렬
    """
    if len(self) <= 1:
        return self
    pivot = self[len(self) // 2][1]
    left, equal, right = [], [], []
    for i in range(len(self)):
        if self[i][1] < pivot:
            left.append(self[i])
        elif self[i][1] > pivot:
            right.append(self[i])
        else:
            equal.append(self[i])
    return quick_sort_year(left) + equal + quick_sort_year(right)


def quick_sort_yeardowntitle(self):
    """
    연도내림차순 정렬후 같은 년도는 제목순
    """
    if len(self) <= 1:
        return self
    pivot = self[len(self) // 2][1]
    left, equal, right = [], [], []
    for i in range(len(self)):
        if self[i][1] > pivot:
            left.append(self[i])
        elif self[i][1] < pivot:
            right.append(self[i])
        else:
            equal.append(self[i])
    return quick_sort_yeardowntitle(left) + quick_sort_title(equal) + quick_sort_yeardowntitle(right)


try:
    '''
    5개 영화이용     제목가나다순,연도별오름차순,연도내림차순정렬후 개봉년도 같으면 가나다순 
    1.제목가나다순
    '''
    print("Insert정렬")
    input_arr = []
    movie5txt = open('5movie.txt', mode='r')
    for line in movie5txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = insert_sort_title(input_arr)
    for i in input_arr:
        print(i)
    print("---------------------------------------")
    input_arr.clear()
    '''
    2.연도별오름차순
    '''
    input_arr = []
    movie5txt = open('5movie.txt', mode='r')
    for line in movie5txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = insert_sort_year(input_arr)
    for i in input_arr:
        print(i)

    print("---------------------------------------")
    input_arr.clear()
    '''
    3.연도내림차순- 개봉년도 같으면 제목 가나다순
    '''
    input_arr = []
    movie5txt = open('5movie.txt', mode='r')
    for line in movie5txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = insert_sort_yeardowntitle(input_arr)
    for i in input_arr:
        print(i)

    print("---------------------------------------")
    input_arr.clear()
    '''
    movie1.txt 파일을 읽고 최신년도 정렬후 같은 연도내에선 제목순 정렬
    '''
    movie1txt = open('movie1.txt', mode='r')
    for line in movie1txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = insert_sort_yeardowntitle(input_arr)  ## 이부분을 구현해야함
    for i in input_arr:
        print(i)

    print("Qucik정렬")
    print("---------------------------------------")
    '''
    5개 영화이용
    1.제목가나다순
    '''
    input_arr.clear()

    input_arr = []
    movie5txt = open('5movie.txt', mode='r')
    for line in movie5txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = quick_sort_title(input_arr)
    for i in input_arr:
        print(i)

    print("---------------------------------------")
    input_arr.clear()
    '''
    2.연도별오름차순
    '''
    input_arr = []
    movie5txt = open('5movie.txt', mode='r')
    for line in movie5txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = quick_sort_year(input_arr)
    for i in input_arr:
        print(i)

    print("---------------------------------------")
    input_arr.clear()
    '''
    3.연도내림차순- 개봉년도 같으면 제목 가나다순
    '''
    input_arr = []
    movie5txt = open('5movie.txt', mode='r')
    for line in movie5txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = quick_sort_yeardowntitle(input_arr)
    for i in input_arr:
        print(i)

    print("---------------------------------------")
    input_arr.clear()
    '''
    movie1.txt 파일을 읽고 최신년도 정렬후 같은 연도내에선 제목순 정렬
    '''
    movie1txt = open('movie1.txt', mode='r')
    for line in movie1txt:
        line = line.rstrip('\n')
        input_arr.append(line.split('\t'))
    input_arr = quick_sort_yeardowntitle(input_arr)  ## 이부분을 구현해야함
    for i in input_arr:
        print(i)
finally:
    movie5txt.close()
