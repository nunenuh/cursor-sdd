"""
User Model - Python Example

This is an EXAMPLE data model based on the User schema specification.
Customize this for your ORM/framework (SQLAlchemy, Django ORM, Pydantic, etc.).

Spec Reference: specs/components/models/user.yaml
Database Schema: specs/schemas/database-schema.md
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, String, DateTime, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Pydantic models for API (matching OpenAPI schema)
class User(BaseModel):
    """
    User model matching OpenAPI User schema.
    
    Reference: specs/components/models/user.yaml
    """
    id: str
    username: str
    email: EmailStr
    name: Optional[str] = None
    createdAt: datetime
    updatedAt: datetime
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "user_123abc",
                "username": "alice",
                "email": "alice@example.com",
                "name": "Alice Smith",
                "createdAt": "2025-01-01T00:00:00Z",
                "updatedAt": "2025-01-16T12:00:00Z"
            }
        }


class UserCreate(BaseModel):
    """User creation input"""
    username: str
    email: EmailStr
    password: str
    name: Optional[str] = None


class UserUpdate(BaseModel):
    """User update input"""
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    name: Optional[str] = None


# SQLAlchemy model for database
class UserEntity(Base):
    """
    User database entity.
    
    Implements: specs/schemas/database-schema.md
    Table: users
    """
    __tablename__ = "users"
    
    id = Column(String, primary_key=True)
    username = Column(String(255), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=True)
    password_hash = Column(String(255), nullable=False)
    is_locked = Column(Boolean, default=False, nullable=False)
    failed_attempts = Column(Integer, default=0, nullable=False)
    locked_until = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_pydantic(self) -> User:
        """Convert SQLAlchemy entity to Pydantic model"""
        return User(
            id=self.id,
            username=self.username,
            email=self.email,
            name=self.name,
            createdAt=self.created_at,
            updatedAt=self.updated_at
        )


# Example: Django Model (if using Django)
"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    password_hash = models.CharField(max_length=255)
    is_locked = models.BooleanField(default=False)
    failed_attempts = models.IntegerField(default=0)
    locked_until = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
"""

