from playwright.sync_api import sync_playwright
from test_profile import profile_verification
from test_login import login_full, login_short
from test_statistics import statistics_verification
from test_courier import courier_verification
from test_shipment_point import shipment_point_verification
from test_products import product_verification
from test_monitoring import monitoring_verification
from test_delivery_zones import delivery_zones_verification
from test_review import review_verification
from test_rating import ratings_verification
from test_order_chain import order_chain_verification

#
# def test_check():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(args=['--start-maximized'], headless=False)
#         with browser.new_page(no_viewport=True) as page:
#             # login_short(page)                        #Укороченная авторизация
#             login_full(page)
#             profile_verification(page)  # Страница профиля
#             statistics_verification(page)  # Страница статистики
#             # application_verification(page)           #Страница заявки
#             courier_verification(page)  # Страница курьера
#             # partner_verification(page)               #Страница партнера
#             shipment_point_verification(page)  # Страница точки вывоза
#             product_verification(page)  # Страница продуктов
#             monitoring_verification(page)  # Страница мониторинга
#             delivery_zones_verification(page)  # Страница зоны доставки
#             # users_verification(page)                 #Страница пользователей
#             review_verification(page)  # Страница отзыва
#             ratings_verification(page)  # Страница рейтинга
#             # order_groups_verification(page)          #Страница группы заявок
#             order_chain_verification(page)           #Страница многоэтапной доставки
#
#         browser.close()


def test_for_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=['--start-maximized'], headless=False)
        with browser.new_page(no_viewport=True) as page:
            login_short(page)
            order_chain_verification(page)
        browser.close()
