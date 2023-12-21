import time

from playwright.sync_api import Page, Playwright, sync_playwright, expect
from time import sleep
import re


def order_chain_verification(page: Page):
    page.get_by_role("tab", name="Многоэтапная доставка").click()
    page.get_by_role("button", name="Создать").click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Огород").click()
    page.locator("input[name=\"packageName\"]").fill("Называние посылки")
    page.locator("input[name=\"packageDescription\"]").fill("Описание посылки")
    page.locator("input[name=\"packageLength\"]").fill("1")
    page.locator("input[name=\"packageHeight\"]").fill("2")
    page.locator("input[name=\"packageWidth\"]").fill("3")
    page.locator("input[name=\"packageWeight\"]").fill("4")
    # page.get_by_label("Choose date, selected date is 22 дек. 2023 г.").click()
    # page.get_by_label("Choose date, selected date is 22 дек. 2023 г.").click()
    page.locator("input[name=\"senderName\"]").fill("Имя отправителя")
    page.locator("input[type=\"tel\"]").nth(2).fill("+7 705 611-97-42")
    page.locator("#senderCityId").click()
    page.get_by_text("Алматы").click()
    page.get_by_text("На карте").first.click()
    time.sleep(1)
    page.locator("#map-container").click()
    page.locator("input[name=\"receiverName\"]").fill("Имя получателя")
    page.locator("input[type=\"tel\"]").nth(3).fill("+7 705 611-97-42")
    page.locator("#receiverCityId").click()
    page.get_by_text("Алматы").click()
    page.get_by_text("На карте").nth(1).click()
    time.sleep(1)
    page.locator("#map-container").click()
    # Создать этап и удалить ее
    page.locator("div").filter(has_text=re.compile(r"^Создать этап$")).nth(1).click()
    page.get_by_text("Последний этап").click()
    page.locator("#mui-component-select-stageType").click()
    page.get_by_role("option", name="ЖД").click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Базовый", exact=True).click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Плановая").click()
    page.get_by_role("button", name="Создать").click()
    page.locator("#composition-button").click()
    page.get_by_role("menuitem", name="Удалить этап").click()
    # Создать первый этап
    page.locator("div").filter(has_text=re.compile(r"^Создать этап$")).nth(1).click()
    page.locator("#mui-component-select-stageType").click()
    page.get_by_role("option", name="Морской").click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Базовый", exact=True).click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Срочная").click()
    page.locator("input[name=\"stageOrderReceiverName\"]").fill("Имя получателя 1")
    page.locator("form div").filter(has_text="Номер телефона получате").get_by_role("textbox").fill("+7 705 611-97-42")
    page.locator("#stageOrderReceiverCityId").click()
    page.get_by_text("Алматы").click()
    page.get_by_label("Создание этапа").get_by_text("На карте").click()
    time.sleep(1)
    page.locator("#map-container").click()
    page.locator("input[name=\"stageOrderComment\"]").fill("Комментарий к этапу 1")
    page.get_by_role("button", name="Создать").click()
    # Создать последний этап
    page.locator("div").filter(has_text=re.compile(r"^Создать этап$")).first.click()
    page.get_by_label("Последний этап").check()
    page.locator("#mui-component-select-stageType").click()
    page.get_by_role("option", name="Авиа").click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Базовый", exact=True).click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Срочная").click()
    page.locator("input[name=\"stageOrderComment\"]").fill("Комментарий к этапу 2")
    page.get_by_role("button", name="Создать").click()

    page.get_by_placeholder("Добавить комментарий").fill("Комментарий к заявке")
    page.get_by_role("button", name="Создать").click()
    page.get_by_role("link", name="История").click()
    page.get_by_role("link", name="Данные").click()
    page.get_by_role("button", name="Редактировать").click()
    page.locator("header").filter(has_text="Этап №1").locator("#composition-button").click()
    page.get_by_role("menuitem", name="Загрузка документа").click()
    page.get_by_role("button", name="Подтвердить").click()
    page.get_by_role("heading", name="Загрузка документа").get_by_role("button").click()
    page.get_by_role("button", name="Подтвердить").click()
    page.locator("header").filter(has_text="Этап №2").get_by_label("Открыть этап").click()

    print("Многоэтапная доставка GOOD")
    sleep(1)
