/**
 * User Model - TypeScript Example
 * 
 * This is an EXAMPLE data model based on the User schema specification.
 * Customize this for your ORM/framework (TypeORM, Prisma, Sequelize, etc.).
 * 
 * Spec Reference: specs/components/models/user.yaml
 * Database Schema: specs/schemas/database-schema.md
 */

/**
 * User entity matching the OpenAPI User schema
 * 
 * Reference: specs/components/models/user.yaml
 */
export interface User {
  id: string;
  username: string;
  email: string;
  name?: string | null;
  createdAt: string; // ISO 8601 date-time
  updatedAt: string; // ISO 8601 date-time
}

/**
 * User entity with password hash (internal use only)
 * Never expose passwordHash in API responses
 */
export interface UserWithPassword extends User {
  passwordHash: string;
  isLocked: boolean;
  failedAttempts: number;
  lockedUntil?: Date | null;
}

/**
 * User creation input
 */
export interface CreateUserInput {
  username: string;
  email: string;
  password: string;
  name?: string;
}

/**
 * User update input
 */
export interface UpdateUserInput {
  username?: string;
  email?: string;
  name?: string;
}

/**
 * Example: TypeORM Entity (if using TypeORM)
 * 
 * Uncomment and customize if using TypeORM:
 */
/*
import { Entity, Column, PrimaryGeneratedColumn, CreateDateColumn, UpdateDateColumn } from 'typeorm';

@Entity('users')
export class UserEntity {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column({ unique: true })
  username: string;

  @Column({ unique: true })
  email: string;

  @Column({ nullable: true })
  name: string | null;

  @Column()
  passwordHash: string;

  @Column({ default: false })
  isLocked: boolean;

  @Column({ default: 0 })
  failedAttempts: number;

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;
}
*/

/**
 * Example: Prisma Schema (if using Prisma)
 * 
 * Add to schema.prisma:
 * 
 * model User {
 *   id          String   @id @default(uuid())
 *   username    String   @unique
 *   email       String   @unique
 *   name        String?
 *   passwordHash String
 *   isLocked    Boolean  @default(false)
 *   failedAttempts Int    @default(0)
 *   createdAt   DateTime @default(now())
 *   updatedAt   DateTime @updatedAt
 * }
 */

