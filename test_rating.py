import time
from playwright.sync_api import Page
import time


def ratings_verification(page: Page):
    page.get_by_role("tab", name="Рейтинг").click()
    page.get_by_role("button", name="Настройка категорий").click()
    page.get_by_role("button", name="Добавить").click()
    page.get_by_placeholder("Введите название").fill("Категория ")
    page.get_by_placeholder("Введите степень категории").fill("-20")
    page.get_by_placeholder("Введите степень категории").fill("41")
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("button", name="settings").click()
    page.get_by_placeholder("Введите название").fill("На удаление")
    page.get_by_role("button", name="arrow down").click()
    page.get_by_role("button", name="arrow up").click()
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("button", name="delete").click()
    page.get_by_role("button", name="Да, удалить").click()

    print("Рейтинг GOOD")

    time.sleep(1)
