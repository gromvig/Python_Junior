import argparse as arg
import csv

def read_csv(file_paths: list[str]) -> list[dict]:
    list_dict_data = []
    for file in file_paths:
        try:
            with open(file, "r", encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                list_dict_data.extend(list(reader))
            print(f"Успешно прочитано из {file}")
        except FileNotFoundError:
            print("Ошибка чтения файла - файл не найден")
        except Exception as e:
            print(f"Ошибка при чтении файла {file}{e}")
    return(list_dict_data)

def calculate_perfomance_report(list_dict_data: list[dict])-> list[dict]:
    position_perform = {}
    for  elem in list_dict_data:
        position = elem["position"]
        performance = float(elem["performance"])
        if position not in position_perform:
            position_perform[position] =   {
                'performance': performance,
                'count': 1
            }
        else:
            position_perform[position]['performance'] += performance
            position_perform[position]['count'] += 1
    report = []
    for position in position_perform:
        avg_performance = round(position_perform[position]['performance'] / position_perform[position]['count'],2)
        report.append(
            {
                "position": position,
                "avg_performance": avg_performance,
            }
        )
    report.sort(key = lambda x: x['avg_performance'], reverse = True)
    return report
def output(report: list[dict]):
    print("ОТЧЕТ ЭФФЕКТИВНОСТИ")
    print("=" * 40)
    count = 1
    for elem in report:
        print(f"{count} {elem['position']:<25} | {elem['avg_performance']}")
        count += 1


def main():
    parser = arg.ArgumentParser(description='Анализ эффективности разработчиков')
    parser.add_argument("--files", nargs= '+', required=True, help="Пути к CSV файлам")
    parser.add_argument("--report", required=True, help="Тип отчёта")
    args = parser.parse_args()
    data = read_csv(args.files)
    report = calculate_perfomance_report(data)
    if report:
        output(report)
    else:
        print("Отсутствуют данные для вывода")

if __name__ == "__main__":
    main()
