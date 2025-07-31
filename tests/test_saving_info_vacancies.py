import json

import pytest

from src.class_vacancies import VacanciesComparisons
from src.class_saving_info_vacancies import JsonInfoVacancies

def test_search_vacancies(test_file_json, test_user_interaction_word, test_user_vacancies):
    """Тестирование метода на возвращение корректной вакансии по ключевому слову."""

    storage = JsonInfoVacancies(test_file_json)
    storage.add_vacancy([test_user_interaction_word, test_user_vacancies])

    result = storage._get_vacancies({"name": "Тестировщик"})
    assert len(result) == 1
    assert result[0]["name"] == "Тестировщик"

def test_add_vacancies(test_file_json, test_user_interaction_word, test_user_vacancies):
    """Тестирование на количество добавленных вакансий"""

    storage = JsonInfoVacancies(test_file_json)
    storage.add_vacancy([test_user_interaction_word, test_user_vacancies])

    with open(test_file_json, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == test_user_interaction_word.name
    assert data[1]["name"] == test_user_vacancies.name

def test_error_add_vacancy(test_file_json, vacancy_with_negative_salary):
    """Тестирование на исключение ValueError при добавлении вакансии с отрицательной зарплатой"""

    storage = JsonInfoVacancies(test_file_json)
    with pytest.raises(ValueError):
        storage.add_vacancy([VacanciesComparisons(**vacancy_with_negative_salary)])

def test_delete_vacancies(test_file_json, test_user_interaction_word, test_user_vacancies):
    """Тестирование удаления вакансии"""

    storage = JsonInfoVacancies(test_file_json)
    storage.add_vacancy([test_user_interaction_word, test_user_vacancies])

    storage.delete_vacancy({"name": "Личный водитель"})
    data = storage._file_vacancy()

    assert len(data) == 1
    assert data[0]["name"] == "Тестировщик"
