
list=[1,2,3,4,5,6]
def insertShiftArray(list,num):
 middle=int(len(list)/2)
 list=list[0:middle]+[num]+list[middle:]
 return list
print (insertShiftArray(list,12))
