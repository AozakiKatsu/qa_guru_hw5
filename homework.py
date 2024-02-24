from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=23)
    if time(hour=6) < current_time < time(hour=22):
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    if dark_theme_enabled_by_user is None:
        if current_time >= time(hour=22) or current_time < time(hour=6):
            is_dark_theme = True
    elif dark_theme_enabled_by_user:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_find_suitable_user():
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = None
    for user in users:
        if user['name'] == 'Olga':
            suitable_users = user
    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def prettify_function_name(func, *arg):
    pretty_function_name = func.__name__.replace('_', ' ').title()
    pretty_arguments = ', '.join(arg)
    print(f'{pretty_function_name} [{pretty_arguments}]')
    return f'{pretty_function_name} [{pretty_arguments}]'


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = prettify_function_name(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = prettify_function_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = prettify_function_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
