import requests

#открыть каталог
def test_open_catalog():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI1MTI1OTQsImV4cCI6MTcyMjUxNjE5NCwidHlwZSI6MjB9.rUG7_rz4pBrUERsPqxCRqfCGtaIapWoNPzOYYAPtJt4'
    }
    response = requests.get(base_URL + 'v2/categories')
    assert response.status_code == 401

#просмотр личных данных
def test_show_personal_date():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI1MTI1OTQsImV4cCI6MTcyMjUxNjE5NCwidHlwZSI6MjB9.rUG7_rz4pBrUERsPqxCRqfCGtaIapWoNPzOYYAPtJt4'
    }
    response = requests.get(base_URL + 'v1/profile/personal-data')
    assert response.status_code == 401

#добавить товар в корзину
def test_add_product_to_cart():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI1MTI1OTQsImV4cCI6MTcyMjUxNjE5NCwidHlwZSI6MjB9.rUG7_rz4pBrUERsPqxCRqfCGtaIapWoNPzOYYAPtJt4'
    }
    response = requests.post(base_URL + 'v1/cart/product')
    assert response.status_code == 401

#очистить корзину
def test_empty_card():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI1MTI1OTQsImV4cCI6MTcyMjUxNjE5NCwidHlwZSI6MjB9.rUG7_rz4pBrUERsPqxCRqfCGtaIapWoNPzOYYAPtJt4'
    }
    response = requests.delete(base_URL + 'v1/cart')
    assert response.status_code == 401