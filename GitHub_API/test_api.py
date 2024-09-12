import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USER = os.getenv('GITHUB_USER')
REPO_NAME = os.getenv('REPO_NAME')

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def create_repo(repo_name):
    """Создание нового репозитория"""
    url = f"https://api.github.com/user/repos"
    data = {
        "name": repo_name,
        "private": False
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Репозиторий '{repo_name}' успешно создан.")
    else:
        print(f"Ошибка создания репозитория: {response.json()}")
    return response


def check_repo_exists(repo_name):
    """Проверка наличия репозитория"""
    url = f"https://api.github.com/users/{GITHUB_USER}/repos"
    response = requests.get(url, headers=headers)
    repos = [repo['name'] for repo in response.json()]
    if repo_name in repos:
        print(f"Репозиторий '{repo_name}' найден.")
        return True
    else:
        print(f"Репозиторий '{repo_name}' не найден.")
        return False


def delete_repo(repo_name):
    """Удаление репозитория"""
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Репозиторий '{repo_name}' успешно удален.")
    else:
        print(f"Ошибка удаления репозитория: {response.status_code}, {response.json()}")


def test_github_api():
    """Основная функция для тестирования GitHub_API"""
    # Шаг 1: Создание репозитория
    create_repo(REPO_NAME)

    # Шаг 2: Проверка существования репозитория
    if check_repo_exists(REPO_NAME):
        # Шаг 3: Удаление репозитория
        delete_repo(REPO_NAME)
    else:
        print(f"Репозиторий '{REPO_NAME}' не найден после создания!")


if __name__ == "__main__":
    test_github_api()
