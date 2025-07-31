from unittest.mock import Mock, patch


def test_hh_api_init(test_hh_api):
    assert test_hh_api.url == "https://api.hh.ru/vacancies"


def test_get_vacancies(vacancies_hh_api):
    """Тест на получение вакансий"""

    with patch("requests.get") as mock_get:

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": [{"id": 1, "name": "Developer"}]}

        vacancies = vacancies_hh_api._get_vacancies("developer")
        assert len(vacancies) == 1
        assert vacancies[0]["name"] == "Developer"
