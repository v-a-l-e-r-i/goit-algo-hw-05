import sys
from collections import defaultdict


def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            logs.append(parse_log_line(line.strip()))

    return logs


def parse_log_line(line: str) -> dict:
    data = {
        "date": line.split(" ")[0],
        "time": line.split(" ")[1],
        "level": line.split(" ")[2],
        "message": " ".join(line.split(" ")[3::])
    }
    return data


def filter_logs_by_level(logs: list, level: str) -> list:
    return [f"{item['date']} {item['time']} - {item['message']}" for item in logs if item['level'] == level]


def count_logs_by_level(logs: list) -> dict:
    count_logs = defaultdict(int)
    for item in logs:
        count_logs[item["level"]] += 1
    return dict(count_logs)


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print(f"{key}\t\t | {value}")


def main(path: str, level: str):
    try:
        logs = load_logs(path)
        match level.upper():
            case "INFO" | "ERROR" | "DEBUG" | "WARNING":
                display_log_counts((count_logs_by_level(logs)))
                print(f"Деталі логів для рівня '{level.upper()}':")
                for item in filter_logs_by_level(logs, level.upper()):
                    print(item)
            case _:
                display_log_counts((count_logs_by_level(logs)))
    except FileNotFoundError:
        print("Файл не знайдено!")


path_to_file = sys.argv
main(path_to_file[1], level=path_to_file[-1])
