'''In this I am finding minimum value'''
import sys


class DataAnalyzer:
    """Finds minimum value"""

    def min_defference(self, data, col_1, col_2):
        '''hii'''
        diff = sys.maxsize
        # index variable stores the minimum difference row index.
        index = -1
        for i in range(1, (len(data))):
            # Checks if the current row is string then skipping this because in interger values
            # there is some string values which is not required.
            if type(data[i][0]) == type(""):
                continue
            if diff > abs(data[i][col_1] - data[i][col_2]):
                diff = abs(data[i][col_1] - data[i][col_2])
                index = i
        # If this is for weathers data then it's final answer is in 0 column else in 1 column.
        if col_1 == 1:
            return data[index][0]
        return data[index][1]
