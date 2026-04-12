# Better Auth

Better Auth is a comprehensive, framework-agnostic authentication and authorization library for TypeScript that provides enterprise-grade features through a flexible plugin architecture. It handles everything from basic email/password authentication to advanced features like multi-tenancy, two-factor authentication, passkeys, WebAuthn, phone authentication, username authentication, anonymous sessions, API keys, JWT tokens, Sign-In with Ethereum (SIWE), OAuth proxy, CAPTCHA protection, and SSO. The library supports multiple database adapters (Prisma, Drizzle, MongoDB, Kysely), integrates seamlessly with popular frameworks (Next.js, SvelteKit, Solid Start, React Start), and provides type-safe client libraries for React, Vue, Svelte, Solid, and Lynx.

The architecture centers around a server-side `betterAuth()` instance that handles authentication logic and exposes REST API endpoints, paired with framework-specific client libraries that provide type-safe methods and hooks for managing authentication state. Plugins extend functionality by adding endpoints, database schemas, hooks, and middleware, enabling complex features like organizations, two-factor authentication, passkey support, phone number authentication, username authentication, anonymous sessions, bearer tokens, access control, multi-session support, device authorization, and OpenID Connect provider capabilities with minimal configuration. The system is designed for production use with built-in rate limiting, CSRF protection, secure cookie handling, password breach checking via HaveIBeenPwned integration, and comprehensive error handling.

## Initialize Server Authentication

Creates a Better Auth server instance with database, social providers, and plugins.

```typescript
import { betterAuth } from 'better-auth';
import { drizzleAdapter } from 'better-auth/adapters/drizzle';
import { organization, twoFactor, passkey } from 'better-auth/plugins';
import { db } from './db';

export const auth = betterAuth({
  appName: 'My Application',
  baseURL: process.env.BETTER_AUTH_URL || 'http://localhost:3000',
  secret: process.env.BETTER_AUTH_SECRET,

  database: drizzleAdapter(db, {
    provider: 'pg',
    schema: schema,
  }),

  emailAndPassword: {
    enabled: true,
    minPasswordLength: 8,
    async sendResetPassword({ user, url, token }) {
      await sendEmail({
        to: user.email,
        subject: 'Reset your password',
        html: `Click <a href="${url}">here</a> to reset your password`,
      });
    },
  },

  emailVerification: {
    async sendVerificationEmail({ user, url, token }) {
      await sendEmail({
        to: user.email,
        subject: 'Verify your email',
        html: `Click <a href="${url}">here</a> to verify`,
      });
    },
    sendOnSignUp: true,
    autoSignInAfterVerification: true,
  },

  socialProviders: {
    github: {
      clientId: process.env.GITHUB_CLIENT_ID!,
      clientSecret: process.env.GITHUB_CLIENT_SECRET!,
    },
    google: {
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
      accessType: 'offline',
    },
  },

  session: {
    expiresIn: 60 * 60 * 24 * 7, // 7 days
    updateAge: 60 * 60 * 24, // 1 day
    freshAge: 60 * 10, // 10 minutes
  },

  rateLimit: {
    enabled: true,
    window: 60,
    max: 10,
  },

  plugins: [
    organization(),
    twoFactor({
      issuer: 'My App',
    }),
    passkey(),
  ],
});

export type Session = typeof auth.$Infer.Session;
```

## Create Authentication API Routes

Exposes Better Auth REST endpoints in your application framework.

```typescript
// Next.js App Router: app/api/auth/[...all]/route.ts
import { auth } from '@/lib/auth';
import { toNextJsHandler } from 'better-auth/next-js';

export const { GET, POST } = toNextJsHandler(auth);

// SvelteKit: src/routes/api/auth/[...all]/+server.ts
import { auth } from '$lib/auth';
import { svelteKitHandler } from 'better-auth/svelte-kit';

export const { GET, POST } = svelteKitHandler(auth);

// Solid Start: src/routes/api/auth/[...all].ts
import { auth } from '~/lib/auth';
import { solidStartHandler } from 'better-auth/solid-start';

export const { GET, POST } = solidStartHandler(auth);

// React Start (TanStack Start)
import { auth } from '~/lib/auth';
import { reactStartHandler } from 'better-auth/react-start';

export const { GET, POST } = reactStartHandler(auth);

// Express.js
import express from 'express';
import { auth } from './auth';

const app = express();

app.all('/api/auth/*', async (req, res) => {
  return auth
    .handler(
      new Request(`${req.protocol}://${req.get('host')}${req.originalUrl}`, {
        method: req.method,
        headers: req.headers as HeadersInit,
        body: req.method !== 'GET' ? JSON.stringify(req.body) : undefined,
      })
    )
    .then(response => {
      res.status(response.status);
      response.headers.forEach((value, key) => res.setHeader(key, value));
      return response.text().then(body => res.send(body));
    });
});
```

## Initialize Client SDK

Creates a type-safe client for authentication operations with framework-specific hooks.

```typescript
// React Client
import { createAuthClient } from 'better-auth/react';
import {
  organizationClient,
  twoFactorClient,
  passkeyClient,
} from 'better-auth/client/plugins';

