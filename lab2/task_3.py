# -*- coding: utf-8 -*-
"""Task_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ozcLwDHF_WXKS2v8LZafUJswIKTg4xrX
"""

txt_input=open('/content/input3.txt','r')
txt_output=open('/content/output3.txt','w')
test=txt_input.readline()
numbers=txt_input.readline().split()

num=[]
for i in numbers:
  i2=int(i)
  num.append(i2)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]

    a1 = merge_sort(l)
    a2 = merge_sort(r)

    return merge(a1, a2)


def merge(a, b):
    merged = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged+=a[i:]
    merged+=b[j:]
    return merged
num1 = merge_sort(num)

for i in num1:
  print(i, end=" ", file=txt_output)
txt_output.close()