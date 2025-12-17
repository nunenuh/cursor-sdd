# API Contract

**Created:** 2025-01-16T12:00:00Z UTC  
**Modified:** 2025-01-16T12:00:00Z UTC

**⚠️ EXAMPLE:** This is an example API contract. Replace with your actual API contract.

Complete API contract documentation for the project.

---

## Overview

This document provides a human-readable overview of the API contract. For the machine-readable specification, see `../api/openapi.yaml`.

---

## Base URL

- **Development:** `http://localhost:3000`
- **Production:** `https://api.example.com`

---

## Authentication

### Bearer Token Authentication

Most endpoints require authentication using a Bearer token in the Authorization header:

```
Authorization: Bearer <token>
```

Tokens are obtained through the `/auth/login` endpoint.

---

## Endpoints

### Health Check

**GET** `/health`

Returns server health status.

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2025-01-16T12:00:00Z"
}
```

---

### Authentication

#### Login

**POST** `/auth/login`

Authenticate user with username and password.

**Request:**
```json
{
  "username": "alice",
  "password": "securePassword123"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "expiresAt": "2025-01-17T12:00:00Z"
  }
}
```

**Response (401):**
```json
{
  "success": false,
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Invalid username or password"
  }
}
```

---

### Users

#### List Users

**GET** `/users`

Get a paginated list of users.

**Query Parameters:**
- `page` (integer, default: 1) - Page number
- `limit` (integer, default: 20, max: 100) - Items per page

**Response:**
```json
{
  "data": [
    {
      "id": "user_123abc",
      "username": "alice",
      "email": "alice@example.com"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "totalPages": 5
  }
}
```

---

## Error Responses

All error responses follow this format:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {}
  }
}
```

### Common Error Codes

- `VALIDATION_ERROR` - Request validation failed
- `INVALID_CREDENTIALS` - Authentication failed
- `NOT_FOUND` - Resource not found
- `UNAUTHORIZED` - Authentication required
- `FORBIDDEN` - Insufficient permissions
- `RATE_LIMIT_EXCEEDED` - Too many requests

---

## Related

- **OpenAPI Spec:** `../api/openapi.yaml` - Machine-readable specification
- **Examples:** `../examples/` - Request/response examples
- **Components:** `../components/` - Reusable components

---

**Note:** This is a human-readable summary. Always refer to `openapi.yaml` for the complete, machine-readable contract.
