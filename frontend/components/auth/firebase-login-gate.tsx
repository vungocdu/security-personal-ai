"use client";

import { createUserWithEmailAndPassword, onAuthStateChanged, signInWithEmailAndPassword, signOut, User } from "firebase/auth";
import { useEffect, useState } from "react";

import { AnalystWorkspace } from "@/components/workspace/analyst-workspace";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { workspaceApi } from "@/lib/api";
import type { AuthMeResponse } from "@/lib/types";
import { getFirebaseAuth, isFirebaseConfigured } from "@/lib/firebase";

function extractErrorMessage(caught: unknown): string {
  if (caught instanceof Error) {
    return caught.message;
  }
  return "Unexpected authentication error.";
}

export function FirebaseLoginGate() {
  const [sessionReady, setSessionReady] = useState(false);
  const [user, setUser] = useState<User | null>(null);
  const [backendProfile, setBackendProfile] = useState<AuthMeResponse | null>(null);
  const [email, setEmail] = useState("spai.analyst@actiwell.co");
  const [password, setPassword] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isFirebaseConfigured()) {
      setSessionReady(true);
      return;
    }

    const auth = getFirebaseAuth();
    if (!auth) {
      setError("Firebase is not configured correctly. Check NEXT_PUBLIC_FIREBASE_* environment.");
      setSessionReady(true);
      return;
    }

    const unsubscribe = onAuthStateChanged(auth, (nextUser) => {
      setUser(nextUser);
      setSessionReady(true);
    });
    return () => unsubscribe();
  }, []);

  useEffect(() => {
    async function resolveProfile() {
      if (!user) {
        setBackendProfile(null);
        return;
      }
      try {
        const profile = await workspaceApi.getMe();
        setBackendProfile(profile);
      } catch (caught) {
        setError(extractErrorMessage(caught));
      }
    }

    void resolveProfile();
  }, [user]);

  async function handleSignIn() {
    const auth = getFirebaseAuth();
    if (!auth) {
      setError("Firebase Auth is not available.");
      return;
    }
    setSubmitting(true);
    setError(null);
    try {
      await signInWithEmailAndPassword(auth, email.trim(), password);
    } catch (caught) {
      setError(extractErrorMessage(caught));
    } finally {
      setSubmitting(false);
    }
  }

  async function handleCreateAccount() {
    const auth = getFirebaseAuth();
    if (!auth) {
      setError("Firebase Auth is not available.");
      return;
    }
    setSubmitting(true);
    setError(null);
    try {
      await createUserWithEmailAndPassword(auth, email.trim(), password);
    } catch (caught) {
      setError(extractErrorMessage(caught));
    } finally {
      setSubmitting(false);
    }
  }

  async function handleSignOut() {
    const auth = getFirebaseAuth();
    if (!auth) {
      return;
    }
    await signOut(auth);
    setBackendProfile(null);
  }

  if (!sessionReady) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#f7f3ec]">
        <Card className="w-full max-w-md">
          <CardHeader>
            <CardTitle>Initializing session</CardTitle>
            <CardDescription>Checking Firebase authentication state…</CardDescription>
          </CardHeader>
        </Card>
      </div>
    );
  }

  if (!isFirebaseConfigured()) {
    return (
      <div>
        <div className="border-b border-[#e9ddca] bg-[#fff6e7] px-4 py-3 text-sm text-[#68430f]">
          Firebase Auth is not configured. Workspace is running in fixture mode without login enforcement.
        </div>
        <AnalystWorkspace />
      </div>
    );
  }

  if (!user) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[linear-gradient(180deg,_#f7f3ec_0%,_#eff2f7_100%)] px-4">
        <Card className="w-full max-w-md">
          <CardHeader>
            <CardTitle>Sign in to Analyst Workspace</CardTitle>
            <CardDescription>Firebase Email/Password authentication (project: actiwell-74477).</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <label className="flex flex-col gap-2 text-sm font-medium text-ink">
              Email
              <input
                className="rounded-xl border border-line px-3 py-2 text-sm outline-none focus:border-accent"
                type="email"
                value={email}
                onChange={(event) => setEmail(event.target.value)}
                autoComplete="email"
              />
            </label>
            <label className="flex flex-col gap-2 text-sm font-medium text-ink">
              Password
              <input
                className="rounded-xl border border-line px-3 py-2 text-sm outline-none focus:border-accent"
                type="password"
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                autoComplete="current-password"
              />
            </label>
            {error ? <div className="rounded-xl border border-[#efc5c5] bg-[#fff4f4] px-3 py-2 text-sm text-[#8f3131]">{error}</div> : null}
            <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
              <Button onClick={() => void handleSignIn()} disabled={submitting}>
                {submitting ? "Signing in…" : "Sign in"}
              </Button>
              <Button variant="secondary" onClick={() => void handleCreateAccount()} disabled={submitting}>
                Create account
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div>
      <div className="flex flex-wrap items-center justify-between gap-3 border-b border-line bg-white px-4 py-3 text-sm">
        <div className="flex items-center gap-2">
          <Badge variant="success">Authenticated</Badge>
          <span>{user.email ?? user.uid}</span>
          {backendProfile ? <Badge variant="accent">backend uid: {backendProfile.uid}</Badge> : null}
        </div>
        <Button variant="secondary" size="sm" onClick={() => void handleSignOut()}>
          Sign out
        </Button>
      </div>
      <AnalystWorkspace />
    </div>
  );
}
