
import pandas as pd
import re
import numpy as np

def binaryToDecimal(binary):

    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


def decimalToBinary(n):
    return bin(n).replace("0b", "")


reg = pd.read_csv('register.csv')
X = reg.iloc[:, 0].values
print(X, type(X))

instruction = "ADD R1,R7,R11"
instr = re.split('[, \n ]', instruction)
print(instr)

# idx = instr[2]
# print(idx)
# val = reg.loc[idx, :].values
# print(val)

if instr[0] == 'ADD':
  idx = np.where(X==instr[2])
  val = reg.loc[idx].values
  print("Val:",val)

  r7 = np.delete(val, 0)
  print("R7:",r7)

  res7 = int("".join(map(str, r7)))
  print(res7, type(res7))

  padded_num = str(res7).rjust(32, '0')
  print(padded_num)

  R7 = binaryToDecimal(res7)
  print(R7)


  idx2 = np.where(X==instr[3])
  val2 = reg.loc[idx2].values
  print("Val2:",val2)

  r11 = np.delete(val2, 0)
  print("R11",r11)

  res11 = int("".join(map(str, r11)))
  print(res11, type(res11))

  padded_num11 = str(res11).rjust(32, '0')
  print(padded_num11)

  R11 = binaryToDecimal(res11)
  print(R11)

  ans = R7 + R11
  ansBin = decimalToBinary(ans)
  padded_num_ans = str(ansBin).rjust(25, '0')
  l = []
  j=0
  for i in range (0,5):
    l.append(padded_num_ans[j:j+5])
    j=j+5
  for count, ele in enumerate(l):
    reg.loc[reg['R'] == 'R1',str(count+1)] = int(ele)
    reg.to_csv('register', index=False)
reg


  # add and update in regsiter file
