# Supabase

Supabase is an open-source Firebase alternative that provides a complete Postgres development platform. It combines enterprise-grade open-source tools to deliver database hosting, authentication, auto-generated APIs (REST and GraphQL), real-time subscriptions, file storage, edge functions, and AI/vector capabilities. The platform is designed to give developers a Firebase-like experience while maintaining full control over their data using standard Postgres.

The platform consists of multiple integrated services: a hosted Postgres database with PostgREST for auto-generated REST APIs, GoTrue for JWT-based authentication, Realtime for WebSocket-based subscriptions, Storage API for S3-compatible file management, pg_graphql for GraphQL support, and globally distributed Edge Functions powered by Deno. All services work together through modular client libraries available for JavaScript/TypeScript, Flutter, Swift, and Python, with community support for additional languages.

## Client Initialization

### Browser Client Setup

Initialize the Supabase client for browser-based applications using environment variables for project URL and anonymous key.

```typescript
import { createBrowserClient } from "@supabase/ssr"

export function createClient() {
  return createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!
  )
}

// Usage in a React component
import { createClient } from '@/utils/supabase/client'

export default function MyComponent() {
  const supabase = createClient()

  const handleSignIn = async (email: string, password: string) => {
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    })

    if (error) {
      console.error('Error signing in:', error.message)
      return
    }

    console.log('User signed in:', data.user)
  }

  return <div>My App</div>
}
```

### Server-Side Client Setup

Configure Supabase for Next.js server components with cookie-based session management for authentication across server and client.

```typescript
import { createServerClient } from '@supabase/ssr'
import { cookies } from 'next/headers'

export async function createClient() {
  const cookieStore = await cookies()

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll()
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) =>
              cookieStore.set(name, value, options)
            )
          } catch {
            // setAll called from Server Component - can be ignored
            // if middleware is refreshing user sessions
          }
        },
      },
    }
  )
}

// Usage in a server component
import { createClient } from '@/utils/supabase/server'

export default async function ServerComponent() {
  const supabase = await createClient()

  const { data: { user } } = await supabase.auth.getUser()

  if (!user) {
    return <div>Not authenticated</div>
  }

  const { data: profile, error } = await supabase
    .from('profiles')
    .select('*')
    .eq('id', user.id)
    .single()

  if (error) {
    console.error('Error fetching profile:', error)
    return <div>Error loading profile</div>
  }

  return (
    <div>
      <h1>Welcome, {profile.username}</h1>
      <p>{profile.full_name}</p>
    </div>
  )
}
```

## Authentication

### Email/Password Authentication

Sign up and sign in users with email and password credentials, with automatic JWT token management.

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
);

// Sign up a new user
async function signUp(email: string, password: string, metadata: any) {
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: {
      data: {
        full_name: metadata.fullName,
        avatar_url: metadata.avatarUrl,
      },
    },
  });

  if (error) {
    throw new Error(`Sign up failed: ${error.message}`);
  }

  return data;
}

// Sign in existing user
async function signIn(email: string, password: string) {
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  });

  if (error) {
    throw new Error(`Sign in failed: ${error.message}`);
  }

  console.log('Access token:', data.session?.access_token);
  console.log('User:', data.user);

  return data;
}

// Sign out
async function signOut() {
  const { error } = await supabase.auth.signOut();

  if (error) {
    throw new Error(`Sign out failed: ${error.message}`);
  }
}

// Listen to auth state changes
supabase.auth.onAuthStateChange((event, session) => {
  console.log('Auth event:', event);
  console.log('Session:', session);

  if (event === 'SIGNED_IN') {
    console.log('User signed in:', session?.user);
  }

  if (event === 'SIGNED_OUT') {
    console.log('User signed out');
  }
});

