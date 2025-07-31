from typing import Dict, List


class VacanciesComparisons:
    """Класс для работы с вакансиями"""

    __slots__ = (
        "name",
        "url",
        "salary",
        "description",
    )

    def __init__(self, name, url, salary, description=""):
        self.name = self._validate_name(name)
        self.url = self._validate_url(url)
        self.salary = self._validate_salary(salary)
        self.description = self._validate_description(description)

    def _validate_name(self, name):
        """Проверяет, что указано название вакансии"""

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Укажите название вакансии")
        return name

    def _validate_url(self, url):
        """Проверяет, что ссылка указана корректно"""

        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError("Некорректная ссылка на вакансию")
        return url

    def _validate_salary(self, salary):
        """Сравнения вакансий между собой по зарплате"""

        if not isinstance(salary, (int, float)) or salary <= 0:
            return "Зарплата не указана"
        else:
            return salary

    def _validate_description(self, description):
        """Проверяет, что описание является непустой строкой"""

        if not isinstance(description, str) or not description.strip():
            raise ValueError("Описание не указано")
        return description

    def __eq__(self, other) -> bool:
        """Метод определяет, являются ли два объекта равными."""
        return self.salary == other.salary

    def __lt__(self, other):
        """Магический метод, для сравнения вакансий по зарплате."""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод, для сравнения вакансий по зарплате"""
        return self.salary > other.salary

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Вакансия: {self.name}, Область: {self.description}, Зарплата: {self.salary}, URL: {self.url}"

    @staticmethod
    def from_vacancy(vacancy_info: List[Dict]) -> List:
        """Метод для формирования списка вакансий"""

        vacancies = []
        for job in vacancy_info:
            name = job.get("name", "Название не указано")
            url = job.get("url", "")

            salary = job.get("salary", {}).get("from", 0) if job.get("salary") else 0

            department = job.get("department")
            description = department.get("name", "Описание не указано") if department else "Описание не указано"

            vacancy = VacanciesComparisons(
                name=name, url=url, salary=salary, description=description
            )
            vacancies.append(vacancy)
        return vacancies
    #
    def to_dict(self) -> Dict:
        """Преобразование в словарь"""

        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }
