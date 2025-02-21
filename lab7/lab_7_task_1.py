# -*- coding: utf-8 -*-
"""Lab 7 Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VIUq6h8wslsU_ZiBGSlwRSwi8PQM-XF-
"""

#task 1
def maxtask(times):
    times.sort(key=lambda x: x[1])
    add_task = []
    final_time = -1

    for task in times:
        start, end = task
        if start >= final_time:
            add_task.append(task)
            final_time = end

    return add_task

with open("/content/input1.txt", "r") as txt_input, open("/content/output1.txt", "w") as txt_output:
  N = int(txt_input.readline())
  time = []
  for i in range(N):
      start, end = map(int, txt_input.readline().split())
      time.append((start, end))

  total_task = maxtask(time)

  print(len(total_task), file = txt_output)
  for i in total_task:
      print(i[0], i[1], file = txt_output)

txt_output.close()