export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_APP_URL,

  plugins: [
    organizationClient(),
    twoFactorClient({
      twoFactorPage: '/two-factor',
      onTwoFactorRedirect() {
        window.location.href = '/two-factor';
      },
    }),
    passkeyClient(),
  ],

  fetchOptions: {
    onError(error) {
      if (error.error.status === 429) {
        toast.error('Too many requests. Please try again later.');
      } else if (error.error.status === 401) {
        console.error('Unauthorized');
      }
    },
    onSuccess(data) {
      console.log('Auth action successful:', data);
    },
  },
});

export const {
  signIn,
  signUp,
  signOut,
  useSession,
  organization,
  twoFactor,
  passkey,
} = authClient;

// Vue Client
import { createAuthClient } from 'better-auth/vue';
export const authClient = createAuthClient({
  /* config */
});

// Svelte Client
import { createAuthClient } from 'better-auth/svelte';
export const authClient = createAuthClient({
  /* config */
});

// Solid Client
import { createAuthClient } from 'better-auth/solid';
export const authClient = createAuthClient({
  /* config */
});

// Lynx Client
import { createAuthClient } from 'better-auth/lynx';
export const authClient = createAuthClient({
  /* config */
});
```

## User Registration and Sign In

Handles email/password authentication with validation and session management.

```typescript
import { authClient } from './auth-client';

// Email/Password Sign Up
try {
  const { data, error } = await authClient.signUp.email({
    name: 'John Doe',
    email: 'john@example.com',
    password: 'SecurePassword123!',
    image: 'https://example.com/avatar.jpg', // optional
    callbackURL: '/dashboard', // redirect after sign up
  });

  if (error) {
    console.error('Sign up failed:', error.message);
    return;
  }

  console.log('User created:', data.user);
  console.log('Session created:', data.session);
} catch (err) {
  console.error('Unexpected error:', err);
}

// Email/Password Sign In
const { data, error } = await authClient.signIn.email({
  email: 'john@example.com',
  password: 'SecurePassword123!',
  rememberMe: true, // extends session duration
  callbackURL: '/dashboard',
});

// Sign Out
await authClient.signOut({
  fetchOptions: {
    onSuccess() {
      window.location.href = '/';
    },
  },
});

// Sign Out from All Devices
await authClient.signOut({
  revokeAllSessions: true,
});
```

## Social OAuth Authentication

Initiates OAuth flows with third-party providers for passwordless sign-in.

```typescript
import { authClient } from './auth-client';

// GitHub OAuth Sign In
await authClient.signIn.social({
  provider: 'github',
  callbackURL: '/dashboard',
});

// Google OAuth Sign In
await authClient.signIn.social({
  provider: 'google',
  callbackURL: '/dashboard',
});

// Discord, Microsoft, Apple, etc.
await authClient.signIn.social({
  provider: 'discord',
  callbackURL: '/dashboard',
});

// Link Additional Social Account
await authClient.linkSocial({
  provider: 'github',
  callbackURL: '/settings/accounts',
});

// Unlink Social Account
await authClient.unlinkAccount({
  accountId: 'acc_123456',
});

// List All Linked Accounts
const { data } = await authClient.listAccounts();
data?.forEach(account => {
  console.log(`${account.provider}: ${account.providerId}`);
});
```

## Session Management with Hooks

Retrieves and monitors authentication state in React components.

```typescript
"use client";

import { useSession } from "./auth-client";
import { Loader } from "./components/loader";

export function ProfilePage() {
  const { data: session, isPending, error } = useSession();

  if (isPending) {
    return <Loader />;
  }

  if (error) {
    return <div>Error loading session: {error.message}</div>;
  }

  if (!session) {
    return <div>Not authenticated. Please sign in.</div>;
  }

  return (
    <div>
      <h1>Welcome, {session.user.name}!</h1>
      <p>Email: {session.user.email}</p>
      <p>Email verified: {session.user.emailVerified ? "Yes" : "No"}</p>
      <img src={session.user.image} alt="Profile" />

      <div>
        <h2>Session Info</h2>
        <p>Session ID: {session.session.id}</p>
        <p>Expires: {new Date(session.session.expiresAt).toLocaleString()}</p>
        <p>IP Address: {session.session.ipAddress}</p>
        <p>User Agent: {session.session.userAgent}</p>
      </div>
    </div>
  );
}

// Update User Profile
import { authClient } from "./auth-client";

