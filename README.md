<div align="center">

<img width="100%" alt="BCS Newspaper Engine — a daily grounded current-affairs briefing for BCS aspirants, delivered at 08:00 Asia/Dhaka" src="https://capsule-render.vercel.app/api?type=waving&color=0:6C2BD9,50:FF2E93,100:FFB703&height=230&section=header&text=BCS%20Newspaper%20Engine&fontSize=46&fontColor=ffffff&fontAlignY=32&animation=fadeIn&desc=Daily%20grounded%20BCS%20briefing%20%C2%B7%2008%3A00%20Asia%2FDhaka&descAlignY=58&descAlign=50&descSize=18"/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3600&pause=700&color=FFB703&center=true&vCenter=true&width=820&height=48&lines=Daily+BCS+current-affairs+briefing;Bengali+notes+grounded+in+the+article;Telegram+quizzes%2C+polls%2C+and+a+PDF;OpenAI%2C+with+free+Gemini+fallback;08%3A00+Asia%2FDhaka+%C2%B7+Friday+revision" />
  <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3600&pause=700&color=6C2BD9&center=true&vCenter=true&width=820&height=48&lines=Daily+BCS+current-affairs+briefing;Bengali+notes+grounded+in+the+article;Telegram+quizzes%2C+polls%2C+and+a+PDF;OpenAI%2C+with+free+Gemini+fallback;08%3A00+Asia%2FDhaka+%C2%B7+Friday+revision" />
  <img width="820" alt="Daily BCS current-affairs briefing. Bengali notes grounded in the article. Telegram quizzes, polls, and a PDF. OpenAI, with free Gemini fallback. 08:00 Asia/Dhaka, with a Friday revision." src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3600&pause=700&color=6C2BD9&center=true&vCenter=true&width=820&height=48&lines=Daily+BCS+current-affairs+briefing;Bengali+notes+grounded+in+the+article;Telegram+quizzes%2C+polls%2C+and+a+PDF;OpenAI%2C+with+free+Gemini+fallback;08%3A00+Asia%2FDhaka+%C2%B7+Friday+revision" />
</picture>

**A personal, cloud-run current-affairs briefing for Bangladesh Civil Service (BCS) preparation.**

<br/>

<img alt="Python 3.11 or newer" src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Telegram bot" src="https://img.shields.io/badge/Telegram-bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
<img alt="Runs on GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-scheduled-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"/>
<img alt="OpenAI is the primary model" src="https://img.shields.io/badge/OpenAI-primary-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img alt="Gemini is the free fallback" src="https://img.shields.io/badge/Gemini-fallback-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white"/>
<img alt="Reads RSS and Atom feeds" src="https://img.shields.io/badge/RSS%2FAtom-feeds-FFB703?style=for-the-badge&logo=rss&logoColor=1A1024"/>
<img alt="Tested with pytest" src="https://img.shields.io/badge/pytest-tested-6C2BD9?style=for-the-badge&logo=pytest&logoColor=white"/>

<br/>

<img alt="Target delivery time 08:00 Asia/Dhaka" src="https://img.shields.io/badge/08%3A00-Asia%2FDhaka-FFB703?style=for-the-badge"/>
<img alt="Study notes are written in Bengali" src="https://img.shields.io/badge/Notes-Bengali-6C2BD9?style=for-the-badge"/>
<img alt="Telegram quiz polls and a PDF edition" src="https://img.shields.io/badge/Quizzes_%2B_PDF-FF2E93?style=for-the-badge"/>

<br/>

<a href="#overview">Overview</a> ·
<a href="#briefing">A briefing</a> ·
<a href="#features">Features</a> ·
<a href="#stack">Stack</a> ·
<a href="#setup">Setup</a> ·
<a href="#subscribers">Subscribers</a> ·
<a href="#configuration">Configuration</a> ·
<a href="#usage">Usage</a> ·
<a href="#sources">Sources</a> ·
<a href="#selection">Selection</a> ·
<a href="#grounding">Grounding</a> ·
<a href="#cost">Cost</a> ·
<a href="#credits">Credits</a>

</div>

> [!CAUTION]
> **Make this repository private before the first live run.** The workflow commits `state/state.json`, which records what was read each day **and subscribers' Telegram chat ids and first names**. It contains no credentials, but it must not be public. Private repositories on GitHub Free include 2,000 Actions minutes a month. This schedule uses about **1,100–1,800** of them. See [Cost](#cost).

---

<a id="overview"></a>

## 📰 Overview

Every morning (target **08:00 Asia/Dhaka**) a GitHub Actions job builds one edition and sends it on Telegram.

1. **Collect** recent news from verified RSS/Atom feeds. The same feeds are read several times during the day, with no AI calls, because a feed only shows its newest items.
2. **Merge** duplicate reports of the same event.
3. **Screen** stories for BCS relevance. OpenAI is the default. Gemini's free tier is the automatic fallback. Screening is one lightweight call per batch.
4. **Read** the accessible article text and write **grounded Bengali study notes**.
5. **Rank** with a configurable rubric: **5–8** stories on a normal day, fewer on a thin day, never padded.
6. **Write three validated MCQs** from verified facts, sent as **Telegram quiz polls** (tap an answer, see right/wrong and the explanation at once).
7. **Send one organised edition** to everyone who subscribed (and, optionally, a public channel), then a short "which stories were useful?" poll and a **PDF copy**.

Every **Friday** the edition adds a **weekly revision** of the week's must-remember facts, with **10 extra MCQs**. On the **1st of each month** it also sends a **monthly current-affairs PDF** of the previous month. The owner gets a private weekly health report.

Expected model cost: roughly **US$2–8 per month (≈ ৳250–1,000)** of prepaid OpenAI credit, depending on the model. If the credit runs out, the free Gemini fallback takes over, so the briefing keeps coming. GitHub Actions and Telegram are free. Details in [Cost](#cost).

> [!TIP]
> No keys yet? `python -m app run --offline` renders a full sample edition (text and, if Chrome or Chromium is installed, the PDF) from bundled fictional data.

---

<a id="briefing"></a>

## ✨ What a briefing looks like

```
📰 বিসিএস দৈনিক ব্রিফিং — ২৩ অক্টোবর ২০২৬
📚 ৬টি খবর · ⏱ পড়তে প্রায় ১০ মিনিট
আজকের শিরোনাম                     ← index of the day's headlines
১. … ২. … ৩. …

১. <headline stating the core fact, in Bengali>
🏷 অর্থনীতি | প্রিলি + লিখিত | স্কোর ৭৪/১০০
📰 The Daily Star, প্রথম আলো · ২২ অক্টোবর ২০২৬
🎯 সিলেবাস: বাজেট, রাজস্ব, এডিপি ও সরকারি ঋণ
কী ঘটেছে: …                       ← summary grounded in the article
🆕 নতুন কী: … (আগের খবর: …)          ← only for a follow-up of an earlier story
📌 প্রিলির জন্য মনে রাখুন (প্রতিবেদন থেকে): • … (at most 3)  ← each fact matched to a quote in the article
আরও তথ্য (প্রতিবেদন থেকে): • …
উদ্ধৃত দাবি (যাচাইকৃত তথ্য নয়): • X: …
বিসিএস-এ কেন গুরুত্বপূর্ণ: …
✍️ লিখিত উত্তরের পয়েন্ট (AI বিশ্লেষণ): • … • …   ← clearly labelled analysis
📚 প্রাসঙ্গিক সাধারণ জ্ঞান (প্রতিবেদনের বাইরের তথ্য; AI দুইবার আলাদাভাবে মিলিয়ে দেখেছে …): • …
📝 সম্ভাব্য লিখিত প্রশ্ন: …
🔗 The Daily Star | প্রথম আলো
🏛 দাপ্তরিক সূত্রে যাচাই: Bangladesh Bank

… more stories …

📅 সাপ্তাহিক রিভিশন (Fridays)      ← the week's top stories: 📌 facts and 📚 GK, then 10 MCQs (answers in spoilers)

🧠 আজকের অনুশীলনী: নিচে ৩টি কুইজ
[quiz poll] প্রশ্ন ১. …           ← tap an answer: Telegram shows right/wrong and the 💡 explanation
[quiz poll] প্রশ্ন ২. …
[quiz poll] প্রশ্ন ৩. …
[poll] 📊 আজকের কোন খবরগুলো আপনার প্রস্তুতিতে কাজে লাগবে?   ← anonymous; results go into the owner's report
```

A question too long for Telegram's quiz limits (300 characters, options 100) is sent as text with the answer in a spoiler instead. Turn quizzes or the feedback poll off with `telegram.mcq_as_quiz` / `telegram.feedback_poll`.

After the messages and polls, each subscriber also receives `BCS-Briefing-<date>.pdf`. On Fridays that PDF includes the weekly revision pages. On the 1st it is joined by `BCS-Monthly-<YYYY-MM>.pdf`, the previous month's facts and GK grouped by subject. The edition is laid out for A4 (good for printing or saving), with the must-remember facts and related GK highlighted, the MCQ answers on a separate page, and a one-page **revision sheet** (every 📌 fact and 📚 GK item of the day) at the end.

---

<a id="features"></a>

## ⚡ Key features

| | Feature | What it does |
|---|---|---|
| 🗞️ | Verified feeds | RSS/Atom only, with `robots.txt`, timeouts, and size caps. Daytime collection uses no model calls. |
| 🧹 | One event, one note | Same URL, title, or excerpt collapses into a single story. A story is never sent twice. |
| 🎯 | Five syllabus gates | Section filters, a syllabus topic, story-type bans, a score floor, and diversity caps. Code enforces every gate. |
| 📝 | Grounded Bengali notes | Every key fact needs a verbatim quote. Sentences with numbers that are not in the article are removed. |
| 🧠 | Three quiz polls | MCQs must cite a verified fact. Telegram shows right/wrong and the explanation. Fewer than three valid questions means fewer are sent. |
| 📊 | Feedback poll | Anonymous "which stories helped?" poll. Results land in the owner's Friday report. |
| 📄 | PDF edition | Headless Chrome, Noto fonts for Bengali, sent after the text. Best effort: if it fails, the text edition still goes out. |
| 📅 | Friday and the 1st | Weekly revision (15 stories, 10 MCQs) and a monthly PDF of the previous month. |
| 🕗 | Held until 08:00 | Built once a tick lands after 05:00, released at 08:00 Asia/Dhaka, at most once a day. |
| 🛟 | OpenAI, then Gemini | Prepaid OpenAI by default. Free-tier Gemini takes over when credit, the key, or the model fails. |
| 👥 | Public bot, optional channel | `/start` subscribes. An invite code can close it. A channel post reaches any number of readers at once. |

---

<a id="stack"></a>

## 🧰 Tech stack

<div align="center">

<img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white"/>
<img alt="Telegram" src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
<img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img alt="Gemini" src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white"/>

</div>

| Piece | What this repo uses |
|---|---|
| Language | Python **3.11+**. GitHub Actions installs **3.12**. |
| HTTP and parsing | `requests`, `feedparser`, `beautifulsoup4` (pinned in `requirements.txt`). No provider SDKs: OpenAI and Gemini are plain REST. |
| Tests | `pytest` (`requirements-dev.txt`). Unit tests mock every external call. |
| Models | OpenAI `gpt-5.4-mini` (override with `OPENAI_MODEL`). Fallback `gemini-3.8-flash` (override with `GEMINI_MODEL`). Optional local [Ollama](#local-model). |
| Delivery | Telegram Bot API. Optional public channel. |
| PDF | Headless Chrome or Chromium, plus a Bengali font (Noto). `CHROME_PATH` picks the browser. |
| Schedule | `.github/workflows/daily-briefing.yml`. Optional free trigger on [cron-job.org](https://cron-job.org). |
| Config | TOML in `config/`. Secrets only from the environment. |

Model ids and the prices in [Cost](#cost) came from third-party trackers and could not be confirmed on the vendors' own pages from the build environment. Check [OpenAI pricing](https://openai.com/api/pricing), the [OpenAI models docs](https://platform.openai.com/docs/models), [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing), and [Gemini rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) before you rely on them.

---

<a id="pdf"></a>

## 📄 Scheduled runs, manual runs, and the PDF

| Run | Limit | What it sends |
|---|---|---|
| Scheduled (08:00) | Once per day. Re-runs never duplicate. | The daily edition |
| Manual `live` (Run workflow) | **Unlimited** | An **extra edition** ("🔄 অতিরিক্ত আপডেট") with stories that are **new since the last edition** |

- A story is never sent twice. If nothing new has turned up, a manual run sends a short "সর্বশেষ ব্রিফিংয়ের পর নতুন কোনো প্রাসঙ্গিক খবর পাওয়া যায়নি" note, so you can see it worked.
- A manual run before 08:00 does not stop the scheduled edition. That one then carries only what is new.
- If an earlier edition today was interrupted, a manual run finishes delivering it first.
- **Cost.** A manual run only analyses *new* articles. Each one is still a few OpenAI calls (about **$0.01–0.10**, depending on how much is new).
- Locally: `python -m app run --manual`.

**The PDF**

- Headless Chrome or Chromium renders the same notes. GitHub-hosted runners have Google Chrome. The workflow installs `fonts-noto-core` so Bengali renders.
- It is sent **after** all text messages, per subscriber, and tracked like a message. A retry sends only what is missing. If the file is gone on a later run, it is rebuilt from saved state.
- Best effort. If it cannot be made (no browser, font problem), the text edition is still sent and the run log and state record `pdf_error`.
- No PDF is sent for an empty "nothing new" edition or a failure notice.
- Turn it off with `python -m app run --no-pdf`. Point at a browser with `CHROME_PATH`.
- The PDF HTML escapes all article and model text. A Content-Security-Policy blocks scripts and external loads.

---

<a id="architecture"></a>

## 🏗️ Architecture

```
        ┌──── GitHub Actions: 30-min ticks → gate → build ≥05:00, send at 08:00 ─┐
        │                                                                       │
 RSS ──▶│ A. collector.py   fetch feeds (robots.txt, timeouts, size caps)       │
 feeds  │        │          normalise URLs, parse dates safely                  │
        │ B. deduplicator.py  same URL / title / excerpt → one "event"          │
        │        │                                                              │
        │ C. screening.py   batched AI calls: relevance, categories, grouping   │──▶ OpenAI API
        │        │          (the model may only reference ids we gave it)       │    (prepaid)
        │ D. extractor.py   fetch article page, strip nav/ads/related blocks    │
        │        │          → full text, or labelled excerpt-only, or skip      │
        │ F. analysis.py    1 AI call per story → JSON note                     │──▶  (Gemini API if
        │      grounding.py drop facts whose quote isn't in the article and     │
        │        │          sentences with numbers not in the article           │
        │ E. scoring.py     weighted rubric → top 5–8 above threshold           │
        │ G. questions.py   1 AI call → MCQs, strictly validated                │──▶  OpenAI fails)
        │        │                                                              │
        │    render.py      Bengali, HTML-escaped, phone-friendly sections      │
        │    subscribers.py read /start & /stop (getUpdates), update the list   │◀─▶ Telegram
        │    telegram_delivery.py  chunk ≤3800 chars, send to every subscriber, │──▶ Telegram
        │                   record message ids per subscriber                   │
        │        │                                                              │
        │    state.py       state/state.json (atomic, versioned), checkpointed  │
        │                   after every stage and every story                   │
        └────────┬──────────────────────────────────────────────────────────────┘
                 ▼
        git commit state/state.json → your repository (memory between runs)
```

A normal day is about **19–26 model requests**: up to **4** screening calls (160 candidates, batches of 40), up to **16** analyses, static-GK proposal and a blind check (a second round is possible), and **1** MCQ call. Fridays add one weekly-MCQ call. Each provider is hard-capped at **`llm.max_calls_per_run` (36)** per run, retries included.

<a id="structure"></a>

### 📁 Project structure

| Path | Purpose |
|---|---|
| `app/__main__.py` | CLI. Run `python -m app` plus a command. |
| `app/config.py` | Loads `config/settings.toml` and environment secrets |
| `app/sources.py` | Source registry (`config/sources.toml`) |
| `app/syllabus.py` | BCS syllabus profile (`config/syllabus.toml`) |
| `app/http.py` | Polite fetcher: `robots.txt`, timeouts, size caps, bounded retries |
| `app/collector.py` | Stage A — feeds → items |
| `app/deduplicator.py` | Stage B — duplicate detection, event grouping |
| `app/screening.py` | Stage C — relevance screening. Unknown model ids are ignored. |
| `app/extractor.py` | Stage D — article text, excerpt-only decision |
| `app/scoring.py` | Stage E — rubric scoring and ranking |
| `app/analysis.py`, `app/grounding.py` | Stage F — study notes and evidence checks |
| `app/enrichment.py` | Related static GK, proposed and then checked blind |
| `app/questions.py` | Stage G — MCQ generation and validation |
| `app/render.py` | Telegram HTML (Bengali). Model text is escaped. |
| `app/pdf.py` | Edition PDF via headless Chrome |
| `app/revision.py` | Weekly revision and the monthly PDF, from stored digests |
| `app/telegram_delivery.py` | Chunking, sending, retries |
| `app/subscribers.py` | `/start`, `/stop`, optional invite code, subscriber list |
| `app/schedule_gate.py` | What a 30-minute tick should do. Standard library only. |
| `app/pipeline.py` | Orchestration, checkpoints, idempotency |
| `app/state.py` | Versioned JSON state store |
| `app/prompts.py` | Prompts with untrusted-content guards |
| `app/llm/` | `openai.py`, `gemini.py`, `ollama.py` (local), `mock.py` (offline and tests), shared client in `base.py` |
| `app/util.py` | Time, hashing, URL and text helpers |
| `config/` | `settings.toml`, `sources.toml`, `syllabus.toml` |
| `state/state.json` | Created by the first live run, committed by the workflow |
| `sample_data/` | Fictional feeds and articles for offline runs and tests |
| `assets/` | Project logo (SVG and PNG) |
| `tests/` | Pytest suite. External calls are mocked. |
| `.github/workflows/daily-briefing.yml` | Schedule, manual modes, state commit |

---

<a id="setup"></a>

## 🚀 Getting started

Allow about **20–30 minutes**. Do the steps in order. The cloud workflow does not need your computer. Local install is under [Usage](#usage).

### Step 0 — Make the repository private

GitHub → your repository → **Settings → General** → **Danger Zone** → **Change repository visibility** → **Make private**.

`state/state.json` holds reading history and subscribers' chat ids and first names. No credentials, and still not something to publish.

### Step 1 — Put the code on the default branch

GitHub only runs **scheduled** workflows from the repository's **default branch** (`main`).

- If this code is on another branch, open a pull request into `main` and merge it. If `main` does not exist yet, create it from that branch: **Code → branch dropdown → View all branches → New branch** (name `main`, source = the code branch). Then set it as default under **Settings → General → Default branch**.
- If you protect `main` with rules that block direct pushes, the workflow cannot commit state. Either allow `github-actions[bot]` to bypass, or do not protect `main` (this is a personal repo).

### Step 2a — Create an OpenAI API key (primary model, prepaid)

1. Go to <https://platform.openai.com/>, sign in, open **Settings → Billing**, and **add prepaid credit**. US$5–10 lasts about 1–4 months. You need a card that works for international online payments.
2. **Turn auto-recharge OFF.** Then the most you can ever spend is the credit you added. When it runs out, OpenAI refuses requests and the app switches to Gemini.
3. Optional extra guard: **Settings → Limits** → set a monthly budget and an email alert.
4. **API keys → Create new secret key.** Copy it (it starts with `sk-`). That value is `OPENAI_API_KEY`.
5. **Check the model and price.** The default in `config/settings.toml` is `gpt-5.4-mini`. A cheaper option is `gpt-5.4-nano`. Those ids, and the prices in [Cost](#cost), were taken from third-party trackers and could not be confirmed on OpenAI's site from the build environment. Check <https://openai.com/api/pricing> and <https://platform.openai.com/docs/models>. To change the model without editing code, set the repository variable `OPENAI_MODEL` (Step 4). If the price differs, update `openai_usd_per_million_input` / `output` so the logged cost estimate stays right.
6. Data use: OpenAI states API inputs are not used for training by default. Only public news text is sent.

### Step 2b — Create a Gemini API key (free fallback)

1. Go to **Google AI Studio → API keys**: <https://aistudio.google.com/apikey> and sign in.
2. Click **Create API key**. Prefer **a new Google Cloud project with no billing account**.
   - Projects **without** billing stay on the **Free** tier. When the free quota runs out, requests fail with HTTP 429 and this app produces a partial edition. It never pays.
   - Linking billing moves the project to a paid tier. Do not link billing unless you intend to pay.
3. Copy the key. You will paste it into GitHub in Step 4.
4. **Check the model.** The default is `gemini-3.8-flash` (`config/settings.toml`). Third-party pricing summaries from October 2026 list it as free-tier eligible, but **this could not be confirmed against Google's own pages from the build environment**. Open <https://ai.google.dev/gemini-api/docs/pricing> and <https://ai.google.dev/gemini-api/docs/rate-limits> and confirm:
   - the model shows "Free of charge" in the Free Tier column, and
   - its free requests-per-day limit is comfortably above ~16.

   If it is not, choose a free Flash or Flash-Lite model and set `GEMINI_MODEL` (Step 4).
5. Privacy: on the free tier, Google states prompts and responses may be used to improve its products. The app only sends public news text, never personal data.

### Step 3 — Create the Telegram bot

1. In Telegram, open **@BotFather** → `/newbot` → choose a name and a username ending in `bot` (for example `bcs_daily_brief_bot`).
2. BotFather replies with a **token** like `123456789:AAH…`. That is `TELE_BOT_TOKEN`. Treat it like a password.
3. Optional but recommended: in BotFather, `/setcommands` → your bot → paste:

   ```
   start - ব্রিফিং চালু করুন
   stop - ব্রিফিং বন্ধ করুন
   help - সাহায্য
   ```

4. The bot is **public**: anyone who opens `https://t.me/<your_bot_username>` and presses **Start** is subscribed, with no limit on numbers. To make it private, set `require_invite_code = true` (and optionally `max_subscribers`) under `[telegram]` in `config/settings.toml`, and add a `BOT_INVITE_CODE` secret: 8–64 characters of `A-Z a-z 0-9 _ -`. Then only `https://t.me/<your_bot_username>?start=<your_invite_code>` works.

There is no chat id to look up. The bot learns who to send to when people press **Start**. See [Subscribers](#subscribers).

### Step 4 — Add GitHub secrets and optional variables

Repository → **Settings → Secrets and variables → Actions**.

**Secrets** → **New repository secret**:

| Name | What to put |
|---|---|
| `OPENAI_API_KEY` | Key from Step 2a (primary model) |
| `GEMINI_API_KEY` | Key from Step 2b (free fallback) |
| `TELE_BOT_TOKEN` | Token from Step 3 |
| `BOT_INVITE_CODE` | Only if you close the bot (Step 3). Ignored while it is public. |

Optional, on the **Variables** tab:

| Name | What it overrides |
|---|---|
| `OPENAI_MODEL` | `llm.openai_model` |
| `GEMINI_MODEL` | `llm.gemini_model` |
| `TELE_CHANNEL_ID` | Public channel that also receives every edition (`@name`) |
| `TELE_OWNER_CHAT_ID` | Chat that receives crash notices and the weekly owner report |

You can run with one AI key. Without `OPENAI_API_KEY` the app uses Gemini only (free). Without `GEMINI_API_KEY` it uses OpenAI only (no fallback).

Secrets are masked in logs. This app also redacts them from its own messages. Names only: never commit a `.env` or paste a live key into the repo. `.env.example` lists the same names with placeholders.

### Step 5 — Enable GitHub Actions

1. **Settings → Actions → General → Actions permissions**: "Allow all actions and reusable workflows", or at least the GitHub-authored actions this workflow uses (`actions/checkout`, `actions/setup-python`, `actions/upload-artifact`).
2. Same page, **Workflow permissions**: the default ("Read repository contents") is enough. The workflow requests `contents: write` itself, and nothing else.
3. Open the **Actions** tab. If GitHub shows "Workflows aren't being run on this repository", click **I understand… enable them**.

### Step 6 — Verify with manual runs, in this order

**Actions → Daily BCS briefing → Run workflow** → pick a **mode** → **Run workflow**.

| # | Mode | What it proves | Uses quota / sends? |
|---|---|---|---|
| 1 | `offline` | Code, tests, and rendering work | No API calls, nothing sent |
| 2 | `verify-sources` | Each feed is reachable, allowed by `robots.txt`, and parses | Fetches feeds only |
| 3 | `check-model` | Both keys work and both model ids exist | 1 metadata call each (no generation, no cost) |
| 4 | `subscribers` | You (and friends) open the bot and press **Start**. This run registers you, sends a welcome, and lists who is subscribed | Welcome replies only |
| 5 | `test-telegram` | Delivery works for every subscriber | 1 test message per subscriber |
| 6 | `dry-run` | Full real pipeline. Download the artifact to read the edition. The summary shows tokens and estimated cost | ~11 OpenAI calls (≈ $0.05–0.25), **nothing sent**, saved state untouched |
| 7 | `live` | The real thing | Sends an edition (text + PDF) to every subscriber and commits state. Run it **as often as you like**: each manual run sends whatever is new since the last edition |

After `verify-sources`, edit `config/sources.toml`: set `enabled = false` for any source that does not show `OK`, and update its `verification` note. See [News sources](#sources).

### Step 7 — Let the schedule run

**How 08:00 delivery works.** GitHub's built-in timer is unreliable. On this repository, scheduled runs have started **4–6 hours late every day** (a run set for 08:00 started at 11:00–13:00), by a different amount each day, so a fixed clock time cannot hit 08:00. The workflow therefore fires a cheap **tick every 30 minutes**, from 00:07 to 08:37 Dhaka nominal time (18 cron lines, 18:07–02:37 UTC). Each tick starts hours late, and that is fine.

Each tick first runs a tiny **gate** (`app/schedule_gate.py`). It takes a few seconds, needs no `pip install`, and reads the saved state and the Dhaka clock:

| Dhaka time when the tick actually starts | Today's edition | What happens |
|---|---|---|
| before 05:00 | — | nothing (tonight's news is not in yet) |
| 05:00–08:00 | not built | **build** it (collect, analyse, text + PDF) and **hold** it |
| 05:00–08:00 | built, 08:00 more than 30 min away | nothing |
| 07:30–08:00 | built (or built now) | the job **waits** and sends at **08:00** |
| 08:00–22:00 | built, or not yet built | **send** (building first if needed) |
| any | already sent, or 5 failed runs already today | nothing |

- Ticks with nothing to do stop after the gate: no Python setup, no state commit, one billed Actions minute.
- **Collecting through the day.** Feeds only show their newest ~10–60 items, so reading them once a morning missed most of the day's news. A tick with no briefing work instead runs `collect` (feeds into state, no AI calls) when the last collection is at least `schedule.collect_every_hours` (4) old. Three extra daytime ticks (13:07, 17:07, 21:07 Dhaka nominal) make sure that happens. Those runs also read new `/start` messages, so welcomes go out within a few hours.
- The edition is still sent **at most once per day**. The briefing job always reads the latest saved state (not the commit it was queued with), so a late or queued run cannot send it twice.
- A persistent failure stops after `schedule.max_runs_per_day` (5) failed runs. A built edition gets twice that many tries to go out. Subscribers get a crash notice only on the day's last chance, or once it is 2+ hours past 08:00.
- The gate writes a notice on every tick, for example `RUN: deliver the held edition [tick '7 21 * * *' started 02:11 UTC (08:11 local), 5 h 04 min after it was due]`. Runs record their lag in `state.json` (`schedule.days`). That is how you see how late GitHub is.
- Times and limits live in `config/settings.toml` under `[schedule]`.
- **Actions minutes:** about 21 gate minutes, ~5 one-minute collections, and ~10–35 minutes of briefing work and waiting a day, ≈ **1,100–1,800** of the 2,000 free minutes a month on a private repository. Lower `collect_every_hours` costs more. Set it to `0` to turn collection off.

With GitHub alone, the briefing arrives at 08:00 when a tick lands in the half hour before 08:00 (normally every day, with ticks every 30 minutes). Otherwise it arrives on the first tick after 08:00. **For 08:00 every single day, add the free external trigger below.** Manual and API-started runs are not delayed the way scheduled ones are.

If you sent a manual edition before the scheduled one and nothing new has appeared since, the scheduled run does not message anyone.

### Exact 08:00 with a free external trigger (recommended)

[cron-job.org](https://cron-job.org) is free and fires on the minute. It calls GitHub's API to start the workflow in `deliver` mode. That run builds the edition if no tick has yet, waits until 08:00 if it is a little early, and sends it.

1. **Create a GitHub token that can only start this workflow.**
   - GitHub → your avatar → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
   - Name: `bcs-08-trigger`. Expiration: 1 year (set a reminder to renew).
   - **Repository access → Only select repositories → `fr-ost/NEWSPAPER-ANALYZER`** (this repository).
   - **Permissions → Repository permissions → Actions: Read and write**. Leave everything else as "No access".
   - Generate, then copy the token (it starts with `github_pat_`).
2. **Create the timer at cron-job.org.** Sign up (free), then **Create cronjob**:
   - **URL:** `https://api.github.com/repos/fr-ost/NEWSPAPER-ANALYZER/actions/workflows/daily-briefing.yml/dispatches` (use the repository's current name; if you rename it, update this URL)
   - **Schedule:** every day at **07:45**, time zone **Asia/Dhaka**. If the edition is already built, the run waits and sends it at 08:00. If not, it builds it (3–5 minutes), then waits and sends it at 08:00.
   - **Advanced → Request method:** `POST`
   - **Headers:**
     - `Authorization`: `Bearer github_pat_…your token…`
     - `Accept`: `application/vnd.github+json`
     - `X-GitHub-Api-Version`: `2022-11-28`
   - **Request body:** `{"ref":"main","inputs":{"mode":"deliver"}}`
   - Save, then use **Test run**. GitHub returns **204 No Content** when it works, and a `deliver` run appears under Actions. That run does nothing if today's edition was already sent, so testing is safe.
3. The GitHub ticks stay as backups. If cron-job.org is down, the next tick still sends the edition.

The token can only start or read workflow runs in this one repository. It cannot read your code or secrets. If it leaks, delete it under Developer settings and make a new one.

GitHub does not guarantee when scheduled runs start. Here they start hours late. If you need the briefing right now, run `live` manually. A re-run of the *scheduled* job never sends a duplicate. *Manual* runs send extra editions with only new stories.

### Setup checklist

- [ ] Repository made **private**
- [ ] Code merged into the **default branch** (`main`)
- [ ] OpenAI credit added, **auto-recharge off**, API key created; model id and price checked
- [ ] Gemini key created in a project **without billing**; the model's free-tier status confirmed on Google's pricing page
- [ ] Telegram bot created
- [ ] Secrets `OPENAI_API_KEY`, `GEMINI_API_KEY`, `TELE_BOT_TOKEN` added, and `BOT_INVITE_CODE` if the bot is closed
- [ ] You and your friends opened the bot and pressed **Start**
- [ ] Actions enabled
- [ ] Manual runs: `offline` → `verify-sources` (and adjust `sources.toml`) → `check-model` → `subscribers` → `test-telegram` → `dry-run` → `live`
- [ ] Next morning: the briefing arrives and a `state: run for …` commit appears

---

<a id="subscribers"></a>

## 👥 Subscribers

The bot is public and sends the same edition to every subscriber. There is no fixed chat id and no always-on server.

**How someone joins**

1. Share `https://t.me/<your_bot>` anywhere. Anyone can join. Old invite links keep working too.
2. They open it in Telegram and press **Start**.
3. The bot reads new messages at its **next run** (a collection run every few hours, the morning run, or immediately if you run `subscribers`), adds them, and replies "✅ … যুক্ত করা হয়েছে".
4. From the next edition on, they receive the daily briefing. Someone who joins after today's edition went out gets tomorrow's.

**Commands:** `/start` join · `/stop` leave · `/help`. A person who **blocks** the bot or deletes the chat is removed automatically. That never stops delivery to the others.

**Timing.** The bot only reads messages when the workflow runs (collection about every 4 hours, plus the morning run). Telegram keeps unread messages for **24 hours**, so a welcome can take a few hours. If someone did not get one, have them press Start again and run `subscribers` from the Actions tab.

**Groups.** Add the bot to a Telegram group and send `/start` (or `/start@your_bot`) there. The whole group counts as one subscriber.

**Limits, speed, and privacy**

- **No subscriber limit** (`telegram.max_subscribers = 0`). Set a number to cap it. `require_invite_code = true` admits only the invite link.
- **Delivery.** Each part of the edition goes to everyone in turn (part 1 to all, then part 2, …), in parallel (`send_workers`, 8), capped at `max_messages_per_second` (25), under Telegram's free broadcast limit of about 30 messages a second. The PDF is uploaded once and then re-sent by file id. An edition is about **8–10 messages**, so expect roughly **1,000 subscribers in 6–7 minutes** after 08:00. The last people get it a little later than the first. Several thousand subscribers still fit in the job's 90-minute limit but use more Actions minutes. Far beyond that, Telegram's paid broadcast option would be needed.
- **Welcomes are not instant.** Messages are read only when the workflow runs. An always-on bot (a webhook on a free serverless host) would reply at once, but needs a separate server. A channel avoids the wait entirely.
- State stores each subscriber's chat id, first name (so you can see who joined), join and leave time, and per-edition delivery status. Nothing else. This is why the repository must stay private. Per-message delivery details are dropped once an edition is fully delivered, to keep the file small.
- **Who is subscribed:** run `subscribers` (count and the newest 30) or `status`. **To remove someone:** ask them to send `/stop`, or set their entry's `"status"` to `"inactive"` in `state/state.json` and commit. **To close the bot:** set `require_invite_code = true` and a `BOT_INVITE_CODE` secret. Existing subscribers stay.

**A public Telegram channel (recommended for a large audience).** A channel post reaches any number of readers at once, with no rate limits. People join instantly, and the channel keeps a searchable archive.

1. In Telegram: **New Channel** → name it (for example "বিসিএস দৈনিক ব্রিফিং") → **Public** → pick a link, for example `t.me/bcs_daily_brief`.
2. Channel → **Administrators** → **Add Admin** → search your bot (`@BCSNWZ_bot`) → allow **Post Messages**.
3. GitHub → Settings → Secrets and variables → Actions → **Variables** → `TELE_CHANNEL_ID` = `@bcs_daily_brief`.

From the next edition, every message, quiz, and PDF also goes to the channel, and the welcome message links to it. Private-chat delivery continues (`telegram.dm_subscribers = true`). Set that to `false` to post only to the channel. If posting fails (the bot is not an admin), subscribers still get their editions. The error is in the run log and the owner's report.

**The owner.** Technical failure notices ("a run crashed") and a **weekly health report** (Fridays) go only to `telegram.owner_chat_id` (your chat; override with the `TELE_OWNER_CHAT_ID` repository variable), never to subscribers. The report lists the week's delivery times, GitHub's start delays, failed runs, estimated OpenAI cost, subscriber changes, failing sources, the last collection, static-GK coverage, the stories readers voted most useful, and quiz accuracy. If a whole edition cannot be built (all sources down, both AI providers out), subscribers still get the short "couldn't make today's briefing" notice.

**Delivery is tracked per subscriber.** If sending fails for one person, the others are unaffected. The next run sends that person only the messages they are missing. The edition is marked delivered once every active subscriber has it.

---

<a id="configuration"></a>

## 🔐 Configuration

Secrets and overrides come from the environment. Nothing secret belongs in `config/` or in git. `.env` is git-ignored. Copy `.env.example` to `.env` for local runs and fill it in there.

| Variable | Kind | Role |
|---|---|---|
| `OPENAI_API_KEY` | Secret | Primary model. Prepaid credit. Keep auto-recharge off. |
| `GEMINI_API_KEY` | Secret | Free-tier fallback. Use a Google Cloud project with no billing. |
| `TELE_BOT_TOKEN` | Secret | Bot token from @BotFather. |
| `BOT_INVITE_CODE` | Secret | Optional. 8–64 of `A-Z a-z 0-9 _ -`. Required only when `require_invite_code` is true. |
| `OPENAI_MODEL` | Variable | Overrides `llm.openai_model`. |
| `GEMINI_MODEL` | Variable | Overrides `llm.gemini_model`. |
| `LLM_PROVIDER` | Variable | `openai`, `gemini`, `ollama`, or `mock`. |
| `LLM_FALLBACK` | Variable | Comma-separated provider list, or `none` to disable fallback. |
| `OLLAMA_MODEL` | Variable | Local model name. Default in config: `qwen2.5:7b-instruct`. |
| `OLLAMA_BASE_URL` | Variable | Default `http://localhost:11434`. |
| `TELE_CHANNEL_ID` | Variable | `@channel` that also receives the edition. |
| `TELE_OWNER_CHAT_ID` | Variable | Owner chat for crash notices and the Friday report. |
| `CHROME_PATH` | Variable | Browser binary for the PDF. |
| `BCS_STATE_PATH` | Variable | Override the state file path. |
| `BCS_OUTPUT_DIR` | Variable | Override the output directory. |
| `BCS_CONFIG_DIR` | Variable | Override the config directory. |
| `RUN_INTEGRATION` | Variable | Set to `1` to opt in to live integration tests. |

Non-secret behaviour (story counts, rubric, schedule, filters) lives in `config/settings.toml`. The full key table is in [Configuration reference](#config-reference).

---

<a id="usage"></a>

## 🖥️ Usage

### Running locally

Only needed for development or testing.

```bash
git clone <your repo url>
cd NEWSPAPER-ANALYZER                              # the folder git creates
python3.12 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt

python -m pytest                       # unit tests, all mocked
python -m app run --offline            # sample edition, no keys → output/edition-*.txt

cp .env.example .env                   # then fill in real values; never commit .env
set -a; source .env; set +a            # load into the shell (bash/zsh)
python -m app verify-sources
python -m app check-model
python -m app subscribers              # after pressing Start in the bot
python -m app test-telegram
python -m app run --dry-run            # real feeds + OpenAI (Gemini fallback), never sends
python -m app status                   # summary of state/state.json
```

Do not run `python -m app run`, `subscribers`, or `test-telegram` locally *and* in Actions. Each has its own copy of the state file, so they would disagree about deliveries and subscribers, and they would compete for the same Telegram updates.

### Commands and modes

| Command | Effect |
|---|---|
| `python -m app run` | Register new subscribers, build today's edition, and deliver it (text + PDF). No-op if today's edition was already delivered. Skips building (no model calls, no cost) when nobody has subscribed. |
| `python -m app run --hold` | Prepare today's edition and hold it until `edition.delivery_time` (08:00). A later run sends it. If 08:00 is at most `schedule.max_wait_minutes` (30) away, it waits and sends on time. After 08:00 it sends at once. Used by scheduled ticks and `deliver`. |
| `python3 -m app.schedule_gate check` | What a scheduled tick would do now. Standard library only. Reads `state/state.json`. Add `--now 2026-10-31T01:45:00+00:00` to try another time. |
| `python -m app run --manual` | Extra edition with whatever is new since the last one. Any number of times. The workflow's manual `live` mode uses this. |
| `python -m app run --no-pdf` | Do not create or send the PDF. |
| `python -m app run --dry-run` | Real feeds and a real model. **Never sends.** Uses `output/dry-run-state.json` (fresh each time), so production state is untouched. |
| `python -m app run --offline` | Bundled fictional sample data and the mock model. No network, no keys. Implies `--dry-run`. |
| `python -m app run --date 2026-10-24` | Override the edition date (testing). |
| `python -m app run --provider openai\|gemini\|ollama\|mock` | Use only that provider (no fallback). |
| `python -m app collect` | Read the feeds into state and answer `/start`. No AI calls. Scheduled ticks between briefings do this. |
| `python -m app subscribers` | Read new `/start` and `/stop` messages now, reply, and list active subscribers. |
| `python -m app test-telegram` | Same registration step, then one test message to each subscriber. |
| `python -m app verify-sources` | Live check of every configured feed. Exit code 1 if an enabled feed fails. |
| `python -m app check-model` | Confirms each configured model id works with its key. Not proof of credit or quota. `--provider openai\|gemini\|ollama` checks one. |
| `python -m app status` | Last edition, events by status, source health, last run. |
| `python -m app notify-failure` | Send a crash notice unless this run already reported one. The workflow calls this. |
| `python -m app -v` before a command | Verbose logs. |

Exit codes: `0` success, dry run, or already delivered; `1` failed; `2` failed but a failure notice was already sent to Telegram; `3` configuration error.

Workflow modes (`workflow_dispatch` on **Daily BCS briefing**): `offline`, `dry-run`, `live`, `deliver`, `subscribers`, `test-telegram`, `collect`, `verify-sources`, `check-model`, `status`. `dry-run` never sends. `deliver` is the on-demand path used by the 07:45 trigger (`python -m app run --hold`).

---

<a id="sources"></a>

## 🗞️ News sources

Sources live in `config/sources.toml`. Each entry has a name, homepage, `feed_url` (only if verified), type, subject relevance, `enabled`, `fetch_articles`, timeout, retry limit, and a `verification` note.

**Feed status** (verified live from GitHub Actions with `verify-sources`, last on **2026-11-21**):

| Source | Feed | Status |
|---|---|---|
| Prothom Alo | `https://www.prothomalo.com/feed` | enabled: fresh; noisy sections are pre-filtered |
| BBC News বাংলা | `https://feeds.bbci.co.uk/bengali/rss.xml` | enabled: fresh; strong on international affairs |
| The Daily Star: Bangladesh / Business / Environment / World | `https://www.thedailystar.net/{news/bangladesh,business,environment,news/world}/rss.xml` | enabled: fresh |
| UN News (all) | `https://news.un.org/feed/subscribe/en/news/all/rss.xml` | enabled: fresh |
| BBC Science & Environment, BBC Technology | `https://feeds.bbci.co.uk/news/{science_and_environment,technology}/rss.xml` | enabled (2026-11-21): fresh; added because science was 4 of 103 stories |
| NASA news releases | `https://www.nasa.gov/news-release/feed/` | enabled (2026-11-21): fresh (rate-limited once, retried) |
| ScienceDaily (top science) | `https://www.sciencedaily.com/rss/top/science.xml` | enabled (2026-11-21): fresh; many pop-science items, screening rejects most |
| WHO news | `https://www.who.int/rss-feeds/news-english.xml` | **disabled**: stale (newest item 2026-10-10) |
| The Daily Star front page | `https://www.thedailystar.net/frontpage/rss.xml` | **disabled**: stale (newest item 2022) |
| Dhaka Tribune (main, business) | `https://www.dhakatribune.com/feed/…` | **disabled**: `robots.txt` disallows bots |
| UN News Asia-Pacific | regional feed | off (covered by UN News all) |
| BSS, Bangladesh Bank, BBS, MoFA | — | reference links only |

Tested and not added: Daily Star `/rss.xml` and TBS (stale); BSS, Kaler Kantho, and Samakal (`robots.txt` blocks bots); Financial Express and Jugantor (broken feeds).

**Run `verify-sources` (Step 6) and disable anything that fails.** A failing source never stops the others. Health is tracked in state. After 3 consecutive failures the edition footer shows a maintenance notice.

**Official sources.** Government sites without feeds are reference entries with `aliases`. When an article names an institution (for example "Bangladesh Bank" / "বাংলাদেশ ব্যাংক"), the story links that institution's homepage under "দাপ্তরিক সূত্রে যাচাই". The app does not scrape government sites.

**Adding a source.** Find the feed link on the publisher's site (often in the page footer, or an HTML `link` tag with `rel="alternate"` and `type="application/rss+xml"`). Add a `[[source]]` block with `enabled = false`, run `verify-sources`, then enable it if it reports `OK`. Never guess feed URLs.

**Access rules.** The fetcher uses an honest user agent (`BCSNewspaperBot/1.0`), obeys `robots.txt`, never retries 401/403/451, and never bypasses paywalls or anti-bot protection. If a page is blocked, the story uses a clearly labelled **excerpt-only** analysis (when the feed excerpt is substantial) or is skipped.

---

<a id="selection"></a>

## 🎯 How stories are selected

Selection was recalibrated after real editions included opinion columns, local notices, party politics, crime, a single company's offers, and foreign domestic trivia. A story has to pass five gates. Every gate is enforced by code, not only by asking the model.

1. **Section and title pre-filter, before any AI call** (`[filters]` in `config/settings.toml`). It drops URL sections such as `/sports/`, `/entertainment/`, `/lifestyle/`, `/opinion/`, `/religion/`, `/bangladesh/district/`, `/bangladesh/crime/`, and `/video/`, plus junk titles ("আজ টিভিতে", horoscopes). This removes about 30–40% of items at no cost.
2. **Screening against the syllabus profile** (`config/syllabus.toml`). The model must give a **story type** and one of **42 syllabus topics**, built from the BPSC preliminary syllabus and written papers 005, 007, and 010 (constitution, budget, monetary policy, bilateral relations, Rohingya, climate diplomacy, UN system, conflicts, awards, indices, and the rest of that profile).
   - Code rejects opinion, feature, crime/accident, local admin, party politics, individual court cases, corporate/commercial news, **daily market prices and rates**, **speculation** ("may rise", undecided demands), foreign domestic trivia, sports, entertainment, and lifestyle, whatever the model decided.
   - An item with no valid syllabus topic is rejected.
   - "Maybe" items are dropped unless their priority is at least 7.
   - The prompt spells out what deserves priority 9–10 / 7–8 / 5–6 (a new head of government in a major country, or a UN decision about Bangladesh, is 9–10; official national statistics or a flagship UN report is 7–8). Analysis capacity (16 a run) goes to the highest priority first.
   - **No repeats.** Screening sees the headlines sent in the last 7 days. A candidate about the same event, report, or data release is rejected unless it carries a genuine new development (a decision, an agreement, new official figures). A follow-up gets a **🆕 নতুন কী** line. A second, deterministic check (same syllabus topic and the same distinctive figures as a story already sent) catches what the model misses.
3. **Full analysis with calibrated scoring.** The prompt defines what each score level means (most news is 3–6; 9–10 only for must-know items). A story needs **syllabus relevance ≥ 7** and a valid syllabus topic.
4. **Ranking.** Total score **≥ 65**, at most **one story per syllabus topic** (two shipbreaking stories cannot both get in), at most **3 per subject**, and 8 at most. **Balance:** science & technology and Bangladesh affairs each keep a slot when a story of theirs scores ≥ 65 (they were 4 and 8 of 103 stories before). The lowest-scoring story of an over-represented subject makes way.
5. **No padding.** If only 2 stories pass, the edition has 2.

Each story shows its **🎯 syllabus topic**, at most three **📌 must-remember facts** for prelims (chosen for durable exam value, not every number), **✍️ written-answer points**, and a BPSC-style **📝 written question**. The exam-focus label (প্রিলি / লিখিত / প্রিলি + লিখিত) is derived in code from those, not guessed. Every run logs a *selection report* (pre-filtered count, screening outcomes by reason, analysis rejections, selected stories with topic and score). See it under the run's "Run (…)" step in the Actions tab.

**Tuning**

- Too strict or too loose? Adjust `selection.min_syllabus_relevance`, `edition.min_story_score`, and `selection.maybe_min_priority` in `config/settings.toml`.
- Add or rename topics, or add good and bad examples, in `config/syllabus.toml`.
- Drop a whole section with `filters.exclude_url_paths`.

Subject mapping follows the BPSC BCS syllabus: preliminary subjects are Bangladesh affairs, international affairs, geography/environment/disaster management, general science, computer & ICT, and ethics/values/good governance. Written papers: 005 Bangladesh Affairs, 007 International Affairs, 010 General Science & Technology. Confirm the latest syllabus at <https://bpsc.gov.bd>.

---

<a id="grounding"></a>

## 🛡️ Factual grounding

The model writes the notes. Deterministic code decides what you see.

- **Every key fact needs a verbatim quote** from the retrieved text. Facts whose quote is not in the article are dropped.
- **Numbers are checked.** Every number in a fact must appear in its quote. Any sentence in the summary, analysis, or background that contains a number not present in the article is removed. Bengali and English digits are normalised before comparison.
- **Claims are separated from facts.** "X said …" goes under *উদ্ধৃত দাবি (যাচাইকৃত তথ্য নয়)*.
- **Analysis is labelled** *(AI বিশ্লেষণ)*. Background is labelled *(প্রতিবেদনের বাইরের সাধারণ প্রেক্ষাপট)* and may not contain figures.
- **Related static GK (📚 প্রাসঙ্গিক সাধারণ জ্ঞান) is checked twice.** These are textbook facts that are *not* in the article: which amendment introduced a system, when an organisation was founded, where it is headquartered. The model proposes at most three per story, each with a question and a short answer. A **second, blind call** answers the questions without seeing those answers. Code keeps an item only if both agree (numbers exactly, names by their words) and the checker is sure. Hedged statements, current office-holders, changing statistics, and anything restating the article's own figures are dropped. The section is labelled as outside the article. An empty section is preferred to a wrong fact.
- **Excerpt-only stories are marked** ⚠️ and analysed only from the excerpt.
- A story with **no verifiable fact is excluded**, not padded.
- **MCQs** must cite a verified fact (an article fact, or a twice-checked GK item for at most two of the three). The correct option's numbers must appear in that fact. The model writes six candidates and code keeps the best three. Each needs exactly 4 distinct options **of the same kind and unit** (no "crore" option in a percentage question, no bare number among names, no "all of the above"), must stand alone (no "প্রতিবেদন অনুযায়ী"), must not give the answer away, and at most one question per story. Fewer than 3 valid MCQs means fewer are sent, with a note.
- **Screening ids are validated.** The model can only reference candidate ids we supplied. Unknown ids are ignored.
- **Neutrality.** Prompts require political neutrality and forbid inferring motives.

The scoring weights (syllabus 30%, significance 25%, facts 20%, written potential 15%, novelty 10%) are **starting heuristics, not validated predictions of exam questions**. Change them in `config/settings.toml`. They must sum to 1.0.

---

<a id="partial"></a>

## ⚠️ Partial editions and quota exhaustion

The model can become unavailable mid-run (daily quota used up, per-minute limit, outage, retired model). Each error is handled differently:

| Situation | Behaviour |
|---|---|
| HTTP 429, per-minute limit | Wait the server's suggested delay (max 90 s), retry up to 3 times |
| HTTP 429, daily quota or `limit: 0` | Stop calling that model for this run, immediately |
| 5xx / network error | Exponential backoff with jitter, max 3 retries |
| Malformed JSON / blocked / truncated output | Retry once, then count a failed attempt for that story |
| 401/403/invalid key, 404 unknown model | Permanent: no retries, the run stops using that model |
| Own budget `max_calls_per_run` reached | Treated like quota exhaustion |

When this happens mid-run:

1. Every completed analysis is **already saved** (state is checkpointed after each story).
2. Completed, useful stories are sent as an edition labelled **⚠️ আংশিক সংস্করণ**, with the reason and the number of candidate stories still waiting.
3. Missing stories are never invented.
4. If nothing usable was produced, every subscriber gets one short **failure notice** instead (only once per day).
5. Unfinished stories stay queued. The next run (scheduled tomorrow, or a manual `live` run after a failure) continues where it stopped: no re-screening, no re-analysis of finished work. Quota failures do not count against a story. Other failures are retried at most `max_attempts_per_story` (3) times.
6. Stories older than `freshness_hours` (36 h) expire rather than pile up.

---

<a id="state"></a>

## 💾 State, persistence, and recovery

`state/state.json` (schema version 2) records processed articles (canonical URL, content hash, publication and retrieval times), event groups, per-stage status (`new → selected/maybe/rejected → analysed/analysis_rejected/failed → included`), stored analyses, attempt counts and last error, editions (status, partial flag, MCQs, every Telegram chunk with message id and sent time), the last successful edition, source health, and the last 30 runs.

- **Atomic writes:** temp file → fsync → rename. The previous version is kept as `state.json.bak` during a run.
- **Validation on startup:** malformed records are dropped individually. A corrupt file is preserved as `state.json.corrupt-<time>` and recovered from the backup, or, as a last resort, a fresh state is started and the run log says so.
- **Migration:** older schemas are upgraded in steps (v1 → v2 added subscribers). A file from a **newer** schema is never overwritten. The run stops instead.
- **Subscribers:** chat id, first name, type (private/group), active/inactive, join/leave time, plus the last processed Telegram `update_id` so no `/start` is handled twice.
- **Idempotent delivery:** an edition is rendered once and its chunks saved *before* sending. For each subscriber, each chunk's Telegram message id is saved as soon as Telegram confirms it. An edition is marked `delivered` only when **every active subscriber** has **all** chunks. The PDF counts as the last item. A retry sends each person only what they are missing. The scheduled edition for a date is never sent twice. Manual extra editions are stored as `<date>-m1`, `-m2`, … and never repeat a story.
  - Residual risk: if the runner dies in the instant between Telegram accepting a message and the state write, that one chunk could be sent twice on retry. Telegram has no idempotency key to prevent this.
- **Git:** the workflow commits `state/state.json` with the workflow token (`contents: write` only). On a rejected push it rebases and retries. If the state file itself conflicts, it **stops without overwriting** newer state and keeps this run's state in the workflow artifact. It never force-pushes. A `concurrency` group (`bcs-briefing-state`) ensures only one run touches state at a time.
- **If a state commit fails,** the edition was still delivered (or saved in the artifact), the job turns red, and you get a Telegram notice. Download the artifact to recover the state if needed.
- Old records are pruned after `retention_days` (14). Editions are pruned after 30 days. Compact per-edition digests used by the weekly and monthly revisions are kept for `revision.keep_days` (40), so those revisions never depend on pruned article text and never contain anything that was not already checked and sent.

To **reset** everything: delete `state/state.json` and commit. The next run starts fresh, so it may re-send stories it had already shown you.

---

<a id="logs"></a>

## 🩺 Logs and troubleshooting

- **Actions → Daily BCS briefing → a run → `briefing` job:** step-by-step logs. The "Run" step prints a JSON summary (`outcome`, `stories`, `mcqs`, `partial`, `llm_calls`, `errors`).
- **Artifacts** (bottom of the run page, kept 7 days): `output/edition-<date>.txt` (exactly what was sent), `edition-<date>.json`, `run-result.json`, and the state file.
- **`status` mode** (or `python -m app status`): last edition, events by status, per-source health, last run errors.
- **Email:** GitHub emails the repository owner when a scheduled run fails. Subscribers get a short, non-technical Telegram notice.

| Symptom | Likely cause / fix |
|---|---|
| `Telegram rejected request (401)` | Wrong `TELE_BOT_TOKEN` |
| Briefing arrives but no PDF | Check the run log for `PDF could not be created` / `pdf_error`. Usually no Chrome, or the font step failed. The text edition is unaffected. |
| Run says `no_subscribers` / "No subscribers yet" | Nobody has pressed Start, or their Start is older than 24 h. Open the bot, press Start, run `subscribers`. |
| Someone pressed Start but got no welcome | Replies only happen at the next run. Run `subscribers`. "❌ আমন্ত্রণ লিংক… সঠিক নয়" means `require_invite_code` is on and they used the plain bot link. |
| "সদস্যসংখ্যা পূর্ণ" reply | A `max_subscribers` cap was reached. Raise it, or set `0` for no limit. |
| `A webhook is set for this bot` | Another tool set a webhook. Open `https://api.telegram.org/bot` + your token + `/deleteWebhook` once. |
| A subscriber marked inactive unexpectedly | They blocked the bot or left the group. They can open the bot and press Start again. |
| `Provider openai disabled for this run: … credit exhausted` | Prepaid OpenAI credit is used up. Today ran on Gemini. Add credit when you want OpenAI back. |
| `OpenAI rejected credentials` / `OpenAI model unavailable` | Bad `OPENAI_API_KEY`, or the model id is wrong or retired. Fix the secret or set `OPENAI_MODEL`. Gemini covers the run meanwhile. |
| `OpenAI request failed (400): … reasoning_effort` | That model does not accept the parameter. Set `openai_reasoning_effort = ""`. |
| Edition footer says "বিকল্প মডেল" was used | OpenAI was unavailable for part of the run. Check the log line `Provider openai disabled …`. |
| `Gemini model unavailable` | Model id retired or renamed. Set `GEMINI_MODEL` to a current free model. |
| `Gemini quota exhausted … limit: 0` | That model has no free quota for your project. Pick another model. |
| `Gemini rejected credentials` | Bad or revoked `GEMINI_API_KEY`. |
| `Source X failed: HTTP 403` / `robots.txt disallows` | The publisher blocks automated access. Disable that source. |
| `Source X failed: Malformed feed` | Feed URL is wrong or has moved. Re-verify. |
| Many stories ⚠️ excerpt-only | The site blocks article pages or renders with JavaScript. Acceptable, or set `fetch_articles = false`. |
| No briefing at 08:00 | Scheduled run delayed or skipped by GitHub, workflow not on the default branch, or Actions disabled. Check the Actions tab and run `live`. |
| `state/state.json changed on the remote too` | Someone edited state while a run was going. Resolve by hand. Never force-push. |
| Exit code 3 / "Configuration error" | Typo in `config/*.toml`. The message names the key. |

---

<a id="cost"></a>

## 💸 Cost and free-tier limits

Measured over 6–21 November 2026: about **$0.15 a day** (≈ $4.50 a month). With daytime collection the morning run screens more candidates (up to 160, 4 screening calls) and analyses up to 16. Static GK may take a second round, and Fridays add one weekly-MCQ call, so expect **about $0.18–0.25 a day**. Repeated prompt prefixes are billed at OpenAI's cached-input rate, which the cost estimate counts.

Daily usage: about 19–26 model requests ≈ **75–120k input + 20–40k output tokens** (Bengali output, plus hidden "reasoning" tokens on newer models, billed as output). A real-model dry run on 2026-10-31 used 19 requests, 76k input and 20k output tokens: about **$0.15**. The edition is built once, so the number of subscribers does not change the AI cost.

| Model (primary) | Price per 1M tokens (in / out)* | Per day | Per month |
|---|---|---|---|
| `gpt-5.4-nano` | $0.20 / $1.25 | ~$0.05–0.07 | **~$1.5–2 (≈ ৳180–260)** |
| `gpt-5.4-mini` (default) | $0.75 / $4.50 | ~$0.17–0.26 | **~$5–8 (≈ ৳600–1,000)** |
| Gemini fallback (free tier) | free | 0 | 0 |

\*Third-party snapshots from mid-2026, at ≈ ৳120/US$. Verify on <https://openai.com/api/pricing>. Dry runs cost about one day's usage each. The overview range of **US$2–8 (≈ ৳250–1,000)** is the spread from the cheaper model to the default.

**See the real numbers.** Every run logs `llm_usage` (requests and tokens per provider) and `estimated_openai_cost_usd` in its JSON summary, and saves them in `state/state.json` under `runs`. Compare with OpenAI's **Usage** page.

**How spending is bounded**

- OpenAI is prepaid. With auto-recharge off, spend cannot exceed the credit you added.
- Each provider is capped at `llm.max_calls_per_run` (36) requests per run, retries included.
- When OpenAI credit runs out, the run continues on Gemini's free tier. A Gemini project without billing refuses requests over quota (HTTP 429), and the app makes a partial edition. Nothing upgrades to a paid plan automatically.
- To go back to **৳0**, remove the `OPENAI_API_KEY` secret (or set `provider = "gemini"`). The app then runs on Gemini only.

| Service | What's used | Free allowance (verify yourself) |
|---|---|---|
| GitHub Actions (private repo, GitHub Free) | ~21 one-minute gate ticks + ~5 collections + ~10–35 min of briefing work a day → ~1,100–1,800 min/month | 2,000 min/month; 500 MB artifact storage |
| Gemini Developer API (Free tier) | only on fallback days | Per-model RPM/RPD limits per project; resets at midnight Pacific time |
| Telegram Bot API | about 8–10 messages per subscriber per edition, plus replies | Free (about 1 msg/s per chat, handled automatically; about 30 msg/s overall) |
| News feeds | a few HTTP requests a day | Free, subject to each publisher's terms |

---

<a id="providers"></a>

## 🤖 AI providers

`config/settings.toml`:

```toml
[llm]
provider = "openai"              # primary
fallback_providers = ["gemini"]  # tried in order; [] to disable
openai_model = "gpt-5.4-mini"
gemini_model = "gemini-3.8-flash"
```

**When the run switches to Gemini.** Each provider has its own call budget, spacing, and retries. OpenAI is switched off **for the rest of that run** (and Gemini takes over) when:

- the prepaid credit is exhausted (`429 insufficient_quota`),
- the key is rejected or the model id is unknown (401/403/404),
- it keeps failing after its retries (outage, 5xx, timeouts),
- it hits the per-run call budget.

Short per-minute rate limits are waited out and retried on OpenAI first. If OpenAI returns unusable output for one request, that single request is retried on Gemini, and OpenAI stays in use. The next day's run tries OpenAI again.

**What readers see.** If a fallback was used, the edition footer says so ("…বিকল্প মডেল দিয়ে করা হয়েছে"). The fact checks (verbatim quotes, numbers present in the article, MCQ validation) apply identically to every model's output. If both providers are unavailable, you get the usual partial edition or failure notice. Nothing is invented.

**Other combinations.** Gemini only: `provider = "gemini"`, `fallback_providers = []`, or simply do not set `OPENAI_API_KEY`. OpenAI only: `LLM_FALLBACK=none`. A local model can be primary or fallback. See below.

<a id="schedule-off"></a>

## ⏸️ Disabling the schedule

- **Pause:** Actions → *Daily BCS briefing* → **⋯** (top right) → **Disable workflow**. Re-enable the same way.
- **Remove the schedule but keep manual runs:** delete the `schedule:` block (the `schedule:` line and all its `- cron:` lines) in `.github/workflows/daily-briefing.yml`.
- **Stop completely:** delete the workflow file, and optionally revoke the OpenAI and Gemini keys and the bot (BotFather → `/revoke`).

GitHub automatically disables schedules in **public** repositories after 60 days without activity. The daily state commit counts as activity.

<a id="local-model"></a>

## 🖥️ Switching to a local model

All AI calls go through `app/llm/base.py`.

- `LLMProvider.generate_raw(request) -> str` is the only thing a provider implements. It maps failures to `QuotaExhaustedError`, `RateLimitError`, `TransientLLMError`, `PermanentLLMError`, `ModelUnavailableError`, or `InvalidResponseError`.
- `LLMClient` adds the call budget, spacing, retries, backoff, and JSON parsing for every provider.
- Prompts, validation, grounding, and rendering do not care which provider produced the JSON.

**Ollama** (included, experimental, not tested against a real Ollama server):

```bash
ollama pull qwen2.5:7b-instruct          # any instruction model that follows JSON well
export LLM_PROVIDER=ollama OLLAMA_MODEL=qwen2.5:7b-instruct
python -m app run --dry-run              # check quality before going live
```

GitHub-hosted runners **cannot reach a model on your computer**. Options:

1. Run the pipeline on your own machine on a schedule (cron / Task Scheduler) with `python -m app run`. The machine must be on at 08:00. Stop the GitHub workflow so the two do not keep separate state.
2. Register your machine as a **self-hosted runner** (free) and change `runs-on` to `self-hosted`. Same requirement: the machine must be on.

Small local models are weaker at the strict JSON and Bengali instructions. The grounding checks discard more of their output, so expect more partial editions. Compare with a `--dry-run` first.

**Another provider:** add a module under `app/llm/` with a `generate_raw` implementation and one branch in `build_provider()` in `app/llm/__init__.py`. Nothing else changes.

---

<a id="testing"></a>

## 🧪 Testing

```bash
python -m pytest
```

The default pytest options skip tests marked `integration`. A fixture blocks real HTTP, so unit tests cannot spend OpenAI credit or Gemini quota, or message Telegram. The scheduled workflow runs this suite before each live run. If the tests fail, no briefing is sent and you are notified.

Coverage includes feed parsing with malformed items, missing, invalid, and future dates, invalid URLs, duplicate detection, extraction failure and excerpt-only rules, the scoring rubric, malformed model output, unsupported facts and numbers, MCQ schema and answer-index validation, HTML escaping and chunking, Telegram retries and plain-text fallback, Gemini and OpenAI 429/404/5xx classification (including OpenAI `insufficient_quota`), the OpenAI → Gemini fallback chain (credit exhausted, bad key or model, outage, invalid output, both exhausted, a mid-run switch that still completes an edition, cost estimate), retry limits and the call budget, state corruption, backup recovery, migration, and newer-schema refusal, quota exhaustion mid-run with resumption, interrupted delivery resuming without duplicates, failure-notice de-duplication, low-relevance days without padding, dry-run behaviour, secret redaction in logs, and subscribers: public joining, invite-code checks, `/stop`, the optional cap, parallel delivery to 40 subscribers with one PDF upload, blocked users, group commands, malformed updates, per-subscriber delivery and resumption, and "no subscribers spends no quota".

**Live integration tests** (opt-in, real network; 1 model lookup and 1 Telegram `getMe`; no message is sent):

```bash
RUN_INTEGRATION=1 GEMINI_API_KEY=… TELE_BOT_TOKEN=… python -m pytest -m integration
```

---

<a id="security"></a>

## 🔒 Security and privacy

- **No secrets in the repository.** Credentials come only from environment variables and GitHub Secrets. `.env` is git-ignored. `.env.example` holds placeholders.
- **Subscriber data** (chat ids, first names) lives only in the private repository's state file. The bot is public, so anyone can subscribe. Their data is never shown to other subscribers. When an invite code is used, it is compared in constant time and redacted from logs like the other secrets.
- **No secrets in logs.** The OpenAI and Gemini keys travel in headers, never URLs. A logging filter redacts credentials from every log line. urllib3 debug logging (which would print Telegram's token-bearing URL) is suppressed. The bot token is part of Telegram's request URL by their design, so it is never logged.
- **Web content is untrusted.** Article text is wrapped in delimiters the article cannot forge. The model is told to treat it as data, and the model has no tools. Its output is parsed as JSON and validated. URLs are stripped from model text, all text is HTML-escaped, and links only ever come from our own feed records. A hostile article can at worst get itself rejected.
- **Network hygiene.** Timeouts on every request, size caps (3 MB) on feeds and pages, `robots.txt` respected, honest user agent, no paywall or anti-bot bypass.
- **Least privilege.** The workflow token has `contents: write` only, used solely to commit `state/state.json`. No force-push. The optional cron-job.org token is scoped to Actions on this one repository.
- **Data use.** OpenAI states API data is not used for training by default. On Gemini's free tier, Google may use prompts and responses to improve its products. Only public news text is sent to either.
- **PDF.** Article and model text is escaped. The document's Content-Security-Policy blocks scripts and external loads.

---

<a id="config-reference"></a>

## ⚙️ Configuration reference

<details open>
<summary><b>config/settings.toml — every non-secret key</b></summary>

Edit and commit. Defaults below are the values in this repository.

| Key | Default | Meaning |
|---|---|---|
| `edition.max_stories` / `min_target_stories` | 8 / 5 | Target range. A ceiling, not a quota. |
| `edition.min_story_score` | 65 | Stories below this (0–100) are never included. |
| `edition.timezone` / `delivery_time` | `Asia/Dhaka` / `08:00` | When the held edition is released. |
| `selection.min_syllabus_relevance` | 7 | Minimum syllabus relevance (0–10) from the full analysis. |
| `selection.maybe_min_priority` | 7 | "Maybe" items below this screening priority are dropped. |
| `selection.max_stories_per_topic` | 1 | Stories per syllabus topic per edition. |
| `selection.max_stories_per_subject` | 3 | Stories per subject per edition. `0` = no cap. |
| `selection.reserve_subjects` | science_technology, bangladesh_affairs | One slot kept for each when a story of it scores ≥ `min_story_score`. |
| `revision.weekly_day` | Friday | Weekly revision day (local). `""` = off. |
| `revision.weekly_stories` / `weekly_mcqs` | 15 / 10 | Size of the weekly revision. |
| `revision.monthly_pdf` | true | Previous month's PDF on the 1st. |
| `revision.keep_days` | 40 | Compact per-edition digests kept for the revisions. |
| `schedule.prepare_from` / `deliver_until` | `05:00` / `22:00` | Window in which a tick may build or send. |
| `schedule.max_wait_minutes` | 30 | A tick this close to 08:00 waits and sends on time. |
| `schedule.max_runs_per_day` | 5 | Failed runs today before ticks stop trying. |
| `schedule.collect_every_hours` | 4 | Collection between briefings (no AI calls). `0` = off. |
| `filters.exclude_url_paths` / `exclude_title_patterns` | sections list | Dropped before any AI call. |
| `edition.freshness_hours` | 36 | Items older than this are ignored or expire. |
| `edition.mcq_count` | 3 | MCQs per complete edition. |
| `collection.max_items_per_source` | 40 | Items kept from each feed. |
| `collection.max_feed_bytes` / `max_article_bytes` | 3 MB / 3 MB | Response size caps. |
| `collection.user_agent` | `BCSNewspaperBot/1.0 …` | Honest agent. Does not impersonate a browser. |
| `extraction.min_article_chars` | 600 | Below this, the body counts as unavailable → excerpt-only. |
| `extraction.max_article_chars` | 12000 | Text sent to the model is truncated here. |
| `extraction.min_excerpt_chars_for_analysis` | 220 | Below this, an excerpt-only story is skipped. |
| `screening.max_candidates` / `batch_size` | 160 / 40 | Candidates screened per run / per call. |
| `analysis.max_analyses_per_run` | 16 | Model calls for analysis per run. |
| `analysis.max_attempts_per_story` | 3 | Then the story is abandoned. |
| `scoring.weights.*` | 0.30 / 0.25 / 0.20 / 0.15 / 0.10 | Rubric weights. Must sum to 1. |
| `llm.provider` | `openai` | Primary: `openai`, `gemini`, `ollama`, or `mock`. |
| `llm.fallback_providers` | `["gemini"]` | Tried in order. Override with `LLM_FALLBACK` (`none` disables). |
| `llm.openai_model` | `gpt-5.4-mini` | Override with `OPENAI_MODEL`. |
| `llm.openai_reasoning_effort` | `""` | Optional `low` or `minimal` to cut reasoning tokens. Empty if the model rejects it. |
| `llm.openai_usd_per_million_input` / `cached_input` / `output` | 0.75 / 0.075 / 4.50 | Only for the logged cost estimate. |
| `llm.gemini_model` | `gemini-3.8-flash` | Override with `GEMINI_MODEL`. |
| `llm.ollama_model` / `ollama_base_url` | `qwen2.5:7b-instruct` / `http://localhost:11434` | Local provider. |
| `llm.max_calls_per_run` | 36 | Hard cap per provider, including retries. |
| `llm.min_seconds_between_calls` | 6 | Spacing for Gemini and Ollama. OpenAI uses its own 1.0 s spacing. |
| `llm.max_retries` / `max_retry_after_seconds` | 3 / 90 | Retries, and the longest per-minute wait that is honoured. |
| `telegram.max_message_chars` | 3800 | Chunk size. Telegram's limit is 4096. |
| `telegram.max_subscribers` | 0 | Cap on active subscribers. `0` = no limit. |
| `telegram.require_invite_code` | false | Only admit `/start` followed by `BOT_INVITE_CODE`. |
| `telegram.min_seconds_between_messages` | 1.1 | Pause between messages to the same chat. |
| `telegram.send_workers` | 8 | Parallel sends when there are many subscribers. |
| `telegram.max_messages_per_second` | 25 | Overall sending rate. Telegram allows about 30. |
| `telegram.channel_id` | `""` | Public channel. Or the `TELE_CHANNEL_ID` variable. |
| `telegram.dm_subscribers` | true | Also send to subscribers' private chats. |
| `telegram.owner_chat_id` | your chat | Crash notices and the weekly report. Or `TELE_OWNER_CHAT_ID`. |
| `telegram.mcq_as_quiz` / `feedback_poll` | true / true | MCQs as quiz polls, and the "useful stories" poll. |
| `state.retention_days` / `max_run_history` | 14 / 30 | Pruning window, and how many runs are kept. |
| `output.dir` | `output` | Rendered editions. Git-ignored. Uploaded as a workflow artifact. |

</details>

---

<a id="credits"></a>

<div align="center">

## 💜 Credits

Built by **[Shahriar Ahmed](https://github.com/fr-ost)**, Co-Founder & COO of **[Unique Labs](https://www.uniquelabs.org)**.

[GitHub](https://github.com/fr-ost) · [Unique Labs](https://www.uniquelabs.org) · [shahriarahmed.net](https://shahriarahmed.net)

BCS syllabus topics follow the public BPSC syllabus. Confirm the current papers at [bpsc.gov.bd](https://bpsc.gov.bd). News stays with its publishers. This project reads public feeds and does not republish full articles.

<br/>

<img width="100%" alt="Footer wave in amber, pink, and violet" src="https://capsule-render.vercel.app/api?type=waving&color=0:FFB703,50:FF2E93,100:6C2BD9&height=120&section=footer"/>

</div>