// Usage example
try {
  await signUp('user@example.com', 'secure-password-123', {
    fullName: 'John Doe',
    avatarUrl: 'https://example.com/avatar.jpg',
  });

  const { user, session } = await signIn(
    'user@example.com',
    'secure-password-123'
  );
  console.log('Logged in as:', user.email);
} catch (error) {
  console.error(error);
}
```

### OAuth Authentication

Authenticate users through third-party OAuth providers with automatic redirect handling.

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
);

// Sign in with Google OAuth
async function signInWithGoogle() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: 'https://your-app.com/auth/callback',
      queryParams: {
        access_type: 'offline',
        prompt: 'consent',
      },
    },
  });

  if (error) {
    throw new Error(`OAuth sign in failed: ${error.message}`);
  }

  // Redirects to Google login
  console.log('Redirect URL:', data.url);
}

// Sign in with GitHub
async function signInWithGitHub() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'github',
    options: {
      redirectTo: 'https://your-app.com/auth/callback',
      scopes: 'repo gist',
    },
  });

  if (error) {
    throw new Error(`GitHub OAuth failed: ${error.message}`);
  }
}

// Handle OAuth callback in Next.js route
// File: app/auth/callback/route.ts
import { createClient } from '@/utils/supabase/server';
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const requestUrl = new URL(request.url);
  const code = requestUrl.searchParams.get('code');

  if (code) {
    const supabase = await createClient();
    await supabase.auth.exchangeCodeForSession(code);
  }

  // Redirect to home page
  return NextResponse.redirect(new URL('/', request.url));
}
```

## Database Operations

### Query Data with REST API

Perform CRUD operations on database tables using the auto-generated REST API with chainable query builders.

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
);

// Select all rows
async function getAllPosts() {
  const { data, error } = await supabase.from('posts').select('*');

  if (error) {
    throw new Error(`Query failed: ${error.message}`);
  }

  return data;
}

// Select with filters
async function getPublishedPosts() {
  const { data, error } = await supabase
    .from('posts')
    .select('id, title, content, author:profiles(username, avatar_url)')
    .eq('published', true)
    .gt('views', 100)
    .order('created_at', { ascending: false })
    .limit(10);

  if (error) {
    throw new Error(`Query failed: ${error.message}`);
  }

  return data;
}

// Insert data
async function createPost(post: any) {
  const { data, error } = await supabase
    .from('posts')
    .insert({
      title: post.title,
      content: post.content,
      author_id: post.authorId,
      published: false,
    })
    .select()
    .single();

  if (error) {
    throw new Error(`Insert failed: ${error.message}`);
  }

  console.log('Created post:', data);
  return data;
}

// Update data
async function updatePost(postId: string, updates: any) {
  const { data, error } = await supabase
    .from('posts')
    .update(updates)
    .eq('id', postId)
    .select()
    .single();

  if (error) {
    throw new Error(`Update failed: ${error.message}`);
  }

  return data;
}

// Delete data
async function deletePost(postId: string) {
  const { error } = await supabase.from('posts').delete().eq('id', postId);

  if (error) {
    throw new Error(`Delete failed: ${error.message}`);
  }
}

// Usage example
const posts = await getPublishedPosts();
console.log('Published posts:', posts);

const newPost = await createPost({
  title: 'My First Post',
  content: 'Hello, world!',
  authorId: 'user-uuid-here',
});

await updatePost(newPost.id, { published: true, views: 0 });
await deletePost(newPost.id);
```

### Row Level Security (RLS) Policies

Secure database access using Postgres Row Level Security policies that enforce per-user permissions.

```sql
-- Create profiles table
create table profiles (
  id uuid references auth.users not null primary key,
  updated_at timestamp with time zone,
  username text unique,
  full_name text,
  avatar_url text,
  website text,

  constraint username_length check (char_length(username) >= 3)
);

-- Enable Row Level Security
alter table profiles enable row level security;

-- Policy: Anyone can view profiles
create policy "Public profiles are viewable by everyone"
  on profiles for select
  using (true);

-- Policy: Users can insert their own profile
create policy "Users can insert their own profile"
  on profiles for insert
  with check ((select auth.uid()) = id);

-- Policy: Users can update their own profile
create policy "Users can update own profile"
  on profiles for update
  using ((select auth.uid()) = id);

