---
date: '2026-03-03T16:00:00+08:00'
publishDate: '2026-03-03T16:00:00+08:00'
draft: false
title: 'EchoCenter'
description: 'A professional, modular intelligent agent management hub with real-time messaging and AI coordination.'
tags: ['project', 'go', 'react', 'ai', 'websocket']
lastmod: '2026-03-04T10:40:00+08:00'

---

## Overview

EchoCenter is a professional, modular intelligent agent management hub. It provides a centralized platform for agent registration, real-time bidirectional messaging via WebSocket, and intelligent command execution coordinated by the core **Butler** agent. The backend is built with testable modules (auth/config/repository), stricter repository error handling, and bilingual contributor documentation for smoother collaboration.

## Key Features

- **🤖 Multi-Agent Fleet**: Seamlessly manage and coordinate diverse AI agents (Python, Go, etc.).
- **⚡ Real-time Messaging**: Low-latency communication powered by a robust WebSocket implementation.
- **🧠 Butler Core**: An AI-driven coordinator that understands user intent and executes complex multi-agent workflows.
- **📊 Interactive Dashboard**: Modern React-based UI for monitoring agent status and system-wide logs.
- **🔒 Secure Architecture**: Mandatory JWT authentication and per-agent API tokens.
- **📂 Persistent History**: Full chat and command history stored in an optimized SQLite database with WAL mode.

## Tech Stack

| Backend | Frontend | Agents |
| :--- | :--- | :--- |
| **Go 1.22+** | **React 19** | **Python 3.9+** |
| Gin Gonic | TypeScript | OpenAI SDK |
| Gorilla WebSocket | Tailwind CSS (v4) | websockets |
| SQLite (WAL) | Zustand | psutil |
| Eino (AI Brain) | Shadcn/ui | python-dotenv |

## Quick Start

### Prerequisites

- **Go**: 1.22 or higher
- **Node.js**: 20 or higher (pnpm recommended)
- **Python**: 3.9 or higher

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/L-Rocket/EchoCenter.git
cd EchoCenter

# 2. Install all dependencies (Backend, Frontend, Python)
# This will also create backend/.env from .env.example
make install

# 3. Configure API Keys
# Edit backend/.env and add your BUTLER_API_TOKEN (e.g., from SiliconFlow or OpenAI)
# and ensure JWT_SECRET is set to a strong random string.

# 4. Launch with mock data and agents (recommended for first run)
make mock-start
```

Run `make help` to see all available commands.

The system will be available at `http://localhost:5173`. Default admin credentials: `admin` / `admin123`.

## Documentation

For detailed guides on architecture, API references, and agent integration, please visit the **[Official Documentation Site](https://l-rocket.github.io/EchoCenter/)**.

- [System Architecture](/architecture/overview)
- [API Reference](/api/authentication)
- [Agent Integration Guide](/development/agent-integration)
- [Development Setup](/development/setup)

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Links

- Code: https://github.com/L-Rocket/EchoCenter
- Documentation: https://l-rocket.github.io/EchoCenter/
- Issues: https://github.com/L-Rocket/EchoCenter/issues
