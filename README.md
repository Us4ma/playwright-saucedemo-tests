# 🧪 SauceDemo QA Automation Suite

This is a real-world, industry-style QA automation framework built for [SauceDemo](https://www.saucedemo.com) using:

- ✅ Python
- ✅ Playwright (Sync API)
- ✅ Pytest
- ✅ Allure Reporting

---

## 📁 Project Structure

MockProject_SauceDemo/
│
├── Pages/
│ ├── login_page.py # Page Object Model (POM) for login
│ ├── inventory_page.py # POM for inventory (product listing)
│ ├── cart_page.py # POM for cart operations
│ ├── checkout_page.py # POM for checkout flow
│
├── Tests/
│ ├── test_login.py # Login validation (valid + negative cases)
│ ├── test_inventory.py # Add-to-cart and cart badge assertion
│ ├── test_cart.py # Cart item verification
│ ├── test_checkout.py # Full checkout flow test
│
├── conftest.py # Playwright fixture for page setup
├── requirements.txt # Dependencies
├── .gitignore
└── README.md

yaml
Copy
Edit

---

## 🚀 How to Run the Tests

1. **Install dependencies**  
pip install -r requirements.txt

markdown
Copy
Edit

2. **Run all tests with Allure results**  
pytest --alluredir=allure-results

markdown
Copy
Edit

3. **View the Allure Report**  
allure serve allure-results

yaml
Copy
Edit

---

## 🎯 Features Covered

- ✅ Login (valid and invalid credentials)
- ✅ Add all products to cart
- ✅ Verify cart items and count
- ✅ Complete checkout process with form submission
- ✅ Assertion-based validation (URLs, elements, text)

---

## 📸 Reporting

Allure is integrated for rich visual reporting:
- Execution trends
- Step-by-step traceability
- Test data insights

---

## 🙋‍♂️ Author

**Muhammad Usama Qamar**  
QA Automation Engineer  
[GitHub](https://github.com/Us4ma)

---