-- Create posts table with user ownership
create table posts (
  id uuid default gen_random_uuid() primary key,
  created_at timestamp with time zone default timezone('utc'::text, now()),
  title text not null,
  content text,
  author_id uuid references auth.users not null,
  published boolean default false
);

alter table posts enable row level security;

-- Policy: Users can view their own posts or published posts
create policy "Users can view own posts and published posts"
  on posts for select
  using (
    auth.uid() = author_id OR published = true
  );

-- Policy: Users can insert their own posts
create policy "Users can create posts"
  on posts for insert
  with check (auth.uid() = author_id);

-- Policy: Users can update their own posts
create policy "Users can update own posts"
  on posts for update
  using (auth.uid() = author_id);

-- Policy: Users can delete their own posts
create policy "Users can delete own posts"
  on posts for delete
  using (auth.uid() = author_id);

-- Create trigger to auto-create profile on signup
create function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, full_name, avatar_url)
  values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
  return new;
end;
$$ language plpgsql security definer;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
```

## Storage

### File Upload and Management

Upload, download, and manage files in S3-compatible storage with automatic CDN distribution and access control.

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
)

// Upload file from browser
async function uploadAvatar(file: File, userId: string) {
  const fileExt = file.name.split('.').pop()
  const fileName = `${userId}-${Math.random()}.${fileExt}`
  const filePath = `avatars/${fileName}`

  const { data, error } = await supabase.storage
    .from('avatars')
    .upload(filePath, file, {
      cacheControl: '3600',
      upsert: false,
    })

  if (error) {
    throw new Error(`Upload failed: ${error.message}`)
  }

  // Get public URL
  const { data: urlData } = supabase.storage
    .from('avatars')
    .getPublicUrl(filePath)

  console.log('File uploaded to:', urlData.publicUrl)
  return { path: data.path, url: urlData.publicUrl }
}

// Download file
async function downloadFile(filePath: string) {
  const { data, error } = await supabase.storage
    .from('avatars')
    .download(filePath)

  if (error) {
    throw new Error(`Download failed: ${error.message}`)
  }

  // Convert blob to URL for display
  const url = URL.createObjectURL(data)
  return url
}

// List files in bucket
async function listFiles(folder: string) {
  const { data, error } = await supabase.storage
    .from('avatars')
    .list(folder, {
      limit: 100,
      offset: 0,
      sortBy: { column: 'name', order: 'asc' },
    })

  if (error) {
    throw new Error(`List failed: ${error.message}`)
  }

  return data
}

// Delete file
async function deleteFile(filePath: string) {
  const { error } = await supabase.storage
    .from('avatars')
    .remove([filePath])

  if (error) {
    throw new Error(`Delete failed: ${error.message}`)
  }
}

// Create signed URL for private files
async function createSignedUrl(filePath: string, expiresIn: number = 3600) {
  const { data, error } = await supabase.storage
    .from('private-files')
    .createSignedUrl(filePath, expiresIn)

  if (error) {
    throw new Error(`Signed URL creation failed: ${error.message}`)
  }

  console.log('Signed URL:', data.signedUrl)
  return data.signedUrl
}

// Image transformation with CDN
function getTransformedImageUrl(filePath: string) {
  const { data } = supabase.storage
    .from('avatars')
    .getPublicUrl(filePath, {
      transform: {
        width: 200,
        height: 200,
        resize: 'cover',
        quality: 80,
      },
    })

  return data.publicUrl
}

// Usage example with React component
import { useState } from 'react'

export default function AvatarUpload({ userId }: { userId: string }) {
  const [uploading, setUploading] = useState(false)
  const [avatarUrl, setAvatarUrl] = useState<string | null>(null)

  const handleUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    try {
      setUploading(true)

      if (!event.target.files || event.target.files.length === 0) {
        throw new Error('You must select an image to upload.')
      }

      const file = event.target.files[0]
      const { url } = await uploadAvatar(file, userId)

      setAvatarUrl(url)

      // Update user profile with new avatar URL
      await supabase
        .from('profiles')
        .update({ avatar_url: url })
        .eq('id', userId)

    } catch (error) {
      console.error('Error uploading avatar:', error)
    } finally {
      setUploading(false)
    }
  }

  return (
    <div>
      {avatarUrl && <img src={avatarUrl} alt="Avatar" />}
      <input
        type="file"
        accept="image/*"
        onChange={handleUpload}
        disabled={uploading}
      />
    </div>
  )
}
```

