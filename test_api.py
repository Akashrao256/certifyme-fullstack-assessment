#!/usr/bin/env python3
"""
API Testing Script - Verify all endpoints are working
"""

import requests
import json
from requests.cookies import RequestsCookieJar

BASE_URL = "http://localhost:5000"
API_BASE = f"{BASE_URL}/api"

# Create session to maintain cookies
session = requests.Session()

print("\n" + "="*80)
print("BACKEND API TESTING")
print("="*80 + "\n")

# Test 1: Signup
print("TEST 1: POST /api/auth/signup")
print("-" * 80)
signup_data = {
    "full_name": "Test User",
    "email": "testuser@example.com",
    "password": "TestPass123!",
    "confirm_password": "TestPass123!"
}
response = session.post(f"{API_BASE}/auth/signup", json=signup_data)
print(f"Status: {response.status_code} - {'✅ PASS' if response.status_code == 201 else '❌ FAIL'}")
print(f"Response: {response.json()}\n")

# Test 2: Login
print("TEST 2: POST /api/auth/login")
print("-" * 80)
login_data = {
    "email": "testuser@example.com",
    "password": "TestPass123!"
}
response = session.post(f"{API_BASE}/auth/login", json=login_data)
print(f"Status: {response.status_code} - {'✅ PASS' if response.status_code == 200 else '❌ FAIL'}")
print(f"Response: {response.json()}\n")

# Test 3: Get current admin
print("TEST 3: GET /api/auth/me")
print("-" * 80)
response = session.get(f"{API_BASE}/auth/me")
print(f"Status: {response.status_code} - {'✅ PASS' if response.status_code == 200 else '❌ FAIL'}")
print(f"Response: {response.json()}\n")

# Test 4: Create opportunity
print("TEST 4: POST /api/opportunities")
print("-" * 80)
opp_data = {
    "name": "Test Internship",
    "duration": "3 months",
    "start_date": "2025-06-01",
    "description": "Test opportunity description",
    "skills_text": "Python, JavaScript, React",
    "category": "Technology",
    "future_opportunities": "High potential for full-time conversion",
    "max_applicants": 50
}
response = session.post(f"{API_BASE}/opportunities", json=opp_data)
print(f"Status: {response.status_code} - {'✅ PASS' if response.status_code == 201 else '❌ FAIL'}")
resp_json = response.json()
print(f"Response: {json.dumps(resp_json, indent=2)}\n")

# Extract opportunity ID
opp_id = resp_json.get('opportunity', {}).get('id')
print(f"Opportunity ID: {opp_id}\n")

# Test 5: GET single opportunity
print("TEST 5: GET /api/opportunities/<id>")
print("-" * 80)
response = session.get(f"{API_BASE}/opportunities/{opp_id}")
print(f"Status: {response.status_code} - {'✅ PASS' if response.status_code == 200 else '❌ FAIL'}")
print(f"Response: {json.dumps(response.json(), indent=2)}\n")

# Test 6: PUT update opportunity
print("TEST 6: PUT /api/opportunities/<id> (⭐ FIXED)")
print("-" * 80)
update_data = {
    "name": "Updated Test Internship",
    "duration": "4 months",
    "start_date": "2025-06-15",
    "description": "Updated opportunity description",
    "skills_text": "Python, JavaScript, React, Docker",
    "category": "Technology",
    "future_opportunities": "Guaranteed full-time offer",
    "max_applicants": 30
}
response = session.put(f"{API_BASE}/opportunities/{opp_id}", json=update_data)
print(f"Status: {response.status_code} - {'✅ PASS (FIXED!)' if response.status_code == 200 else '❌ FAIL'}")
print(f"Response: {json.dumps(response.json(), indent=2)}\n")

# Test 7: DELETE opportunity
print("TEST 7: DELETE /api/opportunities/<id> (⭐ FIXED)")
print("-" * 80)
response = session.delete(f"{API_BASE}/opportunities/{opp_id}")
print(f"Status: {response.status_code} - {'✅ PASS (FIXED!)' if response.status_code == 200 else '❌ FAIL'}")
print(f"Response: {json.dumps(response.json(), indent=2)}\n")

# Test 8: Logout
print("TEST 8: POST /api/auth/logout")
print("-" * 80)
response = session.post(f"{API_BASE}/auth/logout")
print(f"Status: {response.status_code} - {'✅ PASS' if response.status_code == 200 else '❌ FAIL'}")
print(f"Response: {json.dumps(response.json(), indent=2)}\n")

# Test 9: Forgot password
print("TEST 9: POST /api/auth/forgot-password")
print("-" * 80)
forgot_data = {"email": "testuser@example.com"}
response = session.post(f"{API_BASE}/auth/forgot-password", json=forgot_data)
print(f"Status: {response.status_code} - {'✅ PASS' if response.status_code == 200 else '❌ FAIL'}")
resp_json = response.json()
print(f"Response: {json.dumps(resp_json, indent=2)}")
expected_msg = "If an account exists for that email, a password reset link has been sent"
print(f"Message Check: {'✅ CORRECT' if resp_json.get('message') == expected_msg else '❌ WRONG'}\n")

print("="*80)
print("TESTING COMPLETE")
print("="*80 + "\n")
