# Oversold Value Zone Accumulation Strategy

A simple, rule-based, long-only stock accumulation and swing exit strategy built for the Indian stock market (NSE). The goal is to identify oversold value zones, accumulate in stages, and exit during momentum recovery. This strategy works best with fundamentally strong companies and index products.

> Treat this as **side income**. Not financial advice. Not intended for full-time trading reliance.

---

## ✅ Core Principles

- Keep it simple and repeatable
- Avoid prediction and over-analysis
- Accumulate when fear is high
- Exit when optimism returns
- Focus on fewer high-quality trades, not frequent trades
- Do not use this strategy for speculative or weak stocks

---

## 🧭 Market Scope

**Works Best For:**
- NSE Index (NIFTY, BANKNIFTY)
- Large-cap, fundamentally strong companies

**Avoid:**
- Penny stocks
- Small caps with governance risk
- Companies in structural decline

---

## 📊 Indicators Used

| Indicator | Timeframe | Purpose |
|----------|-----------|---------|
| RSI (14) | Daily     | Detect oversold zones |
| 200 DMA  | Daily     | Identify long-term support zones |

**Optional Enhancers:**
- Weekly RSI
- Monthly RSI

---

## 🎯 Entry Rules (Staged Accumulation)

We accumulate in **three daily-based stages**:

| Stage | Condition | Position Size |
|------|-----------|----------------|
| **Stage 1** | Daily RSI < 40 **and** Price ≤ 5% from 200 DMA | Buy **25%** |
| **Stage 2** | Daily RSI < 35 **and** Price ≤ 3% from 200 DMA | Buy **25%** |
| **Stage 3** | Daily RSI < 30 **and** Price ≤ 1% from 200 DMA | Buy **50%** (Full Base Position Active) |

Stop loss is applied **only after Stage 3**.

---

## 🔥 Extended Opportunity (Rare — Market Panic Conditions)

| Stage | Condition | Extra Allocation | Max Total Position |
|------|-----------|------------------|--------------------|
| **Stage 4 (Super)** | Weekly RSI < 40 **and** Monthly RSI < 50 | Add **50%** | 150% |
| **Stage 5 (Super-Super)** | Weekly RSI < 35 **and** Monthly RSI < 45 | Add **50%** | **200% (Max)** |

SL adjusts to the **latest accumulation zone**.
Maximum allowed drawdown = **10%** from latest entry cluster.

---

## 📤 Exit Strategy

### For Base Position (Stage 1–3)
| Signal | Action |
|--------|--------|
| RSI reaches **70** | Sell **50%** |
| RSI crosses **80** | Sell remaining **50%** |

### For Extended Positions (Stage 4–5)
| Position Type | Exit Timing | Condition |
|---------------|-------------|-----------|
| Stage 4 Position | Weekly RSI Exit | Exit near **Weekly RSI 60–65** |
| Stage 5 Position | Monthly RSI Exit | Exit near **Monthly RSI 60–65** |

Daily exit signals **do not apply** once higher timeframe entries occur.

---

## 🧠 Psychology & Discipline

- You will **buy when others are fearful**
- You will **hold while price stabilizes**
- You will **exit when others become greedy**
- Avoid emotional decisions and news noise
- Keep unused capital parked safely (liquid funds / FD)

This strategy rewards:
- Patience  
- Emotional stability  
- Respect for rules  

---

## 📌 Key Takeaways

- The system is designed to capture **oversold → recovery → overbought** cycles.
- Fewer, high-conviction trades outperform frequent trading.
- Cash sitting idle is a feature, not a flaw.
- The edge is **discipline**, not prediction.

---

## 🔗 Community / Contact

Join the discussion channel:

**Telegram:**  
https://web.telegram.org/k/#@dhanyawadss

---

## 📜 License

This project is shared openly for learning and improvement.  
You are free to use, adapt, extend, and automate it.

