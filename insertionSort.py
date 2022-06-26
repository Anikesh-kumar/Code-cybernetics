from turtle import clear
inp_list = []
n = int(input("Enter the number limit:"))
for i in range(0, n):
    elm = int(input())
    inp_list.append(elm)


def insertionSort(arr):
     for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
     print ("Sorted array is:",inp_list) 
     
insertionSort(inp_list)

