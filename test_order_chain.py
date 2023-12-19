from playwright.sync_api import Page, Playwright, sync_playwright, expect
from time import sleep


def product_verification(page: Page):
    page.get_by_role("tab", name="Многоэтапная доставка").click()

    print("Многоэтапная доставка GOOD")
    sleep(1)