### Storage Access Policies

Configure storage bucket policies to control file access based on authentication and custom rules.

```sql
-- Set up Storage bucket
insert into storage.buckets (id, name, public)
values ('avatars', 'avatars', true);

-- Policy: Anyone can view avatar images
create policy "Avatar images are publicly accessible"
  on storage.objects for select
  using (bucket_id = 'avatars');

-- Policy: Authenticated users can upload avatars
create policy "Anyone can upload an avatar"
  on storage.objects for insert
  with check (
    bucket_id = 'avatars'
    AND auth.role() = 'authenticated'
  );

-- Policy: Users can update their own avatars
create policy "Users can update own avatar"
  on storage.objects for update
  using (
    auth.uid()::text = (storage.foldername(name))[1]
    AND bucket_id = 'avatars'
  );

-- Policy: Users can delete their own avatars
create policy "Users can delete own avatar"
  on storage.objects for delete
  using (
    auth.uid()::text = (storage.foldername(name))[1]
    AND bucket_id = 'avatars'
  );

-- Private bucket for user documents
insert into storage.buckets (id, name, public)
values ('private-files', 'private-files', false);

-- Policy: Users can only access their own private files
create policy "Users can access own private files"
  on storage.objects for select
  using (
    bucket_id = 'private-files'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );

create policy "Users can upload own private files"
  on storage.objects for insert
  with check (
    bucket_id = 'private-files'
    AND auth.uid()::text = (storage.foldername(name))[1]
  );
```

## Realtime

### Subscribe to Database Changes

Listen to Postgres changes in real-time using WebSockets for INSERT, UPDATE, and DELETE operations.

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
)

// Subscribe to all changes in a table
const channel = supabase
  .channel('posts-channel')
  .on(
    'postgres_changes',
    { event: '*', schema: 'public', table: 'posts' },
    (payload) => {
      console.log('Database change:', payload)

      if (payload.eventType === 'INSERT') {
        console.log('New post:', payload.new)
      }

      if (payload.eventType === 'UPDATE') {
        console.log('Updated post:', payload.new)
        console.log('Old values:', payload.old)
      }

      if (payload.eventType === 'DELETE') {
        console.log('Deleted post:', payload.old)
      }
    }
  )
  .subscribe((status) => {
    if (status === 'SUBSCRIBED') {
      console.log('Ready to receive database changes')
    }
  })

// Subscribe to specific events only
const insertChannel = supabase
  .channel('new-posts')
  .on(
    'postgres_changes',
    { event: 'INSERT', schema: 'public', table: 'posts' },
    (payload) => {
      console.log('New post created:', payload.new)
    }
  )
  .subscribe()

// Subscribe with filters
const userPostsChannel = supabase
  .channel('user-posts')
  .on(
    'postgres_changes',
    {
      event: '*',
      schema: 'public',
      table: 'posts',
      filter: 'author_id=eq.user-uuid-here',
    },
    (payload) => {
      console.log('Change to your posts:', payload)
    }
  )
  .subscribe()

// Unsubscribe when done
function cleanup() {
  channel.unsubscribe()
  insertChannel.unsubscribe()
  userPostsChannel.unsubscribe()
}

// React example with real-time updates
import { useEffect, useState } from 'react'
import { createClient } from '@/utils/supabase/client'

