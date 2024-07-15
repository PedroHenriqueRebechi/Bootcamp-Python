import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "exemplo.csv", "w", newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'nome'])
    writer.writerow(['01', 'Pedro'])
    writer.writerow(['02', 'Maria'])