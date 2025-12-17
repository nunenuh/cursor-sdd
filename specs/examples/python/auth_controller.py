"""
Authentication Controller - Python Example (FastAPI)

This is an EXAMPLE implementation based on the User Authentication feature spec.
Customize this for your framework (FastAPI, Flask, Django, etc.).

Spec Reference: specs/features/example-feature.md
API Contract: specs/api/openapi.yaml
"""

from fastapi import APIRouter, Request, HTTPException, status
from pydantic import BaseModel
from .auth_login_service import AuthService, LoginRequest, LoginResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="Login with credentials",
    description="Authenticate user with username/password",
    responses={
        200: {
            "description": "Login successful",
            "content": {
                "application/json": {
                    "example": {
                        "success": True,
                        "data": {
                            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                            "expiresAt": "2025-01-17T12:00:00Z",
                            "user": {
                                "id": "user_123abc",
                                "username": "alice",
                                "email": "alice@example.com"
                            }
                        },
                        "error": None
                    }
                }
            }
        },
        401: {
            "description": "Invalid credentials",
            "content": {
                "application/json": {
                    "example": {
                        "success": False,
                        "data": None,
                        "error": {
                            "code": "INVALID_CREDENTIALS",
                            "message": "Invalid username or password"
                        }
                    }
                }
            }
        },
        429: {
            "description": "Too many requests",
            "content": {
                "application/json": {
                    "example": {
                        "success": False,
                        "data": None,
                        "error": {
                            "code": "RATE_LIMIT_EXCEEDED",
                            "message": "Too many login attempts"
                        }
                    }
                }
            }
        }
    }
)
async def login(
    request: LoginRequest,
    http_request: Request
) -> LoginResponse:
    """
    POST /auth/login
    
    Implements: specs/features/example-feature.md
    API Contract: specs/api/openapi.yaml#/paths/~1auth~1login
    
    Request Example: specs/examples/requests/login-request.json
    Response Example: specs/examples/responses/login-success.json
    """
    # Get client IP for rate limiting
    ip_address = http_request.client.host if http_request.client else "unknown"
    
    # Initialize service (in production, use dependency injection)
    auth_service = AuthService(
        user_repository=None,  # Inject your repository
        token_service=None,     # Inject your token service
        rate_limiter=None       # Inject your rate limiter
    )
    
    result = await auth_service.login(request, ip_address)
    
    if not result.success:
        # Map error codes to HTTP status codes
        status_code = _map_error_to_status_code(result.error.get("code") if result.error else "UNKNOWN")
        raise HTTPException(status_code=status_code, detail=result.error)
    
    return result


def _map_error_to_status_code(error_code: str) -> int:
    """Map error codes to HTTP status codes"""
    error_map = {
        "VALIDATION_ERROR": status.HTTP_400_BAD_REQUEST,
        "INVALID_CREDENTIALS": status.HTTP_401_UNAUTHORIZED,
        "ACCOUNT_LOCKED": status.HTTP_423_LOCKED,
        "RATE_LIMIT_EXCEEDED": status.HTTP_429_TOO_MANY_REQUESTS,
        "UNAUTHORIZED": status.HTTP_401_UNAUTHORIZED,
        "FORBIDDEN": status.HTTP_403_FORBIDDEN,
        "NOT_FOUND": status.HTTP_404_NOT_FOUND,
    }
    return error_map.get(error_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