export default function RealtimePosts() {
  const [posts, setPosts] = useState<any[]>([])
  const supabase = createClient()

  useEffect(() => {
    // Fetch initial posts
    async function fetchPosts() {
      const { data } = await supabase
        .from('posts')
        .select('*')
        .order('created_at', { ascending: false })

      setPosts(data || [])
    }

    fetchPosts()

    // Subscribe to new posts
    const channel = supabase
      .channel('realtime-posts')
      .on(
        'postgres_changes',
        { event: 'INSERT', schema: 'public', table: 'posts' },
        (payload) => {
          setPosts((current) => [payload.new, ...current])
        }
      )
      .on(
        'postgres_changes',
        { event: 'DELETE', schema: 'public', table: 'posts' },
        (payload) => {
          setPosts((current) =>
            current.filter((post) => post.id !== payload.old.id)
          )
        }
      )
      .on(
        'postgres_changes',
        { event: 'UPDATE', schema: 'public', table: 'posts' },
        (payload) => {
          setPosts((current) =>
            current.map((post) =>
              post.id === payload.new.id ? payload.new : post
            )
          )
        }
      )
      .subscribe()

    return () => {
      channel.unsubscribe()
    }
  }, [])

  return (
    <div>
      <h1>Real-time Posts</h1>
      {posts.map((post) => (
        <div key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </div>
      ))}
    </div>
  )
}
```

### Broadcast Messages

Send and receive low-latency messages between clients for real-time collaboration features.

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
)

// Set up broadcast channel
const channel = supabase.channel('chat-room')

// Send broadcast messages
async function sendMessage(message: string, username: string) {
  await channel.send({
    type: 'broadcast',
    event: 'message',
    payload: {
      message,
      username,
      timestamp: new Date().toISOString(),
    },
  })
}

// Receive broadcast messages
channel
  .on('broadcast', { event: 'message' }, (payload) => {
    console.log('Received message:', payload)
    displayMessage(payload.payload)
  })
  .subscribe()

function displayMessage(data: any) {
  console.log(`${data.username} at ${data.timestamp}: ${data.message}`)
}

// Cursor tracking example
interface CursorPosition {
  x: number
  y: number
  userId: string
}

const cursorChannel = supabase.channel('cursor-tracking')

function sendCursorPosition(x: number, y: number, userId: string) {
  cursorChannel.send({
    type: 'broadcast',
    event: 'cursor-move',
    payload: { x, y, userId },
  })
}

cursorChannel
  .on('broadcast', { event: 'cursor-move' }, (payload) => {
    const { x, y, userId } = payload.payload as CursorPosition
    updateCursorDisplay(userId, x, y)
  })
  .subscribe()

function updateCursorDisplay(userId: string, x: number, y: number) {
  // Update cursor position in UI
  console.log(`User ${userId} cursor at (${x}, ${y})`)
}

// React chat component
import { useEffect, useState } from 'react'

export default function ChatRoom({ username }: { username: string }) {
  const [messages, setMessages] = useState<any[]>([])
  const [input, setInput] = useState('')
  const supabase = createClient()

  useEffect(() => {
    const channel = supabase.channel('chat-room')

    channel
      .on('broadcast', { event: 'message' }, (payload) => {
        setMessages((current) => [...current, payload.payload])
      })
      .subscribe()

    return () => {
      channel.unsubscribe()
    }
  }, [])

  const handleSend = async () => {
    if (!input.trim()) return

    await supabase.channel('chat-room').send({
      type: 'broadcast',
      event: 'message',
      payload: {
        message: input,
        username,
        timestamp: new Date().toISOString(),
      },
    })

    setInput('')
  }

  return (
    <div>
      <div>
        {messages.map((msg, i) => (
          <div key={i}>
            <strong>{msg.username}:</strong> {msg.message}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && handleSend()}
      />
      <button onClick={handleSend}>Send</button>
    </div>
  )
}
```

### Presence Tracking

Track and synchronize user state across clients to show who is online and active.

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
)

interface UserPresence {
  user_id: string
  username: string
  online_at: string
  status: 'online' | 'away' | 'busy'
}

// Track user presence
const presenceChannel = supabase.channel('room-1', {
  config: {
    presence: {
      key: 'user_id',
    },
  },
})

// Track current user's presence
async function trackPresence(userId: string, username: string) {
  await presenceChannel.track({
    user_id: userId,
    username: username,
    online_at: new Date().toISOString(),
    status: 'online',
  })
}

