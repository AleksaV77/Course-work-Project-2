import pytest
from src.class_vacancies import VacanciesComparisons

def test_vacancy_init(test_user_interaction_word):
    """Тест на вывод вакансии"""

    assert test_user_interaction_word.name == "Личный водитель"
    assert test_user_interaction_word.url == "https://hh.ru/applicant/vacancy_response?vacancyId=123119417"
    assert test_user_interaction_word.salary == 500000
    assert test_user_interaction_word.description == "Подача автомобиля в назначенное время."

def test_vacancy_not_url(test_user_not_url):
    """Тест на корректную ссылку"""

    with pytest.raises(ValueError, match="Некорректная ссылка на вакансию"):
        VacanciesComparisons(**test_user_not_url)

def test_vacancy_not_salary(test_user_not_salary):
    """Тест на отсутствие ЗП"""

    assert test_user_not_salary.salary == "Зарплата не указана"

def test_vacancy_comparison_salary(test_user_interaction_word, test_user_vacancies):
    """Тест на сравнение вакансий по зарплате."""

    assert test_user_interaction_word.salary > test_user_vacancies.salary

def test_vacancy_not_description(test_user_not_description):
    """Тест на создание вакансии с отсутствием описания."""

    with pytest.raises(ValueError, match="Описание не указано"):
        VacanciesComparisons(**test_user_not_description)

def test_create_vacancy_without_name(test_user_interaction_not_word):
    """Тест на создание вакансии с отсутствием названия."""

    with pytest.raises(ValueError, match="Укажите название вакансии"):
        VacanciesComparisons(**test_user_interaction_not_word)
