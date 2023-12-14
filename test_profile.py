from playwright.sync_api import Page
from time import sleep
from test_login import login


def profile_verification(page: Page):

    a = {"Данные менеджера",
         "Фамилия",
         "Имя",
         "Отчество",
         "Номер телефона",
         "Email",
         "Роль",
         "Войти под другой ролью",
         "Данные об организации",
         "Название",
         "БИН",
         "Руководитель",
         "График работы",
         "Настройки организации",
         "Продукт по умолчанию для группы заявок",
         "Адрес офиса курьерской службы"
         }

    page.get_by_role("link", name="+77056119742").click()
    sleep(3)
    for i in a:
        element = page.get_by_text(i, exact=True)
        if element.is_visible():
            continue
        else:
            print(f'{i} - не видим на странице.')

    page.get_by_role("button", name="Менеджер").click()
    page.locator("#menu- div").first.click()

    page.get_by_role("button", name="Редактировать").click()
    page.wait_for_load_state("networkidle")
    page.get_by_placeholder("Введите фамилию").fill("На дереве")
    page.get_by_placeholder("Введите имя").fill("Ель")
    page.get_by_placeholder("Введите отчество").fill("Растет")
    page.get_by_placeholder("Введите название организации").fill("Огород")
    page.get_by_placeholder("09:00").fill("08:45")
    page.get_by_placeholder("18:00").fill("17:45")
    page.get_by_role("button", name="Сохранить").click()

    print("Профиль GOOD")
    sleep(1)

