import pandas as pd


def read_data(data_file):
    """
        Beolvassuk az adatokat a CSV fájból.

        :param data_file: CSV fájl
        :return: DataFrame
    """
    data = pd.read_csv(data_file, sep=";", decimal=",", engine="python", encoding="UTF-8", skiprows=[0])

    return data