async function updateProfile() {
  const { data, error } = await authClient.updateUser({
    name: "John Smith",
    image: "https://example.com/new-avatar.jpg",
  });

  if (!error) {
    console.log("Profile updated:", data);
  }
}

// Change Email
await authClient.changeEmail({
  newEmail: "newemail@example.com",
  callbackURL: "/verify-new-email",
});

// Change Password
await authClient.changePassword({
  currentPassword: "OldPassword123!",
  newPassword: "NewPassword456!",
  revokeOtherSessions: true,
});
```

## Server-Side Session Access

Validates sessions in server components, API routes, and middleware.

```typescript
// Next.js App Router Server Component
import { auth } from "@/lib/auth";
import { headers } from "next/headers";
import { redirect } from "next/navigation";

export default async function ProtectedPage() {
  const session = await auth.api.getSession({
    headers: await headers(),
  });

  if (!session) {
    redirect("/sign-in");
  }

  return (
    <div>
      <h1>Protected Content</h1>
      <p>Welcome, {session.user.name}!</p>
    </div>
  );
}

// Next.js API Route
import { auth } from "@/lib/auth";

export async function GET(req: Request) {
  const session = await auth.api.getSession({
    headers: req.headers,
  });

  if (!session) {
    return new Response("Unauthorized", { status: 401 });
  }

  // Perform authenticated operation
  const data = await fetchUserData(session.user.id);

  return Response.json({ data });
}

// SvelteKit Load Function
import { auth } from "$lib/auth";

export async function load({ request }) {
  const session = await auth.api.getSession({
    headers: request.headers,
  });

  if (!session) {
    throw redirect(302, "/sign-in");
  }

  return { session };
}

// Middleware for Route Protection
import { auth } from "@/lib/auth";

export async function middleware(request: Request) {
  const session = await auth.api.getSession({
    headers: request.headers,
  });

  const isProtectedRoute = request.url.includes("/dashboard");

  if (isProtectedRoute && !session) {
    return Response.redirect(new URL("/sign-in", request.url));
  }
}
```

## Database Adapter Configuration

Connects Better Auth to your database using various ORMs and drivers.

```typescript
// Drizzle ORM Adapter (PostgreSQL, MySQL, SQLite)
import { drizzleAdapter } from 'better-auth/adapters/drizzle';
import { drizzle } from 'drizzle-orm/postgres-js';
import postgres from 'postgres';
import * as schema from './schema';

const client = postgres(process.env.DATABASE_URL!);
const db = drizzle(client, { schema });

export const auth = betterAuth({
  database: drizzleAdapter(db, {
    provider: 'pg', // "pg" | "mysql" | "sqlite"
    schema: schema,
    usePlural: false, // Use singular table names
    camelCase: false, // Use snake_case column names
  }),
});

// Prisma Adapter
import { prismaAdapter } from 'better-auth/adapters/prisma';
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

export const auth = betterAuth({
  database: prismaAdapter(prisma, {
    provider: 'postgresql',
    usePlural: false,
  }),
});

// MongoDB Adapter
import { mongodbAdapter } from 'better-auth/adapters/mongodb';
import { MongoClient } from 'mongodb';

const mongoClient = new MongoClient(process.env.MONGODB_URL!);
await mongoClient.connect();

export const auth = betterAuth({
  database: mongodbAdapter(mongoClient.db('auth')),
});

// Kysely Adapter (SQL Query Builder)
import { kyselyAdapter } from 'better-auth/adapters/kysely';
import { Kysely, PostgresDialect } from 'kysely';
import { Pool } from 'pg';

const db = new Kysely({
  dialect: new PostgresDialect({
    pool: new Pool({
      connectionString: process.env.DATABASE_URL,
    }),
  }),
});

export const auth = betterAuth({
  database: kyselyAdapter(db),
});

// Memory Adapter (Testing Only)
import { memoryAdapter } from 'better-auth/adapters/memory';

export const auth = betterAuth({
  database: memoryAdapter(),
});
```

## Organization Plugin for Multi-Tenancy

Enables team/workspace management with roles, permissions, and invitations.

```typescript
import { betterAuth } from 'better-auth';
import { organization } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    organization({
      async sendInvitationEmail({ email, organization, inviter, url }) {
        await sendEmail({
          to: email,
          subject: `Join ${organization.name}`,
          html: `${inviter.user.name} invited you to join ${organization.name}. <a href="${url}">Accept invitation</a>`,
        });
      },

      allowUserToCreateOrganization: true,
      organizationLimit: 10,

      roles: {
        owner: ['create', 'read', 'update', 'delete', 'invite', 'remove'],
        admin: ['read', 'update', 'invite'],
        member: ['read'],
      },
    }),
  ],
});

// Client Usage
import { organizationClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [organizationClient()],
});

// Create Organization
const { data } = await authClient.organization.create({
  name: 'Acme Corporation',
  slug: 'acme-corp',
  logo: 'https://example.com/logo.png',
  metadata: { industry: 'Technology' },
});

// Invite Member
await authClient.organization.inviteMember({
  email: 'member@example.com',
  role: 'admin',
  organizationId: data.id,
});

// List Members
const { data: members } = await authClient.organization.listMembers({
  organizationId: 'org_123',
});

// Update Member Role
await authClient.organization.updateMemberRole({
  memberId: 'mem_456',
  role: 'owner',
  organizationId: 'org_123',
});

// Remove Member
await authClient.organization.removeMember({
  memberId: 'mem_456',
  organizationId: 'org_123',
});

// Set Active Organization
await authClient.organization.setActive({
  organizationId: 'org_123',
});

// Check Permissions
const hasPermission = await authClient.organization.hasPermission({
  permissions: {
    post: ['create', 'delete'],
    user: ['invite'],
  },
});
```

## Two-Factor Authentication Plugin

Adds TOTP authenticator apps, backup codes, and OTP support for enhanced security.

```typescript
import { betterAuth } from 'better-auth';
import { twoFactor } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    twoFactor({
      issuer: 'My Application',

      otpOptions: {
        async sendOTP({ user, otp }) {
          await sendEmail({
            to: user.email,
            subject: 'Your verification code',
            html: `Your code is: ${otp}`,
          });
        },

        period: 300, // 5 minutes
        length: 6,
      },

      backupCodeLength: 10,
      backupCodeCount: 10,
    }),
  ],
});

// Client Usage
import { twoFactorClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [
    twoFactorClient({
      twoFactorPage: '/two-factor',
      onTwoFactorRedirect() {
        router.push('/two-factor');
      },
    }),
  ],
});

// Enable 2FA
const { data } = await authClient.twoFactor.enable({
  password: 'userPassword123',
});

console.log('TOTP URI:', data.totpURI); // For QR code generation
console.log('Backup codes:', data.backupCodes);

// Verify TOTP Setup
await authClient.twoFactor.verifyTotp({
  code: '123456',
});

// Send OTP via Email
await authClient.twoFactor.sendOtp();

// Verify OTP
await authClient.twoFactor.verifyOtp({
  code: '123456',
});

// Use Backup Code
await authClient.twoFactor.useBackupCode({
  code: 'ABCD-1234-EFGH',
});

// Generate New Backup Codes
const { data: newCodes } = await authClient.twoFactor.regenerateBackupCodes({
  password: 'userPassword123',
});

// Disable 2FA
await authClient.twoFactor.disable({
  password: 'userPassword123',
});
```

## Passkey/WebAuthn Plugin

Implements passwordless authentication using biometric or hardware security keys.

```typescript
import { betterAuth } from 'better-auth';
import { passkey } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    passkey({
      rpName: 'My Application',
      rpID: 'example.com',
      origin: 'https://example.com',
    }),
  ],
});

// Client Usage
import { passkeyClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [passkeyClient()],
});

// Register Passkey (must be signed in)
try {
  const { data } = await authClient.passkey.addPasskey({
    name: 'MacBook Pro Touch ID',
  });

  console.log('Passkey registered:', data.id);
} catch (error) {
  console.error('Passkey registration failed:', error);
}

// Sign In with Passkey
await authClient.passkey.signIn({
  callbackURL: '/dashboard',
});

// List User Passkeys
const { data: passkeys } = await authClient.passkey.listPasskeys();

passkeys?.forEach(key => {
  console.log(`${key.name}: ${key.createdAt}`);
});

// Delete Passkey
await authClient.passkey.deletePasskey({
  id: 'passkey_123',
});

// Check Passkey Support
if (authClient.passkey.isSupported()) {
  console.log('Passkeys are supported in this browser');
}
```

## Magic Link Authentication Plugin

Sends one-time sign-in links via email for passwordless authentication.

```typescript
import { betterAuth } from 'better-auth';
import { magicLink } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    magicLink({
      async sendMagicLink({ email, url, token }) {
        await sendEmail({
          to: email,
          subject: 'Sign in to your account',
          html: `
            <h1>Sign in to My Application</h1>
            <p>Click the link below to sign in:</p>
            <a href="${url}">Sign in</a>
            <p>This link expires in 5 minutes.</p>
          `,
        });
      },

      expiresIn: 300, // 5 minutes
      disableSignUp: false,
    }),
  ],
});

// Client Usage
import { magicLinkClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [magicLinkClient()],
});

// Send Magic Link
const { data, error } = await authClient.magicLink.sendMagicLink({
  email: 'user@example.com',
  callbackURL: '/dashboard',
});

if (!error) {
  console.log('Magic link sent! Check your email.');
}

