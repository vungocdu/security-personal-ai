import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./lib/**/*.{ts,tsx}",
    "./__tests__/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        ink: "#11131A",
        mist: "#EFF2F7",
        sand: "#F7F3EC",
        slate: "#5A6472",
        line: "#D8DDE6",
        accent: "#9C6B30",
        accentSoft: "#F4E9DA",
        success: "#2F7D5C",
        warning: "#B36B27",
      },
      fontFamily: {
        sans: ["ui-sans-serif", "system-ui", "sans-serif"],
      },
      boxShadow: {
        panel: "0 12px 30px rgba(17, 19, 26, 0.06)",
      },
    },
  },
  plugins: [],
};

export default config;
