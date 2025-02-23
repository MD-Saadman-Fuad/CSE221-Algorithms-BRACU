# -*- coding: utf-8 -*-
"""Lab 5 Task 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fp2SHOLV1jpG2COQezilfiTTAfV_c_ao
"""

with open("/content/input2.txt", "r") as txt_input, open("/content/output2.txt", "w") as txt_output:
    def lexicographical_order(list1, dicts, stack, str1, str2):
        for x, y in dicts.items():
            if len(y) == 0 and x not in stack and str(x) not in str1:
                stack.append(x)
                str1 += str(x)
                break
        if len(stack) != 0:
            for i in list1:
                if i[0] == stack[0] and i[2] == False:
                    i[2] = True
                    dicts[i[1]].pop(0)
            str2.append(stack.pop(0))
            list1, dicts, stack, str1, str2 = lexicographical_order(list1, dicts, stack, str1, str2)
            return list1, dicts, stack, str1, str2
        else:
            return list1, dicts, stack, str1, str2

    data = txt_input.readline().split(" ")
    data = [int(i) for i in data]
    list1 = []
    list2 = []
    for i in range(0, data[1], 1):
        datum = txt_input.readline().split(" ")
        datum = [int(j) for j in datum]
        datum.append(False)
        list1.append(datum)
        list2.append(datum)

    dicts = {}
    for i in range(1, data[0]+1):
        m = []
        for j in list1:
            if i == j[1]:
                m.append(j[0])
        dicts[i] = m

    stack = []
    stacked = [list1[0][0]]
    str1 = ""
    result = lexicographical_order(list2, dicts, stack, str1, [])
    if len(result[4]) != data[0]:
        txt_output.writelines("Impossible")
    else:
        liss = [str(i) for i in result[4]]
        x = " ".join(liss)
        txt_output.writelines(x)
txt_output.close()