/**
 * Authentication Controller - TypeScript Example
 * 
 * This is an EXAMPLE implementation based on the User Authentication feature spec.
 * Customize this for your framework (Express, Fastify, etc.).
 * 
 * Spec Reference: specs/features/example-feature.md
 * API Contract: specs/api/openapi.yaml
 */

import { Request, Response } from 'express';
import { AuthService, LoginRequest } from './auth-login-service';

export class AuthController {
  constructor(private authService: AuthService) {}

  /**
   * POST /auth/login
   * 
   * Implements: specs/features/example-feature.md
   * API Contract: specs/api/openapi.yaml#/paths/~1auth~1login
   * 
   * Request Example: specs/examples/requests/login-request.json
   * Response Example: specs/examples/responses/login-success.json
   */
  async login(req: Request, res: Response): Promise<void> {
    try {
      const request: LoginRequest = {
        username: req.body.username,
        password: req.body.password
      };

      // Get client IP for rate limiting
      const ipAddress = req.ip || req.socket.remoteAddress || 'unknown';

      const result = await this.authService.login(request, ipAddress);

      if (result.success) {
        res.status(200).json(result);
      } else {
        // Map error codes to HTTP status codes
        const statusCode = this.mapErrorToStatusCode(result.error?.code || 'UNKNOWN');
        res.status(statusCode).json(result);
      }
    } catch (error) {
      res.status(500).json({
        success: false,
        data: null,
        error: {
          code: 'INTERNAL_ERROR',
          message: 'An error occurred processing your request'
        }
      });
    }
  }

  private mapErrorToStatusCode(errorCode: string): number {
    const errorMap: Record<string, number> = {
      'VALIDATION_ERROR': 400,
      'INVALID_CREDENTIALS': 401,
      'ACCOUNT_LOCKED': 423,
      'RATE_LIMIT_EXCEEDED': 429,
      'UNAUTHORIZED': 401,
      'FORBIDDEN': 403,
      'NOT_FOUND': 404
    };

    return errorMap[errorCode] || 500;
  }
}

