import csv


class CSVReader:
    @staticmethod
    def read_csv(filename):
        try:
            with open(filename, newline='') as csvfile:
                return list(csv.DictReader(csvfile, delimiter=';'))
        except Exception as e:
            print(f'Error reading {filename}: {e}')
            return False
