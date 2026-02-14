# 🚀 DEPLOYING OKTO LANDING PAGE TO VERCEL

This guide explains how to deploy the **Okto Agentic Interface** (located in `web/`) to Vercel for the **BNB Chain OpenClaw Hackathon**.

## 1. PRE-REQUISITES
- A [Vercel Account](https://vercel.com/signup).
- A [GitHub Account](https://github.com/).
- This repository pushed to your GitHub.

## 2. AUTOMATIC DEPLOYMENT (RECOMMENDED)
The easiest way is to use the "Deploy" button we added to `web/README.md`.

1. Go to `web/README.md` in your GitHub repository.
2. Click the **"Deploy with Vercel"** button.
3. Vercel will ask to clone the repository. Click **Create**.
4. Vercel will automatically detect the `web` folder as the root.
5. Click **Deploy**.

## 3. MANUAL DEPLOYMENT
If the button doesn't work or you prefer manual setup:

1. Log in to your [Vercel Dashboard](https://vercel.com/dashboard).
2. Click **"Add New..."** -> **"Project"**.
3. Import your `okto-juvenile-bnb` repository.
4. **IMPORTANT:** In the "Root Directory" settings, click **Edit** and select the `web` folder.
   - If you don't do this, the build will fail because it won't find `package.json` in the root.
5. Click **Deploy**.

## 4. POST-DEPLOYMENT (HACKATHON SUBMISSION)
Once deployed, you will get a URL like `https://okto-juvenile-bnb.vercel.app`.

1. Copy this URL.
2. Add it to your **DoraHacks Submission** under "Project Website" or "Demo Link".
3. Update the `HACKATHON_PITCH.md` with this link if desired.

## 5. ENVIRONMENT VARIABLES
The landing page is static and doesn't strictly require env vars for the UI. However, if you add backend features later:
- Go to Vercel Project Settings -> Environment Variables.
- Add any keys (e.g., `NEXT_PUBLIC_ANALYTICS_ID`).

---
*Built for BNB Chain OpenClaw Hackathon 2026*
