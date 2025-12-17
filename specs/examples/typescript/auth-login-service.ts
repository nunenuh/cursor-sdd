/**
 * Authentication Login Service - TypeScript Example
 * 
 * This is an EXAMPLE implementation based on the User Authentication feature spec.
 * Customize this for your project's needs.
 * 
 * Spec Reference: specs/features/example-feature.md
 * API Contract: specs/api/openapi.yaml
 */

import { UserRepository } from './user-repository';
import { TokenService } from './token-service';
import { PasswordService } from './password-service';

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  success: boolean;
  data: {
    token: string;
    expiresAt: string;
    user: {
      id: string;
      username: string;
      email: string;
    };
  } | null;
  error: {
    code: string;
    message: string;
  } | null;
}

export class AuthService {
  constructor(
    private userRepository: UserRepository,
    private tokenService: TokenService,
    private passwordService: PasswordService
  ) {}

  /**
   * Login user with username and password
   * 
   * Implements: specs/features/example-feature.md
   * Endpoint: POST /auth/login
   * 
   * Constraints:
   * - Rate limit: 5 attempts per minute per IP
   * - Account lockout after 5 failed attempts
   * - Password hashed with bcrypt (cost factor 10)
   */
  async login(request: LoginRequest, ipAddress: string): Promise<LoginResponse> {
    try {
      // Validate input
      if (!request.username || !request.password) {
        return {
          success: false,
          data: null,
          error: {
            code: 'VALIDATION_ERROR',
            message: 'Username and password are required'
          }
        };
      }

      // Check rate limiting (constraint: 5 attempts per minute)
      const rateLimitExceeded = await this.checkRateLimit(ipAddress);
      if (rateLimitExceeded) {
        return {
          success: false,
          data: null,
          error: {
            code: 'RATE_LIMIT_EXCEEDED',
            message: 'Too many login attempts. Please try again later.'
          }
        };
      }

      // Find user
      const user = await this.userRepository.findByUsername(request.username);
      if (!user) {
        await this.recordFailedAttempt(request.username, ipAddress);
        return {
          success: false,
          data: null,
          error: {
            code: 'INVALID_CREDENTIALS',
            message: 'Invalid username or password'
          }
        };
      }

      // Check if account is locked (constraint: lock after 5 failed attempts)
      if (user.isLocked) {
        return {
          success: false,
          data: null,
          error: {
            code: 'ACCOUNT_LOCKED',
            message: 'Account is locked due to too many failed attempts'
          }
        };
      }

      // Verify password (constraint: bcrypt with cost factor 10)
      const passwordValid = await this.passwordService.verify(
        request.password,
        user.passwordHash
      );

      if (!passwordValid) {
        await this.recordFailedAttempt(request.username, ipAddress);
        return {
          success: false,
          data: null,
          error: {
            code: 'INVALID_CREDENTIALS',
            message: 'Invalid username or password'
          }
        };
      }

      // Generate token (constraint: JWT with HS256, expires in 24 hours)
      const token = await this.tokenService.generateToken({
        userId: user.id,
        username: user.username
      });

      const expiresAt = new Date();
      expiresAt.setHours(expiresAt.getHours() + 24); // 24 hours expiration

      // Return success response
      return {
        success: true,
        data: {
          token,
          expiresAt: expiresAt.toISOString(),
          user: {
            id: user.id,
            username: user.username,
            email: user.email
          }
        },
        error: null
      };
    } catch (error) {
      return {
        success: false,
        data: null,
        error: {
          code: 'INTERNAL_ERROR',
          message: 'An error occurred during login'
        }
      };
    }
  }

  private async checkRateLimit(ipAddress: string): Promise<boolean> {
    // Implementation: Check rate limit (5 attempts per minute)
    // This is an example - implement based on your infrastructure
    return false;
  }

  private async recordFailedAttempt(username: string, ipAddress: string): Promise<void> {
    // Implementation: Record failed attempt and check for lockout
    // This is an example - implement based on your requirements
  }
}

