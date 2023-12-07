import csv


class CSVDataManager:
    @staticmethod
    def convert_value_to_int(value):
        try:
            if int(value):
                return int(value)
        except Exception:
            return value

    def get_list_from_csv(self, file_path):
        all_data = []
        with open(file_path, mode="r") as file:
            # reading the CSV file
            csvFile = csv.reader(file)

            # displaying the contents of the CSV file
            for lines in csvFile:
                for _value in lines:
                    all_data.append(self.convert_value_to_int(_value))

        return all_data

