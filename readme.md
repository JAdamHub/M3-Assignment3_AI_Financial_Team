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

### 1. Acquire API Keys
- **GroqChat API Key**: Sign up and retrieve your free API key at:  
  [https://console.groq.com/settings/limits](https://console.groq.com/settings/limits)
- **SERPER SEARCH API Key**: Get your free API key here:  
  [https://serper.dev/dashboard](https://serper.dev/dashboard)

### 2. Clone and Set Up the Repository
Open your terminal and run:
```bash
git clone https://github.com/JAdamHub/M3-Assignment3_AI_Financial_Team.git
cd M3-Assignment3_AI_Financial_Team
pip install -r requirements.txt
```

### 3. Install and Run Flowise (Docker)
Download Docker Desktop:
https://www.docker.com/products/docker-desktop/

Pull and Run Flowise:
```bash
docker pull flowiseai/flowise:latest
docker run -d -p 3000:3000 flowiseai/flowise:latest
```

## 4. Configure Flowise

- **Open your browser and navigate to:**  
  [http://localhost:3000](http://localhost:3000)

- **Import Agentflow:**  
  Import the `Test Agents.json` file into the Agentflows section.

- **Insert Your API Keys in app.py file:**  
  Update the Agentflow configuration with your GroqChat and SERPER DEV API keys.

- **Save the Agentflow:**  
  Ensure you save your imported Agentflow.

## 5. Update the Application Endpoint
Edit app.py to point to your custom Agentflow endpoint:
```bash
# Original endpoint:
http://localhost:3000/api/v1/prediction/9719e978-fd79-4050-8bea-99724ecdb992
# Replace with your Agentflow ID:
http://localhost:3000/api/v1/prediction/[INSERT-YOUR-AGENTFLOW_ID]
```

## 6. Run the Streamlit App:
Launch your application (app.py) by executing:
```bash
streamlit run app.py
```

#### IMPORTANT:
Note:
Ensure your API keys and Agentflow IDs are correctly configured before running the app to avoid any issues.
