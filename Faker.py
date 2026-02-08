import csv
import argparse
from faker import Faker

def main():
    parser = argparse.ArgumentParser(
        description="Генерируем N фейковых имён и фамилий на английском и сохраняем в CSV"
    )
    parser.add_argument('--n', type=int, default=600, help='Количество записей (имен и фамилий)')
    parser.add_argument('--filename', default='data.csv', help='Выходной CSV файл')
    parser.add_argument('--locale', default='en_US', help='Локаль Faker (например, en_US)')
    args = parser.parse_args()

    fake = Faker(args.locale)

    with open(args.filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'lastname'])
        writer.writeheader()
        for _ in range(args.n):
            writer.writerow({'name': fake.first_name(), 'lastname': fake.last_name()})

    print(f"Файл создан: {args.filename} (записано {args.n} пар)")

if __name__ == "__main__":
    main()