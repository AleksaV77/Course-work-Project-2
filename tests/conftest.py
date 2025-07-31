import os

import pytest

from src.class_api import HH
from src.class_vacancies import VacanciesComparisons

@pytest.fixture
def test_hh_api():
    return HH(url="https://api.hh.ru/vacancies")

@pytest.fixture
def vacancies_hh_api():
    """Получение вакансий"""

    platform = HH(url="https://api.hh.ru/vacancies")
    return platform

@pytest.fixture
def test_user_interaction_word():
    """Фикстура, вакансии 1"""

    return VacanciesComparisons(
        name="Личный водитель",
        url="https://hh.ru/applicant/vacancy_response?vacancyId=123119417",
        salary=500000,
        description="Подача автомобиля в назначенное время.",
    )

@pytest.fixture
def test_user_vacancies():
    """Фикстура, вакансии 2"""

    return VacanciesComparisons(
        name="Тестировщик",
        url="https://api.hh.ru/vacancies/123207731?host=hh.ru",
        salary=100000,
        description="Тестирование REST ARI и веб-интерфейсов",
    )

@pytest.fixture
def test_user_not_url():
    """Фикстура, с не корректной ссылкой"""

    return {
        "name": "Управляющий",
        "url": "/vacancy_response?vacancyId=123119417",
        "salary": 60000, "description": "Подача автомобиля в назначенное время."}

@pytest.fixture
def test_user_not_salary():
    """Фикстура, с отсутствием ЗП"""

    return VacanciesComparisons(
        name="Тестировщик",
        url="https://hh.ru/applicant/vacancy_response?vacancyId=123119417",
        salary=0,
        description="Тестирование REST ARI и веб-интерфейсов",
    )

@pytest.fixture
def test_user_not_description():
    """Фикстура, с отсутствием описания в вакансии"""

    return {
        "name": "Тестировщик",
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=123119417",
        "salary": 80000, "description": ""}

@pytest.fixture
def test_user_interaction_not_word():
    """Фикстура, с отсутствием названия вакансии"""

    return {
        "name": "",
        "url": "https://hh.ru/applicant/vacancy_response?vacancyId=123119417",
        "salary": 60000, "description": "Подача автомобиля в назначенное время."}

@pytest.fixture()
def vacancy_with_negative_salary():
    """Фикстура, с отрицательной ЗП"""

    return {"name": "Садовник", "url": "https://hh.com/job2", "salary": -60000}

@pytest.fixture
def test_file_json(tmp_path):
    """Создание временного JSON-файла"""
    file = tmp_path / "test_vacancies.json"
    yield file
    if file.exists():
        os.remove(file)

@pytest.fixture
def vacancies():
    """Список вакансий"""

    return [
        {"name": "Личный водитель",
         "company": "TechCorp",
         "url": "https://example.com/job1234",
         "salary": {"from": 150000, "to": 170000}},
        {"name": "Управляющий",
         "company": "TechCorp",
         "url": "https://example.com/job1214",
         "salary": {"from": 60000, "to": 90000}},
        {"name": "Менеджер по продажам",
         "company": "TechCorp",
         "url": "https://example.com/job214",
         "salary": {"from": 100000, "to": 120000}}
    ]