// Listen to presence changes
presenceChannel
  .on('presence', { event: 'sync' }, () => {
    const state = presenceChannel.presenceState()
    console.log('Current users:', state)

    const users = Object.keys(state).map(key => state[key][0])
    console.log('Online users:', users)
  })
  .on('presence', { event: 'join' }, ({ key, newPresences }) => {
    console.log('User joined:', newPresences)
  })
  .on('presence', { event: 'leave' }, ({ key, leftPresences }) => {
    console.log('User left:', leftPresences)
  })
  .subscribe(async (status) => {
    if (status === 'SUBSCRIBED') {
      await trackPresence('user-123', 'John Doe')
    }
  })

// Update presence state
async function updatePresenceStatus(status: 'online' | 'away' | 'busy') {
  await presenceChannel.track({
    status,
    updated_at: new Date().toISOString(),
  })
}

// Stop tracking presence
async function untrack() {
  await presenceChannel.untrack()
}

// React presence component
import { useEffect, useState } from 'react'
import { createClient } from '@/utils/supabase/client'

export default function OnlineUsers({ userId, username }: any) {
  const [onlineUsers, setOnlineUsers] = useState<UserPresence[]>([])
  const supabase = createClient()

  useEffect(() => {
    const channel = supabase.channel('presence-room', {
      config: {
        presence: {
          key: userId,
        },
      },
    })

    channel
      .on('presence', { event: 'sync' }, () => {
        const state = channel.presenceState()
        const users = Object.keys(state).map(key => state[key][0] as UserPresence)
        setOnlineUsers(users)
      })
      .on('presence', { event: 'join' }, ({ newPresences }) => {
        console.log('New users joined:', newPresences)
      })
      .on('presence', { event: 'leave' }, ({ leftPresences }) => {
        console.log('Users left:', leftPresences)
      })
      .subscribe(async (status) => {
        if (status === 'SUBSCRIBED') {
          await channel.track({
            user_id: userId,
            username: username,
            online_at: new Date().toISOString(),
            status: 'online',
          })
        }
      })

    return () => {
      channel.untrack()
      channel.unsubscribe()
    }
  }, [userId, username])

  return (
    <div>
      <h3>Online Users ({onlineUsers.length})</h3>
      <ul>
        {onlineUsers.map((user) => (
          <li key={user.user_id}>
            {user.username} - {user.status}
          </li>
        ))}
      </ul>
    </div>
  )
}
```

## Edge Functions

### Basic Edge Function

Deploy serverless TypeScript functions at the edge for webhooks, API integrations, and custom backend logic.

```typescript
// File: supabase/functions/hello-world/index.ts
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts';

serve(async req => {
  const { name } = await req.json();

  const data = {
    message: `Hello ${name}!`,
    timestamp: new Date().toISOString(),
  };

  return new Response(JSON.stringify(data), {
    headers: { 'Content-Type': 'application/json' },
    status: 200,
  });
});

// Deploy the function
// $ supabase functions deploy hello-world

// Invoke from client
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
);

async function callEdgeFunction() {
  const { data, error } = await supabase.functions.invoke('hello-world', {
    body: { name: 'World' },
  });

  if (error) {
    console.error('Function error:', error);
    return;
  }

  console.log('Response:', data);
  // Output: { message: 'Hello World!', timestamp: '...' }
}
```

### Edge Function with Supabase Client

Access Supabase services from within Edge Functions with automatic authentication context.

```typescript
// File: supabase/functions/create-post/index.ts
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts';
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers':
    'authorization, x-client-info, apikey, content-type',
};

serve(async req => {
  // Handle CORS
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    // Create Supabase client with user's auth context
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_ANON_KEY') ?? '',
      {
        global: {
          headers: { Authorization: req.headers.get('Authorization')! },
        },
      }
    );

    // Get authenticated user
    const {
      data: { user },
      error: userError,
    } = await supabase.auth.getUser();

    if (userError || !user) {
      throw new Error('Unauthorized');
    }

    // Parse request body
    const { title, content } = await req.json();

    // Insert post with RLS automatically applied
    const { data, error } = await supabase
      .from('posts')
      .insert({
        title,
        content,
        author_id: user.id,
        published: false,
      })
      .select()
      .single();

    if (error) {
      throw error;
    }

    return new Response(JSON.stringify({ success: true, post: data }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200,
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 400,
    });
  }
});

