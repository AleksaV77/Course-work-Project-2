from abc import ABC, abstractmethod
from typing import List, Dict

import requests

class Parser(ABC):
    """ Абстрактный класс для работы с API """

    @abstractmethod
    def _connect_api(self, keyword):
        """Метод подключения к api"""
        pass

    @abstractmethod
    def _get_vacancies(self, keyword):
        """Метод получения вакансий"""
        pass

class HH(Parser):
    """Класс подключаться к API и получать вакансии"""

    def __init__(self, url="https://api.hh.ru/vacancies") -> None:
        self.url = url
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__()

    def _connect_api(self, keyword):
        """Метод подключения к API"""

        params = {"text": keyword, "per_page": 20}
        response = requests.get(self.url, params=params)
        if response.status_code != 200:
            print(f"Произошла ошибка: {response.status_code}")
            return None
        data = response.json()
        return data

    def _get_vacancies(self, keyword=""):
        """Метод получения вакансий"""

        data = self._connect_api(keyword)
        if data and "items" in data:
            return data["items"]
        else:
            return []

