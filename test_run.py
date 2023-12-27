from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

def testrun(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True,slow_mo=10)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    # page.pause()
    page.get_by_role("button", name="Log In").click()
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("milind.divre")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("CapsLock")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("CapsLock")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("milind.divre@test.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("123456")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    # page.pause()
    expect(page.get_by_test_id("siteMembers.inlineErrorMsg")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


@pytest.mark.skip
def testrun2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=10)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    # page.pause()
    page.get_by_role("button", name="Log In").click()
    page.wait_for_load_state("networkidle")
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("milind.divre")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("CapsLock")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("CapsLock")
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("milind.divre@test.com")
    page.get_by_test_id("emailAuth").get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("123456")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    # page.pause()
    expect(page.get_by_test_id("siteMembers.inlineErrorMsg")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()