// The verification happens automatically when user clicks the link
// The URL will be: /api/auth/magic-link/verify?token=xxx
```

## Email OTP Plugin

Sends one-time password codes via email for verification and sign-in.

```typescript
import { betterAuth } from 'better-auth';
import { emailOTP } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    emailOTP({
      async sendVerificationOTP({ email, otp, type }) {
        await sendEmail({
          to: email,
          subject: type === 'sign-in' ? 'Sign in code' : 'Verification code',
          html: `Your verification code is: <strong>${otp}</strong>`,
        });
      },

      otpLength: 6,
      expiresIn: 300, // 5 minutes
      sendOnSignUp: true,
      disableSignUp: false,
    }),
  ],
});

// Client Usage
import { emailOTPClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [emailOTPClient()],
});

// Send OTP
await authClient.emailOTP.sendVerificationOtp({
  email: 'user@example.com',
  type: 'sign-in',
});

// Verify OTP
const { data, error } = await authClient.emailOTP.verifyEmail({
  email: 'user@example.com',
  otp: '123456',
});

if (!error) {
  console.log('Signed in successfully:', data.user);
}
```

## Phone Number Authentication Plugin

Enables phone number registration and SMS-based OTP verification.

```typescript
import { betterAuth } from 'better-auth';
import { phoneNumber } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    phoneNumber({
      async sendOTP({ phoneNumber, otp }) {
        await sendSMS({
          to: phoneNumber,
          message: `Your verification code is: ${otp}`,
        });
      },

      otpLength: 6,
      expiresIn: 300, // 5 minutes
    }),
  ],
});

// Client Usage
import { phoneNumberClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [phoneNumberClient()],
});

// Send Phone OTP
await authClient.phoneNumber.sendOtp({
  phoneNumber: '+1234567890',
});

// Verify Phone OTP and Sign In
const { data, error } = await authClient.phoneNumber.verifyOtp({
  phoneNumber: '+1234567890',
  otp: '123456',
});

if (!error) {
  console.log('Signed in with phone:', data.user);
}
```

## Username Authentication Plugin

Adds username-based authentication alongside email/password.

```typescript
import { betterAuth } from 'better-auth';
import { username } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    username({
      minLength: 3,
      maxLength: 20,
      allowedCharacters: /^[a-zA-Z0-9_-]+$/,
    }),
  ],
});

// Client Usage
import { usernameClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [usernameClient()],
});

// Sign Up with Username
await authClient.signUp.username({
  username: 'johndoe',
  password: 'SecurePassword123!',
  name: 'John Doe',
  email: 'john@example.com', // optional
});

// Sign In with Username
await authClient.signIn.username({
  username: 'johndoe',
  password: 'SecurePassword123!',
});
```

## Anonymous Authentication Plugin

Allows users to create temporary anonymous sessions without credentials.

```typescript
import { betterAuth } from 'better-auth';
import { anonymous } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    anonymous({
      sessionDuration: 60 * 60 * 24 * 30, // 30 days
    }),
  ],
});

// Client Usage
import { anonymousClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [anonymousClient()],
});

// Create Anonymous Session
const { data } = await authClient.anonymous.signIn();

console.log('Anonymous session:', data.session);

// Link Anonymous Account to Email
await authClient.anonymous.linkEmail({
  email: 'user@example.com',
  password: 'SecurePassword123!',
});
```

## Admin Plugin for User Management

Provides administrative endpoints for managing users, sessions, and system operations.

```typescript
import { betterAuth } from 'better-auth';
import { admin } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    admin({
      // Optional: customize admin role check
      async isAdmin(user) {
        return user.role === 'admin' || user.email.endsWith('@company.com');
      },
    }),
  ],
});

// Client Usage
import { adminClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [adminClient()],
});

// List All Users
const { data: users } = await authClient.admin.listUsers({
  limit: 50,
  offset: 0,
  sortBy: 'createdAt',
  sortDirection: 'desc',
  filterBy: 'email',
  filterValue: '@company.com',
});

// Create User (Admin)
await authClient.admin.createUser({
  email: 'newuser@example.com',
  password: 'TempPassword123!',
  name: 'New User',
  role: 'user',
  emailVerified: true,
});

// Update User
await authClient.admin.updateUser({
  userId: 'user_123',
  data: {
    name: 'Updated Name',
    role: 'admin',
    emailVerified: true,
  },
});

// Ban User
await authClient.admin.banUser({
  userId: 'user_123',
  reason: 'Violation of terms',
  banUntil: new Date('2025-12-31'),
});

// Unban User
await authClient.admin.unbanUser({
  userId: 'user_123',
});

// Impersonate User
await authClient.admin.impersonateUser({
  userId: 'user_123',
});

// List User Sessions
const { data: sessions } = await authClient.admin.listUserSessions({
  userId: 'user_123',
});

// Revoke User Session
await authClient.admin.revokeUserSession({
  sessionId: 'session_456',
});

