from itertools import islice
with open('.\\OutData\\log\\col3_1.txt','r') as f:
    while True:
        next_n_lines = list(islice(f, 3))
        print(next_n_lines)
        if not next_n_lines:
            break