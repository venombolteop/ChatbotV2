<p align="center">
  <img src="https://te.legra.ph/file/b55448f8abd23f24ee425.jpg" width="400">
</p>

<h1 align="center">⚡ Venom Chatbot ⚡</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pyroblack-Layer%20227+-2196F3?style=flat-square&logo=telegram&logoColor=white">
  <img src="https://img.shields.io/badge/MongoDB-Async-47A248?style=flat-square&logo=mongodb&logoColor=white">
  <img src="https://img.shields.io/badge/TgCrypto-Fast%20Encryption-FF6F00?style=flat-square">
  <img src="https://img.shields.io/badge/License-MPL%202.0-brightgreen?style=flat-square">
</p>

<p align="center">
  <b>A self-learning Telegram chatbot that grows smarter with every conversation.</b><br>
  <i>No external AI APIs. No model hosting. Pure database-driven intelligence.</i>
</p>

---

<br>

<h3 align="center">✦ How It Works</h3>

<table align="center">
<tr>
<td width="50%" valign="top">

### 🧠 Learning Engine
Every conversation is an opportunity. When users chat in groups or DMs, the bot observes reply patterns and stores **trigger → response** pairs directly in MongoDB. The more it watches, the smarter it gets.

### 💬 Instant Replies
Incoming messages are matched against the learned response database using indexed lookups. No API calls, no latency — just fast, direct MongoDB queries returning the best match.

</td>
<td width="50%" valign="top">

### 🛡️ Built-in Protection
Links, URLs, and usernames are **silently filtered** before reaching the database. The chatbot only learns clean, organic conversation data — keeping the response pool high-quality.

### ⚙️ Zero Downtime Architecture
Built on `pyroblack` with `TgCrypto` C-extension encryption, async MongoDB via native `pymongo.AsyncMongoClient`, and a single global connection pool. Every handler is fully non-blocking.

</td>
</tr>
</table>

---

<br>

<h3 align="center">✦ Features</h3>

<p align="center">

| Feature | Description |
|---------|-------------|
| 🤖 Auto-Reply | Matches incoming messages against learned responses from MongoDB |
| 📚 Continuous Learning | Saves every conversation pair (text & stickers) for future matching |
| 🔕 Group Control | Admins can toggle the chatbot on/off per group via inline buttons |
| 🛡️ Spam Filter | Silently ignores messages containing links, URLs, or @usernames |
| ⚡ Hyper-Fast | Async I/O throughout — Pyrogram + TgCrypto + native async PyMongo |
| 📊 Stats | Owner-only `/stats` command to monitor served users and groups |
| 🔧 Eval/Shell | Owner-only `/eval` and `/sh` for remote code execution |

</p>

---

<br>

<h3 align="center">✦ Commands</h3>

<table align="center">
<thead>
<tr><th>Command</th><th>Scope</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td><code>/start</code></td><td>All</td><td>Welcome message with bot info</td></tr>
<tr><td><code>/help</code></td><td>All</td><td>Command list & usage guide</td></tr>
<tr><td><code>/chatbot</code></td><td>Group Admin</td><td>Toggle chatbot on/off for the group</td></tr>
<tr><td><code>/ping</code></td><td>All</td><td>Check bot response latency</td></tr>
<tr><td><code>/id</code></td><td>All</td><td>Get user, chat & message IDs</td></tr>
<tr><td><code>/stats</code></td><td>Owner</td><td>View total served users & groups</td></tr>
<tr><td><code>/eval</code></td><td>Owner</td><td>Execute Python code remotely</td></tr>
<tr><td><code>/sh</code></td><td>Owner</td><td>Execute shell commands remotely</td></tr>
</tbody>
</table>

---

<br>

<h3 align="center">✦ Architecture</h3>

