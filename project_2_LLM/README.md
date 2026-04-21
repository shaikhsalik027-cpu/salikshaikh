📱 WhatsApp LLM‑Powered Stock Insights & Paper Trading Agent
Overview
This project is an AI‑powered WhatsApp agent that delivers daily and weekly stock market insights, responds to natural‑language investment queries, and simulates buy/sell actions using a paper‑trading engine.
The system combines LLM reasoning, market data analysis, and event‑driven backend services to act as a decision‑support assistant rather than an automated trading bot.

⚠️ Disclaimer
This project is for educational and experimental purposes only. It does not provide financial or investment advice. All trades are simulated using a paper‑trading mechanism — no real money transactions are executed.


Key Features

📩 WhatsApp Interface for natural language interaction
🧠 LLM‑based Agent to understand user intent and generate explanations
📊 Market Data Analysis with technical indicators (RSI, Moving Averages, Trends)
📈 Paper Trading Engine to simulate buy/sell decisions and track portfolio PnL
⏱️ Scheduled Insights

Daily market summary
Weekly portfolio performance report


🔍 Explainable Insights

Why a stock moved
What indicators suggest
Risk and volatility context




Example Interactions
Users can interact with the agent via WhatsApp messages such as:
daily market summary
weekly portfolio report
analyze INFY
buy RELIANCE 10 shares (paper)
why is TCS falling today?

The agent responds with concise, interpretable explanations, not just buy/sell signals.

System Architecture
WhatsApp (User)
      ↓
WhatsApp API (Twilio)
      ↓
FastAPI Backend
      ↓
LLM Agent (Intent + Reasoning)
      ↓
Market Data & Indicator Services
      ↓
Insights / Alerts / Paper Trades

The architecture is modular and designed for extensibility and safe experimentation.

LLM Agent Design
The LLM agent acts as an orchestrator, not a predictor:

Interprets user intent (query, analysis, trade simulation)
Calls predefined tools (market data, indicators, portfolio)
Generates natural‑language explanations grounded in data
Applies guardrails to avoid unsupported financial claims

This design follows tool‑augmented LLM agent principles rather than prompt‑only responses.

Paper Trading Logic
To ensure safety and realism:

All trades are simulated
Portfolio state is persisted locally
Performance metrics include:

Entry price
Exit price
Unrealized / realized PnL


Weekly performance summaries are generated automatically

This allows experimentation with strategies without financial risk.

Repository Structure
Plain Textwhatsapp-llm-stock-agent/│├── app/│   ├── main.py              # FastAPI entry point│   ├── whatsapp_webhook.py  # WhatsApp message handling│   └── scheduler.py         # Daily / weekly jobs│├── agent/│   ├── llm_agent.py         # Core agent logic│   ├── prompts.py           # System and tool prompts│   └── tools.py             # Callable tools for the agent│├── services/│   ├── market_data.py       # Market data fetching│   ├── indicators.py        # Technical indicators│   └── paper_trading.py     # Virtual trading engine│├── data/│   └── portfolio.json       # Simulated portfolio state│├── README.md├── requirements.txt└── .env.exampleShow more lines

Tech Stack

Backend: Python, FastAPI
LLM: OpenAI / Azure OpenAI / Local LLM (pluggable)
Messaging: WhatsApp via Twilio
Data Processing: Pandas, NumPy
Scheduling: Cron / Background tasks
Visualization & Reporting: Text‑based insights via WhatsApp


Why This Project Matters
This project demonstrates:

✅ Practical use of LLMs as agents
✅ Event‑driven backend design
✅ Safe application of AI in sensitive domains
✅ Emphasis on explainability and decision support
✅ Real‑world messaging interface beyond chat UIs

It is designed to reflect production‑quality thinking, not a demo bot.

Possible Future Extensions

Web dashboard for portfolio visualization
Strategy backtesting engine
Multi‑user support
Risk scoring and alerting
Integration with additional market data sources


Author
Salik Shaikh
Python • Machine Learning • AI Automation
LinkedIn: https://www.linkedin.com/in/salikshaikh/