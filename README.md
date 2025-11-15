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

All signals are evaluated on **daily EOD** data.

**Base accumulation (three stages):**

| Stage | Condition | Allocation |
|---:|---|---:|
| **Stage 1** | Daily RSI < 40 **AND** Price ≤ 5% from 200 DMA | **Buy 25%** |
| **Stage 2** | Daily RSI < 35 **AND** Price ≤ 3% from 200 DMA | **Buy 25%** |
| **Stage 3** | Daily RSI < 30 **AND** Price ≤ 1% from 200 DMA | **Buy 50%** (base position complete) |

- Start with small quantity and **pyramid** as confirmations come.
- Stop-loss is **applied only after Stage 3** (see Risk section).

---

## 🔥 Extended Opportunity (rare — panic / crash conditions)

| Stage | Condition | Additional Allocation | Max cumulative |
|---:|---|---:|---:|
| **Stage 4 (Super)** | Weekly RSI < 40 **AND** Monthly RSI < 50 | +50% | 150% |
| **Stage 5 (Super-Super)** | Weekly RSI < 35 **AND** Monthly RSI < 45 | +50% | **200% (max)** |

- If weekly/monthly confirmations occur while base positions are active, you may add Stage 4/5 allocations.
- SL (stop-loss) moves to the **latest accumulation zone** when these stages are added.
- Extended positions use **higher-timeframe exit logic** (see Exits).

---

## ⚠️ Risk Management & Stop Loss

- **Stop loss applies after Stage 3** (i.e., when base position is fully active).  
- SL level is relative to the latest confirmation price/accumulation zone.  
- Recommended hard-cap: **do not let loss > 10%** from the latest accumulation zone (adjust to personal risk tolerance).  
- If using F&O, **hedge with put buys** (no call selling). Futures buys or call buys allowed; prefer buying hedges over selling options.  
- This is long-only — preserve upside unlimited.

---

## 📤 Exit Strategy

**Base positions (Stages 1–3):**
- **Sell 50%** when daily RSI reaches **70** (partial profit booking).  
- **Sell remaining 50%** when daily RSI crosses **80** (final booking).  
- Traders may choose to scale out earlier if personal objectives are met.

**Extended positions (Stages 4–5):**
- **Stage 4 (Weekly entry)**: exit near **Weekly RSI 60–65**.  
- **Stage 5 (Monthly entry)**: exit near **Monthly RSI 60–65**.  
- When higher-timeframe exits apply, daily exit signals for those units are ignored.

---

## 🧠 Psychology & Discipline

- Buy when others are fearful; hold while price stabilizes; exit when others are greedy.  
- Avoid emotional trading and chasing news.  
- Cash idle is a feature — patience is part of the edge.  
- Treat this as **side income**, not your sole source of livelihood.

---

## 📈 Performance Expectations & Metrics (example)

Track and report:
- Number of signals / trades
- Average holding period
- Win rate
- Average return per trade
- CAGR (if backtested), annualized volatility
- Max drawdown, Sharpe ratio

**Targets (example / aspirational)**:
- Conservative: single-digit to mid-teens annualized when applied to a diversified index/large-cap pod.  
- Max drawdown target: **< 12%** (subject to market conditions and personal risk tolerance).

---

## ⚙️ Implementation Roadmap (phased)

**Phase 0 — Documentation & POC**
- Single-symbol POC — start with NIFTY (index) or a handful of hand-picked large caps.

**Phase 1 — POC Automation**
- Daily cron job; EOD screen; DB persistence; email/Telegram alerts.

**Phase 2 — Expand Universe**
- NIFTY 50, F&O-capable symbols, ETFs (index/sector ETFs).

**Phase 3 — UI & User Feature**
- Dashboard to show live triggers, scoreboard, and historical P&L for alerts.

**Phase 4 — Monetization (much later)**
- User subscriptions; personalized alert filters.

**Always**: keep configuration dynamic — allow symbol-specific overrides (RSI thresholds, allocation caps).

---

## 🗂 Project Structure (recommended)

