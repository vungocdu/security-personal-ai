import { FirebaseApp, FirebaseOptions, getApp, getApps, initializeApp } from "firebase/app";
import { Auth, getAuth } from "firebase/auth";

function readEnv(name: string): string {
  return process.env[name]?.trim() ?? "";
}

const firebaseConfig: FirebaseOptions = {
  apiKey: readEnv("NEXT_PUBLIC_FIREBASE_API_KEY"),
  authDomain: readEnv("NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN"),
  projectId: readEnv("NEXT_PUBLIC_FIREBASE_PROJECT_ID"),
  appId: readEnv("NEXT_PUBLIC_FIREBASE_APP_ID"),
  messagingSenderId: readEnv("NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID"),
};

export function isFirebaseConfigured(): boolean {
  return Boolean(
    firebaseConfig.apiKey &&
      firebaseConfig.authDomain &&
      firebaseConfig.projectId &&
      firebaseConfig.appId &&
      firebaseConfig.messagingSenderId,
  );
}

export function getFirebaseApp(): FirebaseApp | null {
  if (!isFirebaseConfigured()) {
    return null;
  }
  return getApps().length > 0 ? getApp() : initializeApp(firebaseConfig);
}

export function getFirebaseAuth(): Auth | null {
  const app = getFirebaseApp();
  return app ? getAuth(app) : null;
}

export async function getFirebaseIdToken(): Promise<string | null> {
  const auth = getFirebaseAuth();
  const user = auth?.currentUser;
  if (!user) {
    return null;
  }
  return user.getIdToken();
}
