import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "exemplo.csv", "r", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
