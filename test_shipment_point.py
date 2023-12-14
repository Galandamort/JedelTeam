import time
from playwright.sync_api import Page
from playwright.async_api import Page
from test_login import login


def shipment_point_verification(page: Page):

    page.get_by_role("tab", name="Точки вывоза").click()
    page.get_by_role("button", name="Добавить").click()
    page.get_by_placeholder("Города").click()
    page.get_by_role("menuitem", name="Алматы").locator("label").click()
    page.get_by_text("На карте").click()
    page.locator("#map-container").click()
    page.get_by_label("Офис").check()
    page.locator("input[name=\"block\"]").fill("1")
    page.locator("input[name=\"floorOffice\"]").fill("2")
    page.locator("input[name=\"office\"]").fill("3")
    page.get_by_role("heading", name="Добавление новой точки вывоза").get_by_role("button").click()
    page.get_by_role("cell", name="Алматы, проспект Абая, 8А, Медеуский район", exact=True).click()

    page.get_by_role("heading", name="Данные о точке вывоза").click()
    page.get_by_role("heading", name="Курьер по умолчанию для группы заявок").click()
    page.get_by_role("heading", name="История").click()

    page.get_by_role("button", name="Редактировать").click()
    time.sleep(20)

    while page.get_by_role("menuitem", name="Ель На дереве").is_hidden():
        if page.locator("#courier").is_visible():
            page.locator("#courier").click()
            page.get_by_role("menuitem", name="Ель На дереве").click()
            break
        else:
            continue
    page.get_by_role("button", name="Сохранить").click()

    print("Точки доставки GOOD")
    time.sleep(1)
