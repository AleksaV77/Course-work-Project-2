from src.user_interactions import sort_vacancies_salary


def test_sort_vacancies(vacancies, capsys):
    sort_vacancies_salary(vacancies, 2)

    sorted_vacancies = capsys.readouterr()

    top_vacancies = (
        "Топ 2 вакансий по зарплате:\n"
        "Вакансия: Личный водитель\n"
        "Зарплата: {'from': 150000, 'to': 170000}\n\n"
        "Вакансия: Менеджер по продажам\n"
        "Зарплата: {'from': 100000, 'to': 120000}"
    ).strip()

    assert sorted_vacancies.out.strip() == top_vacancies
