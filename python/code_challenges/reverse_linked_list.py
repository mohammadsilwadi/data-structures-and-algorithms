list=[1,2,3,4,5,6,-99,100]
def reverseArray(list):
 size=len(list)
 m=int(size/2)
 print(list)
 for i in range(m):
    change=list[i]
    list[i]=list[size-i-1]
    list[size-i-1]=change
    return list
print (reverseArray(list))