```
Venom/
├── __init__.py              ← Pyrogram client + logging setup
├── __main__.py              ← Async entrypoint, index init, graceful shutdown
├── database/
│   ├── __init__.py          ← AsyncMongoClient pool, indexes, exports
│   ├── chats.py             ← Served chat CRUD (async)
│   └── users.py             ← Served user CRUD (async)
└── modules/
    ├── chatbot.py           ← Core engine: learn + respond + spam filter
    ├── callback.py          ← Inline button handler (admin toggles, UI nav)
    ├── start.py             ← /start, /help, /repo, welcome messages
    ├── ping.py              ← /ping with latency measurement
    ├── ids.py               ← /id with user/chat/message info
    ├── eval.py              ← /eval & /sh for owner
    ├── stats.py             ← /stats for owner
    └── helpers/
        ├── inline.py        ← Inline keyboard button layouts
        └── read.py          ← Static text templates
```

**Database Collections & Indexes:**
| Collection | Index | Purpose |
|---|---|---|
| `Anonymous.chatsdb` | `chat_id` (unique) | Track served groups |
| `Anonymous.users` | `user_id` (unique) | Track served users |
| `Word.WordDb` | `word` + compound `(word, text)` | Chatbot response lookup |
| `VickDb.Vick` | `chat_id` (unique) | Chatbot disable list |

---

<br>

<h3 align="center">✦ Deploy</h3>

<h4 align="center">Heroku</h4>
<p align="center">
  <a href="https://dashboard.heroku.com/new?template=https://github.com/venombolteop/ChatbotV2">
    <img src="https://img.shields.io/badge/Deploy%20to%20Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" width="260">
  </a>
</p>

<h4 align="center">Docker</h4>

```bash
docker build -t venom-chatbot .
docker run --env-file .env venom-chatbot
```

<h4 align="center">VPS / Local</h4>

```bash
# 1. Clone
git clone https://github.com/venombolteop/ChatbotV2 && cd ChatbotV2

# 2. Install dependencies
pip3 install -U -r requirements.txt

# 3. Configure environment
cp sample.env .env
# Edit .env with your values:
#   BOT_TOKEN    — from @BotFather
#   API_ID       — from my.telegram.org
#   API_HASH     — from my.telegram.org
#   MONGO_URL    — MongoDB connection string
#   OWNER_ID     — your Telegram user ID

# 4. Run
bash start
```

---

<br>

<h3 align="center">✦ Environment Variables</h3>

<table align="center">
<thead>
<tr><th>Variable</th><th>Required</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td><code>BOT_TOKEN</code></td><td>Yes</td><td>Bot token from <a href="https://t.me/BotFather">@BotFather</a></td></tr>
<tr><td><code>API_ID</code></td><td>Yes</td><td>From <a href="https://my.telegram.org/apps">my.telegram.org</a></td></tr>
<tr><td><code>API_HASH</code></td><td>Yes</td><td>From <a href="https://my.telegram.org/apps">my.telegram.org</a></td></tr>
<tr><td><code>MONGO_URL</code></td><td>Yes</td><td>MongoDB Atlas / self-hosted connection URI</td></tr>
<tr><td><code>OWNER_ID</code></td><td>Yes</td><td>Telegram user ID of the bot owner</td></tr>
<tr><td><code>OWNER_USERNAME</code></td><td>No</td><td>Owner's Telegram username (for credits)</td></tr>
<tr><td><code>SUPPORT_GRP</code></td><td>No</td><td>Support group username</td></tr>
<tr><td><code>UPDATE_CHNL</code></td><td>No</td><td>Update channel username</td></tr>
</tbody>
</table>

---

<br>

<h3 align="center">✦ Support</h3>

<p align="center">
  <a href="https://t.me/Venom_chatting">
    <img src="https://img.shields.io/badge/Support_Group-0088cc?style=for-the-badge&logo=telegram&logoColor=white" width="220">
  </a>
  &nbsp;&nbsp;
  <a href="https://t.me/TomatoFist">
    <img src="https://img.shields.io/badge/Updates_Channel-0088cc?style=for-the-badge&logo=telegram&logoColor=white" width="220">
  </a>
</p>

---

<p align="center">
  <sub>Built with ⚡ by <a href="https://t.me/K_4ip">K_4ip</a> — Powered by Pyroblack, PyMongo & TgCrypto</sub>
</p>
