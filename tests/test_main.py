import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import read_csv, calculate_perfomance_report
def test_calculate_perfomance_report():
    test_data = [
        {
            'name': 'Alex Ivanov',
            'position': 'Backend Developer',
            'performance': '4.8',
            'completed_tasks': '45',
            'skills': 'Python, Django, PostgreSQL, Docker',
            'team': 'API',
            'experience_years': '5'
        }
    ,
    {
        'name': 'Maria Petrova',
        'position': 'Frontend Developer',
        'performance': '4.7',
        'completed_tasks': '38',
        'skills': 'React, TypeScript, Redux, CSS',
        'team': 'Web',
        'experience_years': '4'
    },
    {
        'name': 'John Smith',
        'position': 'Backend Developer',
        'performance': '4.9',
        'completed_tasks': '29',
        'skills': 'Python, ML, SQL, Pandas',
        'team': 'API',
        'experience_years': '3'
    }
    ]
    result = calculate_perfomance_report(test_data)
    assert(len(result) == 2), f"Ожидалось 2 должности, но получено {len(result)}"
    print("Тест группироки по должностям успешно пройден!")
    performances = [item['avg_performance'] for item in result]
    assert( performances == sorted(performances, reverse=True)), "Данные не отсортированы по убыванию эффективности"
    print("Тест сортировки по убыванию успешно пройден!")
    backend_item = next(item for item in result if item['position'] == 'Backend Developer')
    frontend_item = next(item for item in result if item['position'] == 'Frontend Developer')
    assert((backend_item['avg_performance'])  == 4.85), f"Ожидалось значение 4.85, но получено {backend_item['avg_performance']}"
    assert((frontend_item['avg_performance']) == 4.7), f"Ожидалось значение 4.7, но получено {backend_item['avg_performance']}"
    print("Тест правильности вычисления среднего успешно пройден!")
def test_performance_report_empty_data():
    result = calculate_perfomance_report([])
    assert(result == []), "При пустых данных должен возвращаться пустой список"
    print("Тест с пустыми данными успешно пройден!")
def test_calculate_perfomance_report_single_developer():
    test_data = [
    {
            'name': 'Maria Petrova',
            'position': 'Frontend Developer',
            'performance': '4.7',
            'completed_tasks': '38',
            'skills': 'React, TypeScript, Redux, CSS',
            'team': 'Web',
            'experience_years': '4'
    }
    ]
    result = calculate_perfomance_report(test_data)
    assert(len(result) == 1), "Должна быть одна должность"
    assert result[0]['position'] == 'Frontend Developer'
    assert result[0]['avg_performance'] == 4.7
    print("Тест с одним разработчиком успешно пройден!")
if __name__ == '__main__':
    test_calculate_perfomance_report()
    test_performance_report_empty_data()
    test_calculate_perfomance_report_single_developer()
