''' write a program that generates random 4 digits number of 0s and 1s and convert the generate number to base 10'''

import random
random_number_list = []
random_num = ""
num_list = [0,1]
for _ in range(4):
    num = random.choice(num_list)
    random_num += str(num)
    random_number_list.append(num)

base_ten_result = (random_number_list[0] * 2**3) + (random_number_list[1] * 2**2) + (random_number_list[2] * 2**1) + (random_number_list[3] * 2**0)
print(random_num)
print(f"the base ten equivalent is {base_ten_result}")