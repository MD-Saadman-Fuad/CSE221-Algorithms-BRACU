# -*- coding: utf-8 -*-
"""Task_2.A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14-d4pA7LahCSn2JelJtF4aQlFs-erjwO
"""

#Task 2.A

def mergeSort(array):
    if len(array) > 1:

        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

txt_input=open('/content/input2a.txt', 'r')
txt_output=open('/content/output2a.txt', 'w')
test_case1 = (txt_input.readline()).split()
numbers1 = (txt_input.readline()).split()
test_case2 = (txt_input.readline()).split()
numbers2 = (txt_input.readline()).split()

number = numbers1 + numbers2

print(number)
list3=[]
for i in number:
  i2 = int(i)
  list3.append(i2)

array = list3
print(list3)
mergeSort(array)
for i in array:
  print(i, end=" ", file = txt_output)
txt_output.close()