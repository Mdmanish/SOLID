import re
import sys

def data_collection():
    f = open('weather.dat', 'r')
    file = f.readlines()
    data = []

    for line in file:
        if line =='\n':
            continue
        data.append(line.strip().split())

    for i in range(1, (len(data))):
        for j in range(len(data[i])):
            n = re.search(r"\d+", data[i][j])
            if n != None:
                data[i][j] = int(n[0])
    return data

def smallest_temperature_spread(data):
    smallest_temp_spread = sys.maxsize
    day_number = -1
    for line in data[1:]:
        if smallest_temp_spread > line[1] - line[2]:
            smallest_temp_spread = line[1] - line[2]
            day_number = line[0]
    return day_number, smallest_temp_spread


def main():
    data = data_collection()
    print(type(data[2][1]))
    print(smallest_temperature_spread(data))

if __name__ == "__main__":
    main()
