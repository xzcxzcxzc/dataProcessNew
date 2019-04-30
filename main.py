import xlrd
import numpy as np


#读取一行数据
def readDataRow(tableName,rowNumber):
    #读取数据
    # data = xlrd.open_workbook('33_3m.xlsx')  #读取数据
    data = xlrd.open_workbook(tableName)  #读取数据

    table = data.sheets()[0]              #打开第一张表

    # print("rowvslue")
    # print(table.row_values(rowNumber))

    return table.row_values(rowNumber)

#读取所有数据
def readData(tableName):
    #读取数据
    # data = xlrd.open_workbook('33_3m.xlsx')  #读取数据
    data = xlrd.open_workbook(tableName)  #读取数据

    table = data.sheets()[0]              #打开第一张表

    nrows = table.nrows       #获取总行数
    ncols = table.ncols       #获取总列数

    return table,nrows,ncols

#求平均值
def average(data):
    #求和
    sum = 0
    for num in range(len(data)):
        sum = sum + data[num]

    #求平均数
    average = sum/len(data)

    return average

#每行减平均数
def minusAverage(data,nrows,ncols):

    #声明numpy的数组
    data_numpy=np.zeros((nrows,ncols))

    #给numpy赋值
    for num in range(nrows):
        #取行
        tempData = data.row_values(num)

        #减去平均数
        tempData[:] = [x - averageOfData for x in tempData]

        #复制给numpy
        data_numpy[num,:] = tempData[:]

    return data_numpy

#将数值变成0和1
def dataNprmalization(data_numpy):
    numberOfRow = data_numpy.shape[0] #行数
    numberOfCol = data_numpy.shape[1] #列数

    for numRow in range(numberOfRow):
        for numCol in range(numberOfCol):
            #判断
            if data_numpy[numRow,numCol]>0:
                data_numpy[numRow,numCol] = 1
            else:
                data_numpy[numRow,numCol] = 0

    return data_numpy




#---------读取数据---------
tableName = '33_3m.xlsx'
rowNumber = 0

dataRow = readDataRow(tableName,rowNumber)

# print("data")
# print(dataRow)

#---------求平均---------
averageOfData = average(dataRow)

print("averageOfData")
print(averageOfData)

#---------数据处理---------
data,nrows,ncols = readData(tableName) #data=整个数据表格 nrows=数据行数,ncols=数据列数

#每一行减去平均值
data_numpy = minusAverage(data,nrows,ncols)

print("data_numpy")
print(data_numpy)

#将数值变成0和1
dataNorm = dataNprmalization(data_numpy)

print("dataNorm")
print(dataNorm)

#---------数据保存---------
np.savetxt('33_3m_MinusAverag',data_numpy)
np.savetxt('33_3m_Norm',dataNorm)






