# chain code example
# Author: Junchi Wang
# Date: 2024/3/9
# Version: v1.0

import numpy as np

'''
chain code definition:
   1
   |
2-----0
   |
   3
'''

# chain code of first shape 
chain_code_1 = np.array([0,3,0,3,2,2,2,1,0,1])
'''
  _
_| |_
|___|

'''

# compute the difference of chain code(angle)
diff = np.zeros(len(chain_code_1))

for i in range(1, len(chain_code_1)):
    diff[i] = (chain_code_1[i] - chain_code_1[i-1]) % 4

diff[0] = (chain_code_1[0] - chain_code_1[-1]) % 4

# make the magnitude of diff minimal(sort)
min_list = diff
min_value = 0
for i in range(len(diff)):
    min_value += diff[i]*np.power(10, len(diff)-i-1)

for i in range(len(diff)):
    temp = np.roll(diff, i)
    temp_value = 0
    for j in range(len(diff)):
        temp_value += temp[j]*np.power(10, len(diff)-j-1)
    if temp_value < min_value:
        min_list = temp
        min_value = temp_value


# chain code of second shape
chain_code_2 = np.array([0,0,0,0,0,3,3,2,2,3,3,2,1,1,2,2,1,1])
'''
_______
|     |
|__ __|
  | |
  |_|

'''
# compute the difference of chain code(angle)
diff1 = np.zeros(len(chain_code_2))

for i in range(1, len(chain_code_2)):
    diff1[i] = (chain_code_2[i] - chain_code_2[i-1]) % 4

diff1[0] = (chain_code_2[0] - chain_code_2[-1]) % 4


# make the magnitude of diff minimal(sort)
min_list1 = diff1
min_value1 = 0

for i in range(len(diff1)):
    min_value1 += diff1[i]*np.power(10, len(diff1)-i-1)

for i in range(len(diff1)):
    temp = np.roll(diff1, i)
    temp_value = 0
    for j in range(len(diff1)):
        temp_value += temp[j]*np.power(10, len(diff1)-j-1)
    if temp_value < min_value1:
        min_list1 = temp
        min_value1 = temp_value

# ignore the length of the edge and compare the angle
for i in range(len(min_list)-1,-1,-1):
    if min_list[i] == 0:
        min_list = np.delete(min_list, i)

for i in range(len(min_list1)-1,-1,-1):
    if min_list1[i] == 0:
        min_list1 = np.delete(min_list1, i)

print(min_list, min_list1)

if len(min_list) == len(min_list1) and (min_list == min_list1).all():
    print("same shape")
else:
    print("different shape")
