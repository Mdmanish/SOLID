'''In this I am reading and cleaning the data.'''
import re


class DataExtractor:
    """Reading .dat file and after cleanning the data, storing them in a list."""

    def data_read_split(self, dat_data, col_1, col_2, col_3):
        '''Reading the data'''
        file_object = open(dat_data, 'r', encoding = "UTF-8")
        file = file_object.readlines()
        data = []
        for line in file:
            if line == '\n':
                continue
            data.append(line.strip().split())

        # Removing regular expression from the string values and converting them into int.
        for i in range(1, (len(data))):
            for j in (col_1, col_2, col_3):
                if j >= len(data[i]):
                    continue
                val = re.search(r"\d+", data[i][j])
                if val is not None:
                    data[i][j] = int(val[0])
        return data