// Delete User
await authClient.admin.deleteUser({
  userId: 'user_123',
});
```

## Bearer Token Plugin

Enables stateless authentication using bearer tokens for API access.

```typescript
import { betterAuth } from 'better-auth';
import { bearer } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    bearer({
      expiresIn: 60 * 60 * 24 * 7, // 7 days
    }),
  ],
});

// Client Usage
import { bearerClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [bearerClient()],
});

// Generate Bearer Token
const { data } = await authClient.bearer.generate();

console.log('Access token:', data.accessToken);

// Use Bearer Token in API Calls
fetch('/api/protected', {
  headers: {
    Authorization: `Bearer ${data.accessToken}`,
  },
});

// Server-side Bearer Token Validation
const session = await auth.api.getSession({
  headers: {
    authorization: `Bearer ${token}`,
  },
});
```

## API Key Plugin

Provides long-lived API keys for server-to-server authentication.

```typescript
import { betterAuth } from 'better-auth';
import { apiKey } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    apiKey({
      prefix: 'ba_', // API key prefix
    }),
  ],
});

// Client Usage
import { apiKeyClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [apiKeyClient()],
});

// Create API Key
const { data } = await authClient.apiKey.create({
  name: 'Production API Key',
  expiresIn: 60 * 60 * 24 * 365, // 1 year
});

console.log('API Key:', data.key);

// List API Keys
const { data: keys } = await authClient.apiKey.list();

// Revoke API Key
await authClient.apiKey.revoke({
  id: 'key_123',
});

// Server-side API Key Validation
const session = await auth.api.getSession({
  headers: {
    'x-api-key': apiKey,
  },
});
```

## JWT Plugin

Generates and validates JSON Web Tokens for session management.

```typescript
import { betterAuth } from 'better-auth';
import { jwt } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    jwt({
      algorithm: 'HS256',
      expiresIn: '7d',
      issuer: 'https://example.com',
      audience: ['https://api.example.com'],
    }),
  ],
});

// Client Usage
import { jwtClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [jwtClient()],
});

// Generate JWT
const { data } = await authClient.jwt.generate();

console.log('JWT:', data.token);

// Decode JWT
const decoded = await authClient.jwt.decode({
  token: data.token,
});

console.log('JWT payload:', decoded);
```

## Multi-Session Plugin

Allows users to maintain multiple concurrent sessions across devices.

```typescript
import { betterAuth } from 'better-auth';
import { multiSession } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    multiSession({
      maximumSessions: 5, // Max sessions per user
    }),
  ],
});

// Client Usage
import { multiSessionClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [multiSessionClient()],
});

// List Active Sessions
const { data: sessions } = await authClient.multiSession.listSessions();

sessions?.forEach(session => {
  console.log(
    `Device: ${session.userAgent}, Last active: ${session.updatedAt}`
  );
});

// Revoke Specific Session
await authClient.multiSession.revokeSession({
  sessionId: 'session_456',
});

// Revoke All Other Sessions
await authClient.multiSession.revokeOtherSessions();
```

## HaveIBeenPwned Plugin

Checks passwords against known data breaches for enhanced security.

```typescript
import { betterAuth } from 'better-auth';
import { haveibeenpwned } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    haveibeenpwned({
      // Automatically check on sign-up and password change
      checkOnSignUp: true,
      checkOnPasswordChange: true,

      // Optional: warn users instead of blocking
      blockCompromisedPasswords: true,
    }),
  ],
});

// The plugin automatically checks passwords against the HIBP database
// and rejects compromised passwords during sign-up and password changes
```

## CAPTCHA Plugin

Adds bot protection using reCAPTCHA or hCaptcha verification.

```typescript
import { betterAuth } from 'better-auth';
import { captcha } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    captcha({
      provider: 'recaptcha', // "recaptcha" | "hcaptcha"
      siteKey: process.env.RECAPTCHA_SITE_KEY!,
      secretKey: process.env.RECAPTCHA_SECRET_KEY!,

      // Endpoints to protect
      protectEndpoints: ['/sign-up/email', '/sign-in/email'],
    }),
  ],
});

// Client Usage
import { captchaClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [
    captchaClient({
      siteKey: process.env.NEXT_PUBLIC_RECAPTCHA_SITE_KEY!,
    }),
  ],
});

// CAPTCHA is automatically included in protected requests
await authClient.signUp.email({
  email: 'user@example.com',
  password: 'SecurePassword123!',
  // captchaToken is automatically added by the plugin
});
```

## Sign-In with Ethereum (SIWE) Plugin

Enables Web3 authentication using Ethereum wallet signatures.

```typescript
import { betterAuth } from 'better-auth';
import { siwe } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    siwe({
      domain: 'example.com',
      uri: 'https://example.com',
      statement: 'Sign in with your Ethereum account',
    }),
  ],
});

