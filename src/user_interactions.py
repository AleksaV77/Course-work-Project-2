from src.class_api import Parser, HH
from src.class_vacancies import VacanciesComparisons
from src.class_saving_info_vacancies import JsonInfoVacancies

def sort_vacancies_salary(vacancies, n):
    """ Сортировка N вакансий по зарплате """

    sorted_vacancies = sorted(
        vacancies,
        key=lambda v: (
            (v.get("salary", {}).get("from") or 0)
            if isinstance(v.get("salary"), dict)
            else 0
        ),
        reverse=True,
    )
    top_vacancies = sorted_vacancies[:n]
    print(f"Топ {n} вакансий по зарплате:")
    for vacancy in top_vacancies:
        print(f"Вакансия: {vacancy['name']}")
        print(f"Зарплата: {vacancy.get('salary', 'Зарплата не указана')}\n")

def user_interaction():
    """ Функция для взаимодействия с пользователем """

    job_file = JsonInfoVacancies("C:/Users/asurk/PycharmProjects/InformationAboutVacancies/data/vacancies.json")


    print("1. Поиск вакансий по ключевому слову")
    print("2. Получить топ N вакансий по зарплате")
    print("3. Найти вакансии с ключевым словом в описании")

    search_query = input("Введите поисковый запрос: ")

    if search_query not in ("1", "2", "3"):
        print("Такого значения нет, попробуйте снова.")
        return

    if search_query == "1":
        keyword = input("Введите ключевое слово для поиска вакансий: ")
        vacancies = HH()._get_vacancies(keyword)
        vacancies_list = VacanciesComparisons.from_vacancy(vacancies)
        job_file.add_vacancy(vacancies_list)
        print(f"Добавлено {len(vacancies_list)} вакансий.")

    elif search_query == "2":
        top_n = int(input("Укажите, сколько вакансий вы хотите увидеть: "))
        vacancies = HH()._get_vacancies()
        sort_vacancies_salary(vacancies, top_n)

    elif search_query == "3":
        filter_words  = input("Введите ключевое слово для поиска в описаниях: ")
        data = job_file._file_vacancy()
        filtered = [v for v in data if filter_words.lower() in v["description"].lower()]
        for vacancy in filtered:
            print(vacancy)
