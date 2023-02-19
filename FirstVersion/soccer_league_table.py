import re
import sys


def data_collection():
    """Reading the data and removing regular expression."""

    f = open('football.dat', 'r', encoding = "UTF-8")
    file = f.readlines()
    data = []

    for line in file:
        if line == '\n':
            continue
        data.append(line.strip().split())

    for i in range(1, (len(data))):
        for j in range(len(data[i])):
            if j == 1:
                continue
            n = re.search(r"\d+", data[i][j])
            if n is not None:
                data[i][j] = int(n[0])
    return data


def soccer_league_lable(data):
    """Finding minimum value."""

    diff = sys.maxsize
    team_name_name = ""
    for i in range(1, (len(data))):
        if i == 18:
            continue
        if diff > abs(data[i][6] - data[i][8]):
            diff = abs(data[i][6] - data[i][8])
            team_name = data[i][1]
    return team_name


def main():
    data = data_collection()
    print(soccer_league_lable(data))


if __name__ == "__main__":
    main()
