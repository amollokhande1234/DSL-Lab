#Insertion sort 
# def insertionSort(arr,n):
#     i=1
#     for i in range(n):
#         temp = arr[i]
#         j = i-1
#         while(j>=0) and (arr[j]>temp):
#             arr[j+1] = arr[j]
#         arr[j+1] = temp
#     print(arr)
#     print("Top five score are :")
#     for i in range(len(arr)-1,1,-1):
#         print(arr[i])

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = 1
        while arr[j-1]>arr[j] and j>0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1


arr = [88,95,32,45,55,89]
insertion_sort(arr)
print("Insertion Sort : ",arr)
n=6
shellSort(arr,n)
print("Shell Sort :",arr)



# n = int(input("How student :)"))
# arr = []
# i = 0
# for i in range(n):
#     item = float(input("Enter Percentage Marks : "))
#     arr.append(item)
# print("You have entered these Percentage",arr)
# while (True):
#     print("********")
#     print("1. Insertion Sort ")
#     print("2. Shell Sort")
#     print("3. Exit.")
#     choice = int(input("Enter your Choice: "))
#     if choice == 1:
#         print("The sorted score are: ")
#         insertion_sort(arr)
#         print(insertion_sort(arr))
#     elif choice == 2:
#         print(("THe sorted scorer using shell sort are: "))
#         shellSort(arr,n)
#     else:
#         print("Exit.")
#         exit()
