 
import copy
b_1 = [12, 5, 'wer']
b_2 = copy.copy(b_1)

print(id(b_1))
print(id(b_2))
print(b_1 == b_2)
print(b_1 is b_2)
