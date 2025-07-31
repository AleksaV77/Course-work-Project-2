import json
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict

from src.class_vacancies import VacanciesComparisons

class SavingInfoVacancies(ABC):
    """Абстрактный класс, для добавления вакансий в файл"""

    @abstractmethod
    def _file_vacancy(self):
        """Абстрактный метод для получения данных из файла"""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: List[VacanciesComparisons]):
        """Абстрактный метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Абстрактный метод для удаления вакансии из файла"""
        pass

class JsonInfoVacancies(SavingInfoVacancies):
    """Класс для работы с JSON-файлами вакансий"""

    filename = "C:/Users/asurk/PycharmProjects/InformationAboutVacancies/data/vacancies.json"

    def __init__(self, filename="vacancies.json") -> None:
        self.__filename = filename
        if not os.path.exists(self.__filename):
            self.add_vacancy([])

    def _file_vacancy(self) -> list[dict]:
        """Получение данных из файла"""
        try:
            with open(self.__filename, "r", encoding="utf-8") as f:
                data = f.read().strip()
                return json.loads(data) if data else []
        except FileNotFoundError:
            return []

    def _save_vacancy(self, data: List[Dict]) -> None:
        """Приватный метод для сохранения вакансий в JSON-файл."""
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

    def add_vacancy(self, vacancies: List[VacanciesComparisons]) -> None:
        """ Метод добавления список вакансий в JSON - файл """

        data = self._file_vacancy()
        for vacancy in vacancies:
            vacancy_dict = vacancy.to_dict()
            if vacancy_dict not in data:
                data.append(vacancy_dict)
        self._save_vacancy(data)

    def _get_vacancies(self, vacancy):
        """Возвращает список вакансий, которые соответствуют заданным критериям."""

        data = self._file_vacancy()
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in vacancy.items()):
                result.append(item)
        return result

    def delete_vacancy(self, vacancy: Dict) -> None:
        """ Удаление вакансии по критерию """
        data = self._file_vacancy()
        data = [item for item in data if not all(item.get(key) == value for key, value in vacancy.items())]
        self._save_vacancy(data)
