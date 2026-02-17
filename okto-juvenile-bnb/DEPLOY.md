# 🚀 Vercel Deployment Guide for Okto Juvenile

This project is structured as a monorepo with the Next.js application located in the `web` directory.

## ✅ Critical Configuration

When importing the project into Vercel, you **MUST** configure the **Root Directory**:

1.  Go to **Project Settings**.
2.  Find the **Root Directory** setting.
3.  Click **Edit** and select `web` (or enter `okto-juvenile-bnb/web` if importing from a larger repo).
4.  The framework should be auto-detected as **Next.js**.

## 🛠 Build Settings

-   **Build Command:** `next build` (default)
-   **Output Directory:** `.next` (default)
-   **Install Command:** `npm install` (default)

## 📦 Environment Variables

Ensure you have the following environment variables if needed (check `.env.example`):

-   `NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID` (if using WalletConnect)
-   `NEXT_PUBLIC_ALCHEMY_ID` (if using Alchemy)

## 🔍 Verification

After deployment:
1.  Visit the main URL (e.g., `https://your-project.vercel.app`).
2.  Verify the **Headless Liquidity Node** landing page loads.
3.  Check `/preview.html` for the static terminal demo.
4.  Check `/docs`, `/architecture`, and `/blog` for content access.

## 🚨 Troubleshooting

-   **404 on Homepage:** Double-check the **Root Directory** setting. If it's set to the project root instead of `web`, Vercel won't find the Next.js app.
-   **Missing Images:** Ensure all assets are in `web/public/assets`. We have updated paths to be relative for better compatibility.
