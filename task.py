import argparse
n = argparse.ArgumentParser(description='process some integers')
n.add_argument('current_number', type=int)
n.add_argument('previous_number', type=int)
b = n.parse_args()
current_num = b.current_number
previous_num = b.previous_number
for i in range(10):
    sum = previous_num + i
    print(f'Current number {i} Previous Number {previous_num} is {sum}')
    previous_num = i