"""
Authentication Login Service - Python Example

This is an EXAMPLE implementation based on the User Authentication feature spec.
Customize this for your project's needs.

Spec Reference: specs/features/example-feature.md
API Contract: specs/api/openapi.yaml
"""

from datetime import datetime, timedelta
from typing import Optional
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

# Password hashing context (constraint: bcrypt with cost factor 10)
pwd_context = CryptContext(schemes=["bcrypt"], bcrypt__rounds=10)


class LoginRequest(BaseModel):
    """Login request model matching API contract"""
    username: str
    password: str


class LoginResponse(BaseModel):
    """Login response model matching API contract"""
    success: bool
    data: Optional[dict] = None
    error: Optional[dict] = None


class AuthService:
    """
    Authentication service implementing login functionality.
    
    Implements: specs/features/example-feature.md
    Endpoint: POST /auth/login
    
    Constraints:
    - Rate limit: 5 attempts per minute per IP
    - Account lockout after 5 failed attempts
    - Password hashed with bcrypt (cost factor 10)
    - JWT token with HS256, expires in 24 hours
    """
    
    def __init__(self, user_repository, token_service, rate_limiter):
        self.user_repository = user_repository
        self.token_service = token_service
        self.rate_limiter = rate_limiter
    
    async def login(
        self, 
        request: LoginRequest, 
        ip_address: str
    ) -> LoginResponse:
        """
        Login user with username and password.
        
        Returns LoginResponse matching specs/examples/responses/login-success.json
        """
        try:
            # Validate input
            if not request.username or not request.password:
                return LoginResponse(
                    success=False,
                    data=None,
                    error={
                        "code": "VALIDATION_ERROR",
                        "message": "Username and password are required"
                    }
                )
            
            # Check rate limiting (constraint: 5 attempts per minute)
            if await self.rate_limiter.is_rate_limited(ip_address):
                return LoginResponse(
                    success=False,
                    data=None,
                    error={
                        "code": "RATE_LIMIT_EXCEEDED",
                        "message": "Too many login attempts. Please try again later."
                    }
                )
            
            # Find user
            user = await self.user_repository.find_by_username(request.username)
            if not user:
                await self._record_failed_attempt(request.username, ip_address)
                return LoginResponse(
                    success=False,
                    data=None,
                    error={
                        "code": "INVALID_CREDENTIALS",
                        "message": "Invalid username or password"
                    }
                )
            
            # Check if account is locked (constraint: lock after 5 failed attempts)
            if user.is_locked:
                return LoginResponse(
                    success=False,
                    data=None,
                    error={
                        "code": "ACCOUNT_LOCKED",
                        "message": "Account is locked due to too many failed attempts"
                    }
                )
            
            # Verify password (constraint: bcrypt with cost factor 10)
            if not pwd_context.verify(request.password, user.password_hash):
                await self._record_failed_attempt(request.username, ip_address)
                return LoginResponse(
                    success=False,
                    data=None,
                    error={
                        "code": "INVALID_CREDENTIALS",
                        "message": "Invalid username or password"
                    }
                )
            
            # Generate token (constraint: JWT with HS256, expires in 24 hours)
            token = await self.token_service.generate_token(
                user_id=user.id,
                username=user.username
            )
            
            expires_at = datetime.utcnow() + timedelta(hours=24)
            
            # Return success response matching specs/examples/responses/login-success.json
            return LoginResponse(
                success=True,
                data={
                    "token": token,
                    "expiresAt": expires_at.isoformat() + "Z",
                    "user": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    }
                },
                error=None
            )
            
        except Exception as e:
            return LoginResponse(
                success=False,
                data=None,
                error={
                    "code": "INTERNAL_ERROR",
                    "message": "An error occurred during login"
                }
            )
    
    async def _record_failed_attempt(self, username: str, ip_address: str):
        """Record failed login attempt and check for lockout"""
        # Implementation: Record failed attempt and check for lockout
        # This is an example - implement based on your requirements
        pass

