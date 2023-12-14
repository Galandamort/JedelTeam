from playwright.sync_api import Page, Playwright, sync_playwright, expect
from time import sleep
import re


def monitoring_verification(page: Page):

    page.get_by_role("tab", name="Мониторинг").click()
    page.get_by_placeholder("Выберите город").click()
    page.get_by_text("Алматы").click()
    page.get_by_role("row", name="На дереве Ель +77056119742").locator("div").first.click()
    page.get_by_text("Данные курьера").click(click_count=3)
    page.get_by_text("Заявки курьера").click()
    page.get_by_role("button", name="Вернуться в Список курьеров").click()
    page.get_by_label("Сбросить").click()
    page.get_by_placeholder("Выберите город").click()
    page.get_by_text("Шымкент").click()
    page.get_by_role("button", name="arrow").click()
    page.get_by_role("button", name="arrow").click()
    page.locator("#monitoring-map").click()

    print("Мониторинг GOOD")
    sleep(1)
