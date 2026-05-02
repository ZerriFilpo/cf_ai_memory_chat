# cf_ai_memory_chat

An AI-powered chat assistant built on Cloudflare's developer platform. Users can have conversations with Llama 3.3, and the assistant remembers the conversation history across messages using Cloudflare KV.

**Live demo:** https://cf-ai-memory-chat-frontend.pages.dev

---

## Architecture

- **LLM** — Llama 3.3 via Cloudflare Workers AI
- **Backend** — Python Cloudflare Worker handles requests and coordinates the flow
- **Memory** — Cloudflare KV stores conversation history across messages
- **Frontend** — Static HTML/CSS/JS chat UI hosted on Cloudflare Pages

---

## Local Setup

1. Install Node.js and uv
2. Clone the repository
3. Inside `worker/`:
```bash
uv sync
pywrangler dev
```
4. Open `frontend/index.html` with a local server:
```bash
cd frontend && npx serve .
```

---

## Deploy

Deploy the Worker:
```bash
cd worker
npx wrangler deploy src/index.py --name cf-ai-memory-chat --compatibility-date 2026-04-30 --compatibility-flags python_workers
```

Deploy the frontend:
```bash
cd frontend
npx wrangler pages deploy . --project-name cf-ai-memory-chat-frontend
```

---

## How to Use

Open the live demo link above, type a message and press Enter or click Send. The assistant remembers your conversation for the duration of the session. Opening a new tab starts a fresh conversation.