# Oversold Value Zone Accumulation Strategy

**A simple, rule-based, long-only stock accumulation and swing exit strategy built for the Indian stock market (NSE).**  
The goal is to identify oversold value zones, accumulate in stages, and exit during momentum recovery. This is designed as a side-income approach, not full-time trading advice.

> **Not financial advice.** Use at your own risk. Treat this as educational / experimental.

---

## ✅ Core Principles

- **Keep it simple and repeatable.**
- **Avoid prediction and over-analysis.**
- **Accumulate when fear is high.**
- **Exit when optimism returns.**
- Focus on **fewer high-quality trades**, not frequent trades.  
- Do **not** use this strategy for speculative or weak stocks.

---

## 🧭 Market Scope

**Works best for**
- NSE index products (NIFTY, BANKNIFTY)  
- Large-cap, fundamentally strong companies

**Avoid**
- Penny stocks  
- Small caps with governance/structural risk  
- Companies in long-term decline

---

## 📊 Indicators Used

| Indicator | Timeframe | Purpose |
|---|---:|---|
| RSI (14) | Daily | Detect oversold zones |
| 200-day SMA | Daily | Identify long-term support zone |

**Optional (enhancers)**: Weekly RSI, Monthly RSI

---

## 🎯 Entry Rules (Staged Accumulation — daily EOD)

All signals are evaluated on **daily EOD** data. (No Live)

> We prefer to sit on cash (liquid funds), when no suitable stocks found and capital is idle.

**Base accumulation (three stages):**
 
| Stage | Condition | Allocation |
|---:|---|---:|
| **Stage 1** | Daily RSI <= 40 **AND** Price ≤ 5% from 200 DMA | **Buy 25%** |
| **Stage 2** | Daily RSI <= 35 **AND** Price ≤ 3% from 200 DMA | **Buy 25%** |
| **Stage 3** | Daily RSI <= 30 **AND** Price ≤ 1% from 200 DMA | **Buy 50%** (base position complete) |

- Start with small quantity and **pyramid** as confirmations come.
- Stop-loss is **applied only after Stage 3** (see Risk section).

---

## 🔥 Extended Opportunity (rare — panic / crash conditions)

| Stage | Condition | Additional Allocation | Max cumulative |
|---:|---|---:|---:|
| **Stage 4 (Super)** | Weekly RSI <= 40 **AND** Monthly RSI <= 50 | +50% | 150% |
| **Stage 5 (Super-Super)** | Weekly RSI <= 35 **AND** Monthly RSI <= 45 | +50% | **200% (max)** |

- If weekly/monthly confirmations occur while base positions are active, you may add Stage 4/5 allocations.
- SL (stop-loss) moves to the **latest accumulation zone** when these stages are added.
- Extended positions use **higher-timeframe exit logic** (see Exits).

---

## ⚠️ Risk Management & Stop Loss

- **Stop loss applies after Stage 3** (i.e., when base position is fully active).  
- SL level is relative to the latest confirmation price/accumulation zone.  
- Recommended hard-stop: **do not let loss > 10%** from the latest accumulation zone (adjust to personal risk tolerance).  
- F&O is not recommended due to long holding periods, large contract size, more capital (margin money), rollover costs, expert skills required for risk and capital management.
---

## 📤 Exit Strategy

> This is long-only strategy — preserve upside unlimited.

**Base positions (Stages 1–3):**
- **Sell 50%** when daily RSI reaches **70** (partial profit booking).  
- **Sell remaining 50%** when daily RSI crosses **80** (final booking).  
- Traders may choose to scale out earlier if personal objectives are met.

**Extended positions (Stages 4–5):**
- **Stage 4 (Weekly entry)**: exit near **Weekly RSI 60–65+**.  
- **Stage 5 (Monthly entry)**: exit near **Monthly RSI 60–65+**.  
- When higher-timeframe exits apply, daily exit signals for those units are ignored.

---

## 🧠 Psychology & Discipline

- Buy when others are fearful; hold while price stabilizes; exit when others are greedy.  
- Avoid emotional trading and chasing news.  
- Cash idle is a feature — patience is part of the edge.  
- Treat this as **side income**, not your sole source of livelihood.

---

## 📈 Performance Expectations & Metrics (example)

We plan to track and report (post Go Live):
- Number of signals / trades
- Average holding period
- Win rate
- Average return per trade
- CAGR, annualized volatility
- Max drawdown, Sharpe ratio

**Targets (aspirational)**:
- Conservative: single-digit to mid-teens annualized when applied to a diversified index/large-cap pod. Expected to be better than FD and comparable to SIP 
- Max drawdown target: **< 12%** (subject to market conditions and personal risk tolerance).

---

## ⚙️ Implementation Roadmap (phased)

**Phase 0 — Documentation & POC**
- Single-symbol POC — start with NIFTY (index) or a handful of hand-picked large caps.

**Phase 1 — POC Automation**
- Daily cron job; EOD screen; DB persistence; email/Telegram alerts.

**Phase 2 — Expand Universe**
- NIFTY 50, F&O-capable symbols, ETFs (index/sector ETFs).

**Phase 3 — Further Expand Universe**
- Commodity (MCX) - Gold, Silver etc. Currency - BTC/ETH, USDINR etc.

**Phase 4 — UI & User Feature**
- Dashboard to show live triggers, scoreboard, and historical P&L for alerts.

**Phase 5 — Monetization (Optional)**
- User subscriptions; personalized alert filters.

**Always**: keep configuration dynamic — allow symbol-specific overrides (RSI thresholds, allocation caps).

---

## 🗂 Project Structure (recommended)

dss/  
├── README.md  
├── LICENSE  
├── requirements.txt  
├── config/  
│ ├── default_settings.yaml  
│ ├── symbols_list.yaml  
│ └── overrides/  
│ └── symbol_custom_settings.yaml  
├── data/  
│ ├── raw/  
│ ├── processed/  
│ └── logs/  
├── src/  
│ ├── core/  
│ ├── poc/  
│ ├── services/  
│ ├── app/  
│ └── ui/  
├── tests/  
├── docs/  
└── cron/  

---

## Telegram & Contact
Join the discussion channel:  
- https://t.me/dhanyawadss  
- https://web.telegram.org/k/#@dhanyawadss

---

---

## Legal / Disclaimer
This repository documents a rule-based idea for education and demonstration. **Not financial advice.** Use at your own risk. The owner/contributors are not liable for any trading losses.

---

## Licensing
Open for learning, adaptation and non-commercial use unless you decide otherwise. Added a formal `LICENSE` file to specify the license you prefer (MIT/Apache2/GPL).

---