// Invoke from client with auth
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
);

async function createPost() {
  const { data, error } = await supabase.functions.invoke('create-post', {
    body: {
      title: 'My New Post',
      content: 'This is the content of my post.',
    },
  });

  if (error) {
    console.error('Error creating post:', error);
    return;
  }

  console.log('Post created:', data.post);
}
```

### Edge Function with OpenAI Integration

Integrate third-party APIs like OpenAI for AI-powered features in your edge functions.

```typescript
// File: supabase/functions/openai/index.ts
import 'https://deno.land/x/xhr@0.3.0/mod.ts';
import { serve } from 'https://deno.land/std@0.168.0/http/server.ts';

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers':
    'authorization, x-client-info, apikey, content-type',
};

serve(async req => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders });
  }

  try {
    const { query } = await req.json();

    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${Deno.env.get('OPENAI_API_KEY')}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'gpt-4',
        messages: [
          { role: 'system', content: 'You are a helpful assistant.' },
          { role: 'user', content: query },
        ],
        temperature: 0.7,
        max_tokens: 500,
      }),
    });

    const data = await response.json();
    const answer = data.choices[0].message.content;

    return new Response(JSON.stringify({ answer }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 500,
    });
  }
});

// Set secrets for the function
// $ supabase secrets set OPENAI_API_KEY=sk-...

// Invoke from client
const { data, error } = await supabase.functions.invoke('openai', {
  body: { query: 'Explain quantum computing in simple terms' },
});

if (!error) {
  console.log('AI Response:', data.answer);
}
```

## Vector Search and AI

### Vector Similarity Search

Store and query vector embeddings for semantic search, recommendation systems, and AI applications.

```typescript
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  'https://your-project.supabase.co',
  'your-anon-key'
);

// First, create a table with vector column (run in SQL editor)
/*
-- Enable pgvector extension
create extension if not exists vector;

-- Create documents table with embeddings
create table documents (
  id bigserial primary key,
  content text not null,
  embedding vector(1536), -- OpenAI embedding dimension
  metadata jsonb,
  created_at timestamp with time zone default timezone('utc'::text, now())
);

-- Create vector index for faster similarity search
create index on documents using ivfflat (embedding vector_cosine_ops)
with (lists = 100);
*/

// Generate embedding using OpenAI
async function generateEmbedding(text: string): Promise<number[]> {
  const response = await fetch('https://api.openai.com/v1/embeddings', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${OPENAI_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'text-embedding-ada-002',
      input: text,
    }),
  });

  const data = await response.json();
  return data.data[0].embedding;
}

// Store document with embedding
async function storeDocument(content: string, metadata: any) {
  const embedding = await generateEmbedding(content);

  const { data, error } = await supabase
    .from('documents')
    .insert({
      content,
      embedding,
      metadata,
    })
    .select()
    .single();

  if (error) {
    throw new Error(`Failed to store document: ${error.message}`);
  }

  return data;
}

// Semantic search using vector similarity
async function semanticSearch(query: string, matchCount: number = 5) {
  const queryEmbedding = await generateEmbedding(query);

  const { data, error } = await supabase.rpc('match_documents', {
    query_embedding: queryEmbedding,
    match_count: matchCount,
    match_threshold: 0.78, // Only return matches with similarity > 0.78
  });

  if (error) {
    throw new Error(`Search failed: ${error.message}`);
  }

  return data;
}

// Create the match_documents function in SQL
/*
create or replace function match_documents (
  query_embedding vector(1536),
  match_count int default 5,
  match_threshold float default 0.78
)
returns table (
  id bigint,
  content text,
  metadata jsonb,
  similarity float
)
language plpgsql
as $$
begin
  return query
  select
    documents.id,
    documents.content,
    documents.metadata,
    1 - (documents.embedding <=> query_embedding) as similarity
  from documents
  where 1 - (documents.embedding <=> query_embedding) > match_threshold
  order by documents.embedding <=> query_embedding
  limit match_count;
end;
$$;
*/

