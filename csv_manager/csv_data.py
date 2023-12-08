import csv
from typing import List, Any
import logging


class CSVDataManager:
    @staticmethod
    def convert_value_to_int(value):
        try:
            if int(value):
                return int(value)
        except Exception:
            return value

    @staticmethod
    def write_data_to_csv(header: List[str], data: List[dict]) -> None:
        with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)

    def get_data_from_csv(self, file_path) -> List[dict]:
        """
     = [
        {'id': 1,
        'coordinate_X': 0,
        'coordinate_Y': 0,
        'coordinate_Z': 10},
       {'id': 2,
        'coordinate_X': 0,
        'coordinate_Y': 10,
        'coordinate_Z': 10},
    ]
        :param file_path:
        :return:
        """
        all_data = []
        with open(file_path, mode="r") as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                for _value in lines:
                    all_data.append(self.convert_value_to_int(_value))

        return all_data
