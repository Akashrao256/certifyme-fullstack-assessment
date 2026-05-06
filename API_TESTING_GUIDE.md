# API Testing Guide

## Quick Setup

1. Start backend:

```powershell
cd backend
C:\Users\AKASH\AppData\Local\Programs\Python\Python313\python.exe app.py
```

2. Start frontend:

```powershell
cd frontend
C:\Users\AKASH\AppData\Local\Programs\Python\Python313\python.exe -m http.server 8000
```

3. Open browser: `http://localhost:8000`

---

## Testing with curl or Postman

### 1. Signup

```bash
POST http://localhost:5000/api/auth/signup
Content-Type: application/json

{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "confirm_password": "SecurePass123!"
}
```

**Expected Response:** 201 Created

```json
{
  "message": "Account created successfully",
  "admin": {
    "id": 1,
    "full_name": "John Doe",
    "email": "john@example.com"
  }
}
```

---

### 2. Login

```bash
POST http://localhost:5000/api/auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "SecurePass123!",
  "remember_me": false
}
```

**Expected Response:** 200 OK (Cookie set automatically)

```json
{
  "message": "Login successful",
  "admin": {
    "id": 1,
    "full_name": "John Doe",
    "email": "john@example.com"
  }
}
```

**Note:** Use `--cookie-jar cookies.txt` and `--cookie cookies.txt` with curl to maintain sessions, or enable credentials in Postman.

---

### 3. Get Current Admin

```bash
GET http://localhost:5000/api/auth/me
```

**Expected Response:** 200 OK

```json
{
  "admin": {
    "id": 1,
    "full_name": "John Doe",
    "email": "john@example.com"
  }
}
```

---

### 4. Create Opportunity

```bash
POST http://localhost:5000/api/opportunities
Content-Type: application/json

{
  "name": "Software Engineering Internship",
  "duration": "3 months",
  "start_date": "2025-06-01",
  "description": "Join our team as a software engineering intern",
  "skills_text": "Python, JavaScript, React, Flask",
  "category": "Technology",
  "future_opportunities": "High potential for full-time conversion",
  "max_applicants": 50
}
```

**Expected Response:** 201 Created

```json
{
  "message": "Opportunity created successfully",
  "opportunity": {
    "id": 1,
    "admin_id": 1,
    "name": "Software Engineering Internship",
    "duration": "3 months",
    "start_date": "2025-06-01",
    "description": "Join our team as a software engineering intern",
    "skills_text": "Python, JavaScript, React, Flask",
    "category": "Technology",
    "future_opportunities": "High potential for full-time conversion",
    "max_applicants": 50,
    "created_at": "2025-05-06 12:30:45"
  }
}
```

---

### 5. List All Opportunities

```bash
GET http://localhost:5000/api/opportunities
```

**Expected Response:** 200 OK

```json
{
  "opportunities": [
    {
      "id": 1,
      "admin_id": 1,
      "name": "Software Engineering Internship",
      ...all fields...
    }
  ]
}
```

---

### 6. Get Single Opportunity

```bash
GET http://localhost:5000/api/opportunities/1
```

**Expected Response:** 200 OK

```json
{
  "opportunity": {
    "id": 1,
    "admin_id": 1,
    "name": "Software Engineering Internship",
    ...all fields...
  }
}
```

---

### 7. Update Opportunity

```bash
PUT http://localhost:5000/api/opportunities/1
Content-Type: application/json

{
  "name": "Senior Software Engineering Internship",
  "duration": "4 months",
  "start_date": "2025-06-15",
  "description": "Join our senior team as an engineering intern",
  "skills_text": "Python, JavaScript, React, Flask, Docker",
  "category": "Technology",
  "future_opportunities": "Guaranteed full-time offer",
  "max_applicants": 30
}
```

**Expected Response:** 200 OK

```json
{
  "message": "Opportunity updated successfully",
  "opportunity": {
    "id": 1,
    "admin_id": 1,
    "name": "Senior Software Engineering Internship",
    ...updated fields...
  }
}
```

---

### 8. Delete Opportunity

```bash
DELETE http://localhost:5000/api/opportunities/1
```

**Expected Response:** 200 OK

```json
{
  "message": "Opportunity deleted successfully"
}
```

---

### 9. Forgot Password

```bash
POST http://localhost:5000/api/auth/forgot-password
Content-Type: application/json

{
  "email": "john@example.com"
}
```

**Expected Response:** 200 OK

```json
{
  "message": "If an account exists for that email, a password reset link has been sent"
}
```

**Note:** This endpoint returns the same message whether the email exists or not (security best practice).

---

### 10. Logout

```bash
POST http://localhost:5000/api/logout
```

**Expected Response:** 200 OK

```json
{
  "message": "Logged out successfully"
}
```

---

## Error Responses

### Invalid Email Format

```bash
POST http://localhost:5000/api/auth/signup
{
  "full_name": "John",
  "email": "not-an-email",
  "password": "SecurePass123!",
  "confirm_password": "SecurePass123!"
}
```

**Response:** 400 Bad Request

```json
{
  "message": "Invalid email format"
}
```

---

### Password Too Short

```bash
POST http://localhost:5000/api/auth/signup
{
  "full_name": "John",
  "email": "john@example.com",
  "password": "short",
  "confirm_password": "short"
}
```

**Response:** 400 Bad Request

```json
{
  "message": "Password must be at least 8 characters long"
}
```

---

### Passwords Don't Match

```bash
POST http://localhost:5000/api/auth/signup
{
  "full_name": "John",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "confirm_password": "DifferentPass123!"
}
```

**Response:** 400 Bad Request

```json
{
  "message": "Passwords do not match"
}
```

---

### Duplicate Email

```bash
POST http://localhost:5000/api/auth/signup
{
  "full_name": "Jane Doe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "confirm_password": "SecurePass123!"
}
```

**Response:** 409 Conflict

```json
{
  "message": "Account already exists"
}
```

---

### Invalid Login Credentials

```bash
POST http://localhost:5000/api/auth/login
{
  "email": "john@example.com",
  "password": "WrongPassword123!"
}
```

**Response:** 401 Unauthorized

```json
{
  "message": "Invalid email or password"
}
```

---

### Unauthorized Access

```bash
GET http://localhost:5000/api/opportunities
(without being logged in)
```

**Response:** 401 Unauthorized

```json
{
  "message": "Unauthorized"
}
```

---

### Opportunity Not Found

```bash
GET http://localhost:5000/api/opportunities/999
(or trying to access another user's opportunity)
```

**Response:** 404 Not Found

```json
{
  "message": "Opportunity not found"
}
```

---

## Postman Collection Setup

### Import the following as environment variables:

- `base_url`: `http://localhost:5000`
- `api_base`: `{{base_url}}/api`

### Headers for all requests:

```
Content-Type: application/json
```

### Pre-request Script (for authenticated endpoints):

- Enable "Send cookies" in Settings
- Login first to set session cookie
- All subsequent requests will include the session

---

## Key Testing Points

✅ Test all validation (email format, password length, match)
✅ Test data isolation (admin 1 can't see admin 2's opportunities)
✅ Test 404 for non-existent resources
✅ Test 401 without authentication
✅ Test all CRUD operations
✅ Verify database persistence
✅ Test forgot password (should not reveal if email exists)
