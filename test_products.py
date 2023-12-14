from playwright.sync_api import Page, Playwright, sync_playwright, expect
from time import sleep
import re


def product_verification(page: Page):

    page.get_by_role("tab", name="Продукты").click()
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="Создать").click()
    page.get_by_label("​", exact=True).click()
    page.get_by_role("option", name="Огород").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("Огород у бабушки")
    page.get_by_label("Срочная").check()
    page.get_by_label("Плановая").check()
    page.get_by_label("Самовывоз").check()
    page.get_by_role("button", name="arrow up").click()
    page.get_by_role("spinbutton").click()
    page.get_by_label("Выберите тип доставки").click()
    page.get_by_role("option", name="OTP + скан + последконтроль").click()
    page.locator("#mui-component-select-pickupDeliveryGraph").click()
    page.get_by_role("option", name="Самовывоз с OTP+ scan+ post control").click()
    page.locator("#distribute").check()
    page.locator("#distribute").uncheck()
    page.get_by_label("​", exact=True).click()
    page.get_by_label("Выбрать все").check()
    page.locator(".MuiBackdrop-root").click()
    page.get_by_role("button", name="Перенос встречи").click()
    page.get_by_role("button", name="На доработке", exact=True).click()
    page.locator("#courier_appointed_sms_on").check()
    page.locator("#courier_appointed_sms_on").uncheck()
    page.get_by_label("Кол-во и название требуемых фотографий для последующего контроля*").click()

    page.locator("div").filter(
        has_text=re.compile(r"^Кол-во и название требуемых фотографий для последующего контроля\*$")).get_by_role(
        "button").nth(2).click()

    page.get_by_label("Добавить название фото").click()
    page.get_by_placeholder("Название фотографии").fill("Пусть будет картошка")
    page.locator("div").filter(
        has_text=re.compile(r"^Кол-во и название требуемых фотографий для последующего контроля\*$")).get_by_role(
        "button").nth(2).click()

    page.locator("#cities").click()
    page.get_by_label("Алматы").check()
    page.get_by_label("Караганда").check()
    page.locator("div").filter(has_text=re.compile(r"^Города\*2АлматыКараганда$")).first.click()
    page.get_by_role("button", name="Алматы").click()
    page.get_by_role("button", name="Сохранить").is_visible()

    print("Продукты GOOD")
    sleep(1)