// Client Usage
import { siweClient } from 'better-auth/client/plugins';
import { ethers } from 'ethers';

const authClient = createAuthClient({
  plugins: [siweClient()],
});

// Get Nonce
const { data: nonce } = await authClient.siwe.getNonce();

// Create and Sign Message
const provider = new ethers.BrowserProvider(window.ethereum);
const signer = await provider.getSigner();
const address = await signer.getAddress();

const message = await authClient.siwe.prepareMessage({
  address,
  nonce: nonce.nonce,
});

const signature = await signer.signMessage(message);

// Verify and Sign In
await authClient.siwe.signIn({
  message,
  signature,
});
```

## Device Authorization Plugin

Implements OAuth 2.0 device authorization flow for limited-input devices.

```typescript
import { betterAuth } from 'better-auth';
import { deviceAuthorization } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    deviceAuthorization({
      deviceCodeExpiresIn: 600, // 10 minutes
      userCodeLength: 8,
      pollingInterval: 5, // seconds
    }),
  ],
});

// Client Usage (Device)
import { deviceAuthorizationClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [deviceAuthorizationClient()],
});

// Request Device Code
const { data } = await authClient.deviceAuthorization.requestCode();

console.log('User code:', data.userCode);
console.log('Verification URL:', data.verificationUri);

// Poll for Authorization
const result = await authClient.deviceAuthorization.pollForAuthorization({
  deviceCode: data.deviceCode,
});

// User visits verification URL and enters user code to authorize
```

## Access Control Plugin

Provides fine-grained permission and role-based access control.

```typescript
import { betterAuth } from 'better-auth';
import { access } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    access({
      permissions: {
        post: ['create', 'read', 'update', 'delete'],
        comment: ['create', 'read', 'delete'],
        user: ['read', 'update'],
      },

      roles: {
        admin: {
          post: ['create', 'read', 'update', 'delete'],
          comment: ['create', 'read', 'delete'],
          user: ['read', 'update'],
        },
        editor: {
          post: ['create', 'read', 'update'],
          comment: ['create', 'read'],
        },
        viewer: {
          post: ['read'],
          comment: ['read'],
        },
      },
    }),
  ],
});

// Client Usage
import { accessClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [accessClient()],
});

// Check Permission
const canEdit = await authClient.access.hasPermission({
  resource: 'post',
  action: 'update',
});

// Get User Permissions
const { data: permissions } = await authClient.access.getPermissions();

console.log('User permissions:', permissions);
```

## One-Time Token Plugin

Generates single-use tokens for secure one-time operations.

```typescript
import { betterAuth } from 'better-auth';
import { oneTimeToken } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    oneTimeToken({
      expiresIn: 60 * 15, // 15 minutes
    }),
  ],
});

// Client Usage
import { oneTimeTokenClient } from 'better-auth/client/plugins';

const authClient = createAuthClient({
  plugins: [oneTimeTokenClient()],
});

// Generate One-Time Token
const { data } = await authClient.oneTimeToken.generate({
  action: 'download-report',
  metadata: { reportId: '123' },
});

console.log('Token:', data.token);

// Verify and Consume Token (server-side)
const result = await auth.api.oneTimeToken.verify({
  token: data.token,
});

if (result.valid) {
  console.log('Token metadata:', result.metadata);
  // Perform action and token is automatically consumed
}
```

## Generic OAuth Plugin

Adds support for custom OAuth 2.0 providers not built into Better Auth.

```typescript
import { betterAuth } from 'better-auth';
import { genericOAuth } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    genericOAuth({
      config: [
        {
          providerId: 'custom-provider',
          clientId: process.env.CUSTOM_CLIENT_ID!,
          clientSecret: process.env.CUSTOM_CLIENT_SECRET!,
          authorizationUrl: 'https://oauth.example.com/authorize',
          tokenUrl: 'https://oauth.example.com/token',
          userInfoUrl: 'https://oauth.example.com/userinfo',
          scopes: ['openid', 'profile', 'email'],
        },
      ],
    }),
  ],
});

// Client Usage - Same as other OAuth providers
await authClient.signIn.social({
  provider: 'custom-provider',
  callbackURL: '/dashboard',
});
```

## Custom Plugin Development

Creates reusable plugins with endpoints, schemas, hooks, and middleware.

```typescript
import { createAuthEndpoint, sessionMiddleware } from 'better-auth';
import type { BetterAuthPlugin } from 'better-auth';
import { z } from 'zod';

