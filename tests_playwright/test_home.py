import logging
import pytest
from playwright.sync_api import sync_playwright
from pageObject_playwright.home_page import *
logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture
def open_home_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://automationpractice.com/index.php")
        yield HomePage(page)
        page.close()


def test_empty_email(open_home_page):
    """
    test that check that no email has been entered
    """
    mylogger.info("test no email")
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    Authntication_page.Login("", "D123456")
    alert = Authntication_page.msg_error()
    assert "An email address required." in alert


def test_invalid_email(open_home_page):
    """
        test that check that an invalid email was entered
    """
    mylogger.info("test fake email")
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    Authntication_page.Login("d2@gmail", "D123456")
    alert = Authntication_page.msg_error()
    assert "Invalid email address" in alert


def test_invalid_password(open_home_page):
    """
    test that check that an invalid password was entered
    """
    mylogger.info("test invalid password")
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    Authntication_page.Login("d2@gmail.com", "1234")
    alert = Authntication_page.msg_error()
    assert "Invalid password" in alert


def test_unregistered_authentication(open_home_page):
    """
    test that check that an invalid authentication try to login
    """
    mylogger.info("test fake authentication")
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    Authntication_page.Login("d2@gmail.com", "123456")
    alert = Authntication_page.msg_error()
    assert "Authentication failed" in alert


def test_empty_password(open_home_page):
    """
    test that check that no password has been entered
    """
    mylogger.info("test no password")
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    Authntication_page.Login("d2@gmail.com", "  ")
    alert = Authntication_page.msg_error()
    assert "Password is required" in alert


def test_valid_authentication(open_home_page):
    """
    test that check valid authentication
    """
    mylogger.info("test valid authentication")
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    MyAccount_page = Authntication_page.Login("d2@gmail.com", "D123456")
    alert = MyAccount_page.valid_authentication()
    assert "Welcome to your account" in alert


def test_forgot_password(open_home_page):
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    msg_forget_pass = Authntication_page.Forget_password()
    assert "Forgot your password" in msg_forget_pass


def test_buy_dress(open_home_page):
    home_page = open_home_page
    Authntication_page = home_page.SingIn()
    MyAccount_page = Authntication_page.Login("d2@gmail.com", "D123456")
    Home_page = MyAccount_page.go_home()
    Search_resulte_page = Home_page.search("summer")
    cheapest_Item_page = Search_resulte_page.choose_cheapest_Item()
    complet_page = cheapest_Item_page.complet_buy()
    comp = complet_page.locator(".cheque-indent").locator(".dark")
    assert "Your order on My Store is complete." in comp.inner_html()
