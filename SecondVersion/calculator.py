'''In this I am initializing the classes.'''
import data_extractor
import data_analyzer


class Calculator:
    """Initializing the DataExtractor and DataAnalyzer class."""

    def __init__(self, data_file, col_1, col_2, col_3):
        # This dictionary is used to convert column name to column index.
        col_name_index = {"Dy": 0, "MxT": 1, "MnT": 2, " ": 0, "F": 6, "A": 8}
        extractor_obj = data_extractor.DataExtractor()
        data = extractor_obj.data_read_split(
            data_file, col_name_index[col_1], col_name_index[col_2], col_name_index[col_3])
        analyzer_obj = data_analyzer.DataAnalyzer()
        self.ans = analyzer_obj.min_defference(
            data, col_name_index[col_2], col_name_index[col_3])
