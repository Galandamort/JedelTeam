from playwright.sync_api import Page
from time import sleep


def statistics_verification(page: Page):
    page.get_by_role("tab", name="Статистика").click()

    page.locator("button").nth(3).click()
    page.get_by_role("button", name="Сегодня").click()
    page.get_by_role("button", name="7 дней").click()
    page.get_by_role("button", name="1 месяц").click()
    page.get_by_role("button", name="1 год").click()
    page.get_by_placeholder("-").click()
    page.get_by_placeholder("-").press("Control+a")
    page.get_by_placeholder("-").fill("10")
    page.get_by_role("button", name="Применить").click()
    #
    page.get_by_label("Все города").click()
    page.get_by_role("option", name="Все города").click()
    page.get_by_label("Все партнеры").click()
    page.locator("#menu-partner div").first.click()
    #
    page.get_by_role("heading", name="Количество заявок по дням").click()
    page.get_by_label("Новые", exact=True).click()
    page.get_by_role("option", name="Доставленные").click()
    page.get_by_label("Доставленные", exact=True).click()
    page.get_by_role("option", name="Отмененные").click()
    page.get_by_label("Отмененные", exact=True).click()
    page.get_by_role("option", name="Новые").click()
    #
    page.get_by_role("heading", name="Плотность выполнения в течении суток").click()
    page.get_by_role("heading", name="Тепловая карта").click()
    #
    page.get_by_role("link", name="По курьерам").click()
    #
    page.get_by_role("button").nth(3).click()
    page.get_by_text("Выберите период").click()
    page.get_by_role("button", name="Сегодня").click()
    page.get_by_role("button", name="7 дней").click()
    page.get_by_role("button", name="1 месяц").click()
    page.get_by_role("button", name="1 год").click()
    page.get_by_placeholder("-").click()
    page.get_by_placeholder("-").press("Control+a")
    page.get_by_placeholder("-").fill("10")
    page.get_by_role("button", name="Применить").click()
    # -------------------------------------------------------------------------------------------- Отчет по заявкам
    page.get_by_role("link", name="Общая").click()
    page.get_by_role("button", name="Сформировать отчет").click()
    page.get_by_role("menuitem", name="Отчет по заявкам").click()
    #
    page.get_by_placeholder("Города").click()
    page.get_by_label("KZ").click()
    page.get_by_label("Фильтры для формирования отчета").click()

    page.locator("#partner").click()
    page.get_by_text("Выбрать все").click()
    page.click('body')

    page.locator("#courier").click()
    page.mouse.click(0, 0)

    page.locator("#shipmentPoint").click()
    page.get_by_text("Выбрать все").click()
    page.click('body')

    page.locator("#status").click()
    page.get_by_label("Выбрать все").click()
    page.click('body')

    page.get_by_text("Статусы").click()
    page.get_by_text("Заявки, которые были приняты в работу курьерами").click()
    #
    page.locator("input[name=\"period\"]").click()
    page.get_by_role("button", name="Сегодня").click()
    page.get_by_role("button", name="7 дней").click()
    page.get_by_role("button", name="1 месяц").click()
    page.get_by_role("button", name="1 год").click()
    page.get_by_placeholder("-").click()
    page.get_by_placeholder("-").press("Control+a")
    page.get_by_placeholder("-").fill("10")
    page.get_by_role("button", name="Применить").click()
    page.locator("input[name=\"deliveryDatePeriod\"]").click()
    page.get_by_role("button", name="Сегодня").click()
    page.get_by_role("button", name="7 дней").click()
    page.get_by_role("button", name="1 месяц").click()
    page.get_by_role("button", name="1 год").click()
    page.get_by_placeholder("-").click()
    page.get_by_placeholder("-").press("Control+a")
    page.get_by_placeholder("-").fill("10")
    page.get_by_role("button", name="Применить").click()
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Сформировать").click()
    download = download_info.value
    # -------------------------------------------------------------------------------------------- Отчет по группам
    page.get_by_role("button", name="Сформировать отчет").click()
    page.get_by_role("menuitem", name="Отчет по группам заявок").click()

    page.locator("#partner").click()
    page.get_by_text("Выбрать все").click()
    page.locator("#menu-partner > .MuiBackdrop-root").click()

    page.locator("#courier").click()
    page.mouse.click(0, 0)

    page.locator("#status").click()
    page.get_by_text("Выбрать все").click()
    page.mouse.click(0, 0)

    page.locator("#sorter").click()
    page.mouse.click(0, 0)

    page.locator("#shipmentPoint").click()
    page.get_by_text("Выбрать все").click()
    page.mouse.click(0, 0)

    page.get_by_role("textbox").click()
    page.get_by_role("button", name="Сегодня").click()
    page.get_by_role("button", name="7 дней").click()
    page.get_by_role("button", name="1 месяц").click()
    page.get_by_role("button", name="1 год").click()
    page.get_by_placeholder("-").click()
    page.get_by_placeholder("-").press("Control+a")
    page.get_by_placeholder("-").fill("10")
    page.get_by_role("button", name="Применить").click()
    with page.expect_download() as download1_info:
        page.get_by_role("button", name="Сформировать").click()
    download1 = download1_info.value

    print("Статистика GOOD")
    sleep(1)
