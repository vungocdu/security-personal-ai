import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "Security Personal AI Analyst Workspace",
  description: "Three-column analyst workstation for query-first RAG workflows.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="vi">
      <body>{children}</body>
    </html>
  );
}
