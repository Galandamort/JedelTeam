import time
from playwright.sync_api import Page
from test_login import login
import re


def review_verification(page: Page):
    page.get_by_role("tab", name="Курьеры").click()
    page.get_by_role("tab", name="Отзывы").click()
    page.get_by_role("link", name="Новые").click()
    page.get_by_role("link", name="Рассмотренные").click()
    page.get_by_role("link", name="Отклоненные").click()
    page.get_by_role("button", name="Настройка причин").click()

    page.get_by_role("button", name="Добавить").click()
    page.get_by_placeholder("Введите название причины").fill("Курьер был прям хорош")
    page.get_by_label("Отображать в тэгах").check()
    page.get_by_label("Ужасно").check()
    page.get_by_label("Плохо").check()
    page.get_by_label("Нормально").check()
    page.get_by_label("Хорошо").check()
    page.get_by_label("Отлично").check()
    page.locator("form div").filter(has_text="УжасноБаллы:*-+").get_by_role("spinbutton").fill("-20")
    page.locator("form div").filter(has_text="ПлохоБаллы:*-+").get_by_role("spinbutton").fill("-10")
    page.get_by_role("button", name="Добавить").click()

    page.get_by_role("row", name="Курьер был прям хорош Да 5 -1 -5 -10 -20 settings delete").get_by_role(
        "button").first.click()
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("row", name="Курьер был прям хорош Да 5 -1 -5 -10 -20 settings delete").get_by_role(
        "button").nth(1).click()
    page.get_by_role("button", name="Да, удалить").click()

    print("Отзывы GOOD")

    time.sleep(1)
