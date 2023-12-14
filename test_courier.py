import time
from playwright.sync_api import Page
from test_login import login


def courier_verification(page: Page):
    a = {"Легковая машина",
         "Грузовой",
         "Фургон",
         "Велосипед",
         "Мото скутер",
         "Пешком / самокат"
         }

    b = {"Имя*",
         "Фамилия*",
         "Отчество",
         "Дата рождения",
         "Номер телефона*",
         "Адрес прописки",
         "Город*",
         "Тип документа",
         "№ документа",
         "Дата окончания срока действия",
         "Орган выдачи",
         "Транспортное средство*"
         }

    page.get_by_role("tab", name="Курьеры").click()
    # будет ждать, пока страница не достигнет состояния когда нет активных сетевых запросов
    page.wait_for_load_state("networkidle")

    page.locator("#composition-button").nth(1).click()
    page.get_by_role("menuitem", name="Поиск по ФИО курьера").is_visible()
    page.get_by_role("menuitem", name="Поиск по номеру телефона").is_visible()
    page.get_by_role("menuitem", name="Поиск по ИИН").is_visible()

    page.get_by_role("link", name="Ожидают решения").click()

    page.get_by_role("link", name="Отмененные").click()

    page.get_by_role("link", name="Приглашение отправлено").click()
    page.locator("#composition-button").nth(1).click()
    page.get_by_role("menuitem", name="Поиск по номеру телефона").click()
    page.locator("#composition-button").nth(1).click()
    page.get_by_role("menuitem", name="Поиск по ИИН").click()

    page.get_by_role("link", name="Отказались").click()

    page.get_by_role("link", name="Добавленные").click()

    page.get_by_placeholder("Города").click()
    page.get_by_role("menuitem", name="Алматы").locator("label").click()

    page.get_by_role("button", name="Добавить").click()

    for i in b:
        element = page.get_by_text(i, exact=True)
        if element.is_visible():
            continue
        else:
            print(f'{i} - не видим на странице.')

    page.get_by_placeholder("Введите имя").fill("Ель")
    page.get_by_placeholder("Введите фамилию").fill("На дереве")
    page.locator("input[type=\"tel\"]").nth(2).fill(login)
    page.get_by_placeholder("Выберите город").click()
    page.get_by_text("Алматы").click()
    page.get_by_label("Выберите транспортное средство").click()

    for i in a:
        element = page.get_by_role("option", name=i)
        if element.is_visible():
            continue
        else:
            print(f'{i} - не видим на странице.')

    page.get_by_role("option", name="Фургон").click()
    page.get_by_role("button", name="Создать").click()

    print("Курьер GOOD")
