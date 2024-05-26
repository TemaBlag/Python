#task1
""""
countShumerid = int(input())
countCube = 0
countDelCube = 0
for i in range(1, countShumerid + 1):
    countCube += (2 * i - 1) ** 2
    countDelCube = (2 * i - 1) ** 3 - countCube
    print(countDelCube, end=" ")
"""

#task2
"""
class Queue:
    def __init__(self) -> None:
        self._list = list()

    def push(self, element) -> None:
        self._list.append(element)

    def get(self):
        if len(self._list) == 0:
            pass
        else:
            return self._list.pop(0)

    def isEmpty(self) -> bool:
        return len(self._list) == 0

    def expansion(self) -> None:
        lenQueue = len(self._list)
        if lenQueue == 0:
            pass
        else:
            bufQueue = list()
            for i in range(lenQueue):
                value = self._list.pop(0)
                bufQueue.append(value)
                bufQueue.append(value)
            self._list = bufQueue


queue = Queue()
buf = []
countRequest = int(input())
while countRequest:
    num = input().split()
    if num[0] == "1":
        queue.push(int(num[1]))
    elif num[0] == "2":
        queue.expansion()
    else:
        buf.append(queue.get())
    countRequest -= 1

for i in range(len(buf)):
    print(buf[i])
"""

#task3
"""
nmq = input().split()
n = int(nmq[0])
m = int(nmq[1])
q = int(nmq[2])
labyrinth = []
for i in range(n):
    values = input().split()
    for j, elem in enumerate(values):
        values[j] = int(elem)
    labyrinth.append(values)
result = []
for i in range(q):
    count = 0
    trial = input().split()
    x = int(trial[0]) - 1
    y = int(trial[1]) - 1
    k = int(trial[2])
    for col in range(n):
        if abs(labyrinth[col][y] - labyrinth[x][y]) <= k:
            count += 1
    for row in range(m):
        if abs(labyrinth[x][row] - labyrinth[x][y]) <= k:
            count += 1
    result.append(count - 2)

for k in range(len(result)):
    print(result[k])
"""

#task4
"""
q = int(input())
result = []
while q:
    number = 1
    values = input().split()
    for i in range(int(values[0]), int(values[1]) + 1):
        number *= i
        while number % 10 == 0 and number / 10 != 0:
            number = number // 10
    if number <= 9:
        result.append(number)
    strNum = str(number)
    lenStrNum = len(strNum)
    while lenStrNum != 1:
        sumVal = 0
        for i in range(lenStrNum):
            sumVal += int(strNum[i])
        strNum = str(sumVal)
        lenStrNum = len(strNum)
    result.append(int(strNum[0]))
    q -= 1

for k in range(len(result)):
    print(result[k])
"""
"""
def digit_sum(x):
    if x < 10:
        return x
    return digit_sum(sum(int(digit) for digit in str(x)))

def product_digit_sum(l, r):
    digit_sums = [ digit_sum(x) for x in range(l, r+1)]
    product = 1
    for digit_sum in digit_sums:
        product *= digit_sum
    while product >= 10:
        product = digit_sum(product)
    return product


q = int(input())
result = []
while q:
    values = input().split()
    result.append(product_digit_sum(values[0], values[1]))
for k in range(len(result)):
    print(result[k])
"""





#task5
"""
countHerd = int(input())
numA = 0
numB = 0
numC = 0
numHorses = 0
ugliness = 0
horses = []
buf = []
while countHerd:
    herd = input()
    lenHerd = len(herd)
    a = herd.count("a")
    b = herd.count("b")
    c = herd.count("c")
    numA += a
    numB += b
    numC += c
    horses.append([a, b, c])
    countHerd -= 1
numHorses = numA + numB + numC
ugliness = max(numA, numB, numC) - min(numA, numB, numC)
for p in range(3):
    l = len(horses)
    while l:
        x0 = horses[0][0]
        y0 = horses[0][1]
        z0 = horses[0][2]
        ugliness0 = max(x0, y0, z0) - min(x0, y0, z0)
        numIn = [0]
        for i in range(1, l):
            x = horses[i][0]
            y = horses[i][1]
            z = horses[i][2]
            newUgliness = max(x0 + x, y0 + y, z0 + z) - min(x0 + x, y0 + y, z0 + z)
            if newUgliness <= ugliness0:
                x0 += x
                y0 += y
                z0 += z
                ugliness0 = newUgliness
                numIn.append(i)
        buf.append([x0, y0, z0])
        for i in range(len(numIn)):
            horses.pop(i)
        l = len(horses)
    horses = buf
    buf = []
for i in range(len(horses)):
    a = horses[i][0]
    b = horses[i][1]
    c = horses[i][2]
    count = a + b + c
    ugl = max(a, b, c) - min(a, b, c)
    if ugl < ugliness:
        numHorses = count
        ugliness = ugl
    elif ugl == ugliness and count > numHorses:
        numHorses = count
        ugliness = ugl
print(numHorses)
"""











"""
def max_horse_power(n, herds):
    MAX_UGLINESS = 1000
    MAX_HORSES = 510

    # Инициализация массива dp
    dp = [[[0] * (MAX_HORSES) for _ in range(MAX_HORSES)] for _ in range(MAX_UGLINESS)]

    for herd in herds:
        # Подсчет лошадей каждого типа в табуне
        a = herd.count('a')
        b = herd.count('b')
        c = herd.count('c')

        # Обновление массива dp
        for i in range(MAX_UGLINESS - 1, -1, -1):
            for j in range(MAX_HORSES - a - 1, -1, -1):
                for k in range(MAX_HORSES - b - 1, -1, -1):
                    ugliness = i + max(a - j, 0) + max(b - k, 0) + max(c - (a + b + c - j - k), 0)
                    dp[ugliness][j + a][k + b] = max(dp[ugliness][j + a][k + b], dp[i][j][k] + a + b + c)

    # Поиск ответа на основе массива dp
    for i in range(MAX_UGLINESS):
        max_power = max(dp[i][j][k] for j in range(MAX_HORSES) for k in range(MAX_HORSES))
        if max_power > 0:
            return max_power

    return -1

# Чтение входных данных
n = int(input().strip())
herds = [input().strip() for _ in range(n)]

# Вывод максимальной силы при минимальном уродстве
print(max_horse_power(n, herds))
"""


def sumCount(n):
    i = 1
    sumE = 1
    while i <= n:
        sumE *= 1 + (1.0 / (i * i))
        i += 1
    return sumE


print(sumCount(10000000))
