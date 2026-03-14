
# Project Title

A brief description of what this project does and who it's for

# Hyperliquid Trader Behavior Analysis Using Market Sentiment

## Project Overview
This project analyzes trader behavior using historical trading data and the Fear & Greed market sentiment index.

The goal is to understand how market sentiment influences trader activity, profit/loss, and trading behavior.

---

## Dataset

Two datasets were used:

1. Trader Historical Data
- Account
- Timestamp
- Closed PnL
- Size USD
- Size Tokens
- Side

2. Fear & Greed Sentiment Data
- Date
- Classification (Fear, Greed, Neutral, etc.)

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Methodology

1. Data cleaning
2. Removing duplicates
3. Converting timestamps to date format
4. Merging trader data with sentiment data
5. Creating trader segments
6. Visualizing insights using charts

---

## Trader Segmentation

Traders were divided into:

1. High vs Low Leverage Traders
2. Frequent vs Infrequent Traders
3. Consistent Winners vs Inconsistent Traders

---

## Key Insights

### Insight 1
PnL distribution becomes more volatile during Greed market conditions because traders take more aggressive positions.

### Insight 2
Trading activity increases during Fear and Greed periods, indicating that traders respond strongly to emotional market signals.

### Insight 3
Trade sizes increase during uncertain market conditions such as Fear or Neutral phases.

---

## Strategy Recommendations

1. Use strong risk management during Greed markets.
2. Adjust position sizes based on market sentiment.
3. Monitor sentiment indicators to avoid emotional trading decisions.

---

## Author

Vishal Singh Rawat  
Final Year – Computer Science & Engineering  
Birla Institute of Applied Science, Bhimtal