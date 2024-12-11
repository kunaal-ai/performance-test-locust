import csv
import random
import os


class CsvRead:

    def __init__(self, file):
        self.file_path = os.path.join(os.path.dirname(__file__), file)

    def read(self):
        try:
            with open(self.file_path, encoding="utf-8-sig") as file:
                reader = csv.DictReader(file)
                return random.choice(list(reader))
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found at {self.file_path}")
        except Exception as e:
            raise Exception(f"Error reading the file: {e}")