export const customSubscriptionPlugin = (options?: { plans?: string[] }) => {
  return {
    id: 'subscription',

    // Add database schema
    schema: {
      subscription: {
        fields: {
          userId: {
            type: 'string',
            required: true,
            references: { model: 'user', field: 'id' },
          },
          plan: { type: 'string', required: true },
          status: { type: 'string', required: true },
          currentPeriodEnd: { type: 'date', required: true },
          cancelAtPeriodEnd: { type: 'boolean', required: true },
        },
      },
    },

    // Add custom endpoints
    endpoints: {
      getSubscription: createAuthEndpoint(
        '/subscription/get',
        {
          method: 'GET',
          use: [sessionMiddleware],
        },
        async ctx => {
          const subscription = await ctx.context.adapter.findOne({
            model: 'subscription',
            where: [{ field: 'userId', value: ctx.context.session.user.id }],
          });

          return { subscription };
        }
      ),

      updateSubscription: createAuthEndpoint(
        '/subscription/update',
        {
          method: 'POST',
          body: z.object({
            plan: z.enum(['free', 'pro', 'enterprise']),
          }),
          use: [sessionMiddleware],
        },
        async ctx => {
          const updated = await ctx.context.adapter.update({
            model: 'subscription',
            where: [{ field: 'userId', value: ctx.context.session.user.id }],
            update: { plan: ctx.body.plan },
          });

          return { subscription: updated };
        }
      ),
    },

    // Add hooks
    hooks: {
      after: [
        {
          matcher: context => context.path === '/sign-up/email',
          handler: async ctx => {
            // Create free subscription on sign up
            await ctx.context.adapter.create({
              model: 'subscription',
              data: {
                userId: ctx.context.session.user.id,
                plan: 'free',
                status: 'active',
                currentPeriodEnd: new Date(
                  Date.now() + 30 * 24 * 60 * 60 * 1000
                ),
                cancelAtPeriodEnd: false,
              },
            });
          },
        },
      ],
    },

    // Add rate limiting
    rateLimit: [
      {
        pathMatcher: path => path.startsWith('/subscription/'),
        window: 60,
        max: 10,
      },
    ],

    // Type inference for client
    $Infer: {
      Subscription: {} as {
        plan: string;
        status: string;
        currentPeriodEnd: Date;
      },
    },
  } satisfies BetterAuthPlugin;
};

// Usage
export const auth = betterAuth({
  plugins: [
    customSubscriptionPlugin({
      plans: ['free', 'pro', 'enterprise'],
    }),
  ],
});
```

## Rate Limiting Configuration

Controls request frequency to prevent abuse and protect endpoints from attacks.

```typescript
import { betterAuth } from 'better-auth';

export const auth = betterAuth({
  // Global rate limiting
  rateLimit: {
    enabled: true,
    window: 60, // seconds
    max: 10, // requests per window
    storage: 'memory', // "memory" | "database"

    // Custom rate limit rules
    customRules: [
      {
        pathMatcher: path => path === '/sign-in/email',
        window: 60,
        max: 5, // More restrictive for sign-in
      },
      {
        pathMatcher: path => path === '/sign-up/email',
        window: 60,
        max: 3, // Even more restrictive for sign-up
      },
      {
        pathMatcher: path => path.startsWith('/reset-password'),
        window: 300, // 5 minutes
        max: 3,
      },
    ],
  },
});

// Plugin-specific rate limiting
import { twoFactor } from 'better-auth/plugins';

export const auth = betterAuth({
  plugins: [
    twoFactor({
      // Plugin adds its own rate limits
      rateLimit: {
        window: 60,
        max: 3, // Only 3 2FA attempts per minute
      },
    }),
  ],
});
```

## Better Auth provides a production-ready authentication system that scales from simple email/password flows to complex multi-tenant applications with enterprise SSO, Web3 authentication, and device authorization. The plugin architecture enables rapid feature development while maintaining type safety across the entire stack, supporting advanced features like phone number authentication, username login, anonymous sessions, bearer tokens, API keys, JWT tokens, CAPTCHA protection, password breach checking, and fine-grained access control. Database adapters abstract away ORM-specific details, allowing seamless switching between Prisma, Drizzle, MongoDB, or Kysely. Framework integrations handle the nuances of Next.js App Router, SvelteKit, Solid Start, React Start, and other modern frameworks, ensuring cookies, headers, and redirects work correctly in server components, API routes, and edge runtimes.

The client libraries provide a unified API across React, Vue, Svelte, Solid, and Lynx with framework-specific primitives like hooks, stores, and signals for reactive session management. Plugins like organization, two-factor, passkey, phone number, username, anonymous, bearer, API key, JWT, multi-session, CAPTCHA, SIWE, device authorization, and access control add complete features with minimal configuration, including database schemas, API endpoints, hooks, rate limiting, and client methods. The system's security defaults include automatic CSRF protection, secure cookie handling with httpOnly and sameSite flags, bcrypt password hashing, rate limiting, password breach checking via HaveIBeenPwned integration, and session validation on every request, making it suitable for production use without extensive security hardening.
