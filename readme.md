# 🚀 Financial Stock Analysis Suite

**AI-Powered Fundamental, Technical & Sentiment Analysis for Stocks/ETFs**

## 📌 Overview
Advanced analytics platform combining three AI-powered analysis methodologies:
1. **Fundamental Analysis** - Financial health & valuation metrics  
2. **Technical Analysis** - Price patterns & trading signals  
3. **Sentiment Analysis** - Market psychology & news trends  

Powered by Flowise AI agents with real-time data integration via Serper API.

## ✨ Features
- **3-in-1 Analysis Modules**
  - 📊 Fundamental Health Check (P/E, ROE, Debt Ratios)
  - 📈 Technical Pattern Recognition (RSI, MACD, Support/Resistance)
  - 🧠 Sentiment Radar (News/Social Media Monitoring)
- Real-time market data integration
- Streaming AI response system
- SEC filings & earnings call analysis
- Actionable investment recommendations
- Source citation for all data points

## 🛠️ Instructions
```bash
git clone https://github.com/JAdamHub/M3-Assignment3_AI_Financial_Team.git
cd M3-Assignment3_AI_Financial_Team
pip install -r requirements.txt
```
- Install latest version of Flowise (Docker):
https://www.docker.com/products/docker-desktop/

```bash
docker pull flowiseai/flowise:latest
docker run -d -p 3000:3000 flowiseai/flowise:latest
```

- Access localhost through URL in a Browser:
```bash
http://localhost:3000
```

- Import Test Agents.json file in Agentflows under Flowise
- Save the the Agentflow
- Edit app.py to include your own version of:

```bash
http://localhost:3000/api/v1/prediction/9719e978-fd79-4050-8bea-99724ecdb992
# TO:
http://localhost:3000/api/v1/prediction/[INSERT-YOUR-AGENTFLOW_ID]
```

Run app.py as streamlit app:
```bash
streamlit run app.py
```
