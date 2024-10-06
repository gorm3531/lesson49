import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file1:
        while True:
            line = file1.readline().strip()
            all_data.append(line)
            if not line:
                break


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start = datetime.now()

for i in files:
    read_info(i)

end = datetime.now()
time = end - start
print(f'Время работы линейного процесса {time}')
if __name__ == '__main__':
    start2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end2 = datetime.now()
    time2 = end2 - start2
    print(f'Время работы мультипроцесса {time2}')


