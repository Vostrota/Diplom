import requests

#открыть каталог
def test_open_catalog():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI4ODA5MTUsImV4cCI6MTcyMjg4NDUxNSwidHlwZSI6MjB9.Cj611jJuZ9R6agiViz4egC22Xhe-hzGL6YPmOkbIKbo'
    }
    response = requests.get(base_URL + 'v2/categories', headers=headers)
    assert response.status_code == 200

#просмотр личных данных
def test_show_personal_date():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI4ODA5MTUsImV4cCI6MTcyMjg4NDUxNSwidHlwZSI6MjB9.Cj611jJuZ9R6agiViz4egC22Xhe-hzGL6YPmOkbIKbo'
    }
    response = requests.get(base_URL + 'v1/profile/personal-data', headers=headers)
    assert response.status_code == 200

#добавить товар в корзину
def test_add_product_to_cart():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI4ODA5MTUsImV4cCI6MTcyMjg4NDUxNSwidHlwZSI6MjB9.Cj611jJuZ9R6agiViz4egC22Xhe-hzGL6YPmOkbIKbo'
    }
    data = {
        "productId": 2715144,
        "quantity": 1
    }
    response = requests.post(base_URL + 'v1/cart/product', headers=headers, json=data)
    assert response.status_code == 200

#очистить корзину
def test_empty_card():
    base_URL = 'https://web-gate.chitai-gorod.ru/api/'
    headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwOTA4MzgxLCJpYXQiOjE3MjI4ODA5MTUsImV4cCI6MTcyMjg4NDUxNSwidHlwZSI6MjB9.Cj611jJuZ9R6agiViz4egC22Xhe-hzGL6YPmOkbIKbo'
    }
    response = requests.delete(base_URL + 'v1/cart', headers=headers)
    assert response.status_code == 200

