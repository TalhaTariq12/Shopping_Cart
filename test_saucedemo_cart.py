import pytest
from playwright.sync_api import Page, expect

def test_cart_checkoutToHome(page: Page):
  
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator(".title")).to_have_text("Products")

    # page.locator('[data-test="product-sort-container"]').select_option("hilo")  
    # expect(page.locator('.inventory_item_name').first).to_have_text("Sauce Labs Fleece Jacket")

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")


    page.locator(".shopping_cart_link").click()
    expect(page.locator(".title")).to_have_text("Your Cart")

    page.locator('[data-test="remove-sauce-labs-bike-light"]').click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    expect(page.locator('.inventory_item_name')).to_have_text("Sauce Labs Backpack")

  
    page.locator('[data-test="checkout"]').click()
    expect(page.locator(".title")).to_have_text("Checkout: Your Information")

    page.locator('[data-test="firstName"]').fill("John")
    page.locator('[data-test="lastName"]').fill("Doe")
    page.locator('[data-test="postalCode"]').fill("T1234")
    page.locator('[data-test="continue"]').click()

    expect(page.locator(".title")).to_have_text("Checkout: Overview")
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
    page.locator('[data-test="finish"]').click()

   
    expect(page.locator(".title")).to_have_text("Checkout: Complete!")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

  
    page.wait_for_timeout(5000)

  
    back_home_btn = page.locator('[data-test="back-to-products"]')
    expect(back_home_btn).to_be_visible()
    back_home_btn.click()

    expect(page.locator(".title")).to_have_text("Products")
