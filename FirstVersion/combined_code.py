import re
import sys

def data_read_split(dat_data):
    f = open(dat_data, 'r')
    file = f.readlines()
    data = []

    for line in file:
        if line =='\n':
            continue
        data.append(line.strip().split())
    return data


def weather_data_regex(data):
    for i in range(1, (len(data))):
        for j in range(len(data[i])):
            n = re.search(r"\d+", data[i][j])
            if n != None:
                data[i][j] = int(n[0])
    return data


def football_data_regex(data):
    for i in range(1, (len(data))):
        for j in range(len(data[i])):
            if j == 1:
                continue
            n = re.search(r"\d+", data[i][j])
            if n != None:
                data[i][j] = int(n[0])
    return data


def smallest_temperature_spread(data):
    smallest_temp_spread = sys.maxsize
    day_number = -1
    for line in data[1:]:
        if smallest_temp_spread > (int(line[1]) - int(line[2])):
            smallest_temp_spread = int(line[1]) - int(line[2])
            day_number = line[0]
    return day_number, smallest_temp_spread


def soccer_league_lable(data):
    diff = sys.maxsize
    team_name = ""
    for i in range(1, (len(data))):
        if i == 18:
            continue
        if diff > abs(data[i][6] - data[i][8]):
            diff = abs(data[i][6] - data[i][8])
            team_name = data[i][1]
    return team_name


def main():
    data = data_read_split('weather.dat')
    data = weather_data_regex(data)
    print(smallest_temperature_spread(data))

    data = data_read_split('football.dat')
    data = football_data_regex(data)
    print(soccer_league_lable(data))

if __name__ == "__main__":
    main()
