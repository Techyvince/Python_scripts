def getNumberList(Num):

    x = open(Num,'r')
    line = x.readline()
    numbers = line.split(',')#split the numbers separated by comma
    numberList = []#holds the integer value 
    for i in numbers:
        numberList.append(int(i))

    return numberList

def getAverage(Num):

    sum = 0#stores the sum of the numbers in the list
    count = 0#keeps the count of numbers in the list
    for i in Num:
        sum = sum + i
        count = count + 1

    average = sum/count#calculate the average
    return average