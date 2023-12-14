import time
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

login = "+7 705 611-97-42"


def login_full(page: Page):
    a = {"Kyrgyzstan +996",
         "Russia +7",
         "United Arab Emirates +971",
         "Ukraine +380",
         "Uzbekistan +998",
         "Kazakhstan +7"
         }

    page.goto("https://preprod.loggy.kz/login")
    # будет ждать, пока страница не достигнет состояния когда нет активных сетевых запросов
    page.wait_for_load_state("networkidle")
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("+")
    page.get_by_label("Country selector").click()

    for i in a:
        element = page.get_by_label(i).locator("img")
        if element.is_visible():
            continue
        else:
            print(f'Элемент с селектором {i} не видим на странице.')

    page.get_by_label("Country selector").click()
    page.get_by_text("Войти с помощью электронной почты").click()
    page.get_by_text("Войти с помощью номера телефона").click()
    page.get_by_role("textbox").fill(login)
    page.get_by_role("button", name="Получить OTP-код").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("1")
    page.get_by_role("textbox").nth(2).fill("1")
    page.get_by_role("textbox").nth(3).fill("1")
    page.get_by_role("textbox").nth(4).fill("1")
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("option", name="Менеджер", exact=True).click()
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="ОК").click()
    page.get_by_label("css-kzdnpn-MuiButtonBase-root").click()
    page.locator(".MuiButtonBase-root").first.click()
    page.locator(".css-1uzvz49").click()

    print("Авторизация GOOD")


def login_short(page: Page):
    page.goto("https://preprod.loggy.kz/login")
    page.get_by_role("textbox").fill(login)
    page.get_by_role("button", name="Получить OTP-код").click()
    time.sleep(3)
    page.get_by_role("textbox").nth(1).fill("1")
    page.get_by_role("textbox").nth(2).fill("1")
    page.get_by_role("textbox").nth(3).fill("1")
    page.get_by_role("textbox").nth(4).fill("1")
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("option", name="Менеджер", exact=True).click()
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("button", name="ОК").click()
    page.locator(".MuiButtonBase-root").first.click()
    page.locator(".css-1uzvz49").click()

    print('\n'"Авторизация Короткая авторизация GOOD")
    time.sleep(1)
