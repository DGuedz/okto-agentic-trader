import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        bg: {
          0: "#0B0D10",
          1: "#0F1115",
          2: "#13161D",
          glass: "rgba(255,255,255,0.04)",
        },
        surface: {
          card: "#12141A",
          cardHover: "#171A22",
          panel: "#0E1016",
        },
        text: {
          primary: "#EDEDED",
          secondary: "#A7ABB3",
          muted: "#7B808A",
          inverse: "#0B0D10",
        },
        border: {
          subtle: "rgba(255,255,255,0.06)",
          default: "rgba(255,255,255,0.10)",
          strong: "rgba(255,255,255,0.16)",
        },
        accent: {
          amber: {
            400: "#FDBA12", // Primary
            500: "#E7A600",
            glow: "rgba(253,186,18,0.22)",
          },
          neon: {
            400: "#33FF99", // Success/Status
            glow: "rgba(51,255,153,0.18)",
          },
        },
        state: {
          success: "#33FF99",
          warning: "#FDBA12",
          danger: "#FF4D4D",
          info: "#6EA8FF",
        },
      },
      fontFamily: {
        sans: ["var(--font-inter)"],
        mono: ["var(--font-jetbrains-mono)"],
      },
      boxShadow: {
        glowAmber: "0 0 30px rgba(253,186,18,0.22)",
        glowNeon: "0 0 26px rgba(51,255,153,0.18)",
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0) scale(1)' },
          '50%': { transform: 'translateY(-15px) scale(1.02)' },
        },
        undulate: {
          '0%, 100%': { transform: 'translateY(0) scale(1) rotate(0deg)' },
          '25%': { transform: 'translateY(-10px) scale(1.02) rotate(1deg)' },
          '75%': { transform: 'translateY(5px) scale(0.98) rotate(-1deg)' },
        },
        biolumPulse: {
          '0%, 100%': { opacity: '0.8', filter: 'brightness(1)' },
          '50%': { opacity: '1', filter: 'brightness(1.3) hue-rotate(15deg)' },
        },
        pulseSlow: {
          '0%, 100%': { opacity: '0.4' },
          '50%': { opacity: '0.7' },
        }
      },
      animation: {
        float: 'float 8s ease-in-out infinite',
        undulate: 'undulate 10s ease-in-out infinite',
        biolum: 'biolumPulse 4s ease-in-out infinite',
        pulseSlow: 'pulseSlow 6s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
    },
  },
  plugins: [],
};
export default config;
