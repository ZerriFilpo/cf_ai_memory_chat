# PROMPTS.md

This file documents all AI prompts used during the development of cf_ai_memory_chat.

---

## 1. Repository scaffold

**Tool:** GitHub Copilot  
**Purpose:** Generate the initial folder structure and HTML design  
**Prompt:**
Create the file and folder structure for a Cloudflare Python Worker project called "cf_ai_memory_chat".

STRICT RULES — follow exactly:
- All files must be empty except frontend/index.html
- Do NOT write any Python code
- Do NOT write any JavaScript code
- Do NOT add any fetch() calls, event listeners, or logic of any kind
- Do NOT install packages or run any commands
- frontend/index.html is the ONLY file with content

FOLDER STRUCTURE:
cf_ai_memory_chat/
├── worker/
│   ├── src/
│   │   └── index.py          ← empty file
│   └── wrangler.toml         ← empty file
├── frontend/
│   └── index.html            ← see design spec below
├── README.md                 ← empty file
└── PROMPTS.md                ← empty file

DESIGN SPEC for frontend/index.html:
- Clean, modern chat interface
- Dark sidebar on the left with app name "cf_ai_memory_chat" and a "New Chat" button
- Main area on the right with a scrollable message display area at the top
- Chat bubbles: user messages aligned right with a dark background, assistant messages aligned left with a light background
- At the bottom: a text input field and a send button side by side
- Fully responsive layout using CSS flexbox or grid
- No external libraries, no CDN links, no JavaScript frameworks
- All CSS must be written inside a 
---

## 2. asyncio

**Tool:** Claude  
**Purpose:** Know if the asyncio module was needed  
**Prompt:**
Do I need to import asyncio for this project?

## 2. asyncio

**Tool:** Claude  
**Purpose:** How to handle http in the project 
**Prompt:**
I'm building a Cloudflare Python Worker that receives chat messages from a browser. I know Python's requests library for making HTTP calls, but I'm not sure what I need to handle incoming HTTP requests inside a Worker. Do I need to import anything to read the request body, check the method, and send a JSON response back? Or does the Workers runtime handle that?

## Notes

- All logic was written manually by the developer based on AI guidance
- AI was used for scaffolding, configuration syntax, and API reference
- The overall architecture and design decisions were made by the developer