// Usage example
async function example() {
  // Store some documents
  await storeDocument('Supabase is an open source Firebase alternative.', {
    category: 'product',
    tags: ['database', 'backend'],
  });

  await storeDocument('PostgreSQL is a powerful relational database.', {
    category: 'technology',
    tags: ['database', 'sql'],
  });

  await storeDocument('Edge Functions run TypeScript code at the edge.', {
    category: 'product',
    tags: ['serverless', 'functions'],
  });

  // Search for similar documents
  const results = await semanticSearch('What is Supabase?');

  console.log('Search results:');
  results.forEach((doc: any) => {
    console.log(`${doc.content} (similarity: ${doc.similarity})`);
  });
}
```

## Configuration and Environment

### Environment Variables

Configure your Supabase project using environment variables for URL, keys, and custom settings.

```bash
# .env.local or .env
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Database connection string (for direct connections)
DATABASE_URL=postgresql://postgres:password@db.your-project.supabase.co:5432/postgres

# Optional: Custom domain
NEXT_PUBLIC_SUPABASE_URL=https://api.yourdomain.com
```

```typescript
// utils/supabase/config.ts
export const supabaseConfig = {
  url: process.env.NEXT_PUBLIC_SUPABASE_URL!,
  anonKey: process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
  serviceRoleKey: process.env.SUPABASE_SERVICE_ROLE_KEY,
};

// Create admin client with service role (server-side only)
import { createClient } from '@supabase/supabase-js';
import { supabaseConfig } from './config';

export const createAdminClient = () => {
  return createClient(supabaseConfig.url, supabaseConfig.serviceRoleKey!, {
    auth: {
      autoRefreshToken: false,
      persistSession: false,
    },
  });
};

// Use admin client for privileged operations
async function deleteUserAsAdmin(userId: string) {
  const adminClient = createAdminClient();

  const { error } = await adminClient.auth.admin.deleteUser(userId);

  if (error) {
    throw new Error(`Failed to delete user: ${error.message}`);
  }
}
```

### Local Development Setup

Set up Supabase locally using the CLI for development and testing.

```bash
# Install Supabase CLI
npm install -g supabase

# Initialize Supabase in your project
supabase init

# Start local Supabase stack (Postgres, Auth, Storage, Realtime, etc.)
supabase start

# Output will show local connection details:
# API URL: http://localhost:54321
# DB URL: postgresql://postgres:postgres@localhost:54322/postgres
# Studio URL: http://localhost:54323
# Anon key: eyJh...
# Service role key: eyJh...

# Create a migration
supabase migration new create_posts_table

# Apply migrations
supabase db push

# Generate TypeScript types from database
supabase gen types typescript --local > types/database.ts

# Run Edge Functions locally
supabase functions serve

# Deploy to production
supabase link --project-ref your-project-ref
supabase db push
supabase functions deploy function-name

# Stop local Supabase
supabase stop
```

## Summary

Supabase provides a comprehensive backend-as-a-service platform built on PostgreSQL, offering developers production-ready features including authentication, real-time subscriptions, file storage, and serverless functions. The platform emphasizes developer experience through auto-generated APIs, type-safe client libraries, and seamless integration across client and server environments. Key features include Row Level Security for fine-grained access control, realtime data synchronization via WebSockets, CDN-backed storage with on-the-fly image transformations, and globally distributed Edge Functions for low-latency serverless execution.

Integration patterns center around the modular client library that works consistently across browser, server, and edge environments. Authentication flows leverage JWT tokens stored in cookies for Next.js applications, enabling secure session management across Server Components, Client Components, API Routes, and Middleware. Database operations use chainable query builders with automatic RLS policy enforcement, while realtime features support both database change subscriptions and custom broadcast channels for collaborative applications. Edge Functions integrate seamlessly with other Supabase services and external APIs, making them ideal for webhooks, AI integrations, and custom business logic. The platform's local development workflow mirrors production, enabling rapid iteration with the Supabase CLI for migrations, type generation, and function deployment.
