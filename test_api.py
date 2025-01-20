import requests
import json

BASE_URL = "https://box7-fastapi-505ffc77ba2f.herokuapp.com"

def test_login():
    login_data = {
        "email": "gael.jaunin@gmail.com",
        "password": "1234azerty"
    }
    
    print("=== Testing Login ===")
    print(f"Connecting to {BASE_URL}")
    
    # Test login
    response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
    print(f"\nLogin Status: {response.status_code}")
    
    print("\nCookie Details:")
    for cookie in response.cookies:
        print("-" * 50)
        print(f"Name: {cookie.name}")
        print(f"Value: {cookie.value[:20]}...")  # Only show start of value
        print(f"Domain: {cookie.domain}")
        print(f"Secure: {cookie.secure}")
        print(f"HttpOnly: {'httponly' in cookie._rest}")
        print(f"Path: {cookie.path}")
    
    # Test protected route with session
    if response.status_code == 200:
        print("\n=== Testing Protected Route ===")
        session = requests.Session()
        session.cookies.update(response.cookies)
        auth_check = session.get(f"{BASE_URL}/auth/check-auth")
        print(f"Auth Check Status: {auth_check.status_code}")
        if auth_check.ok:
            print("Auth Check Response:")
            print(json.dumps(auth_check.json(), indent=2))

if __name__ == "__main__":
    test_login()
