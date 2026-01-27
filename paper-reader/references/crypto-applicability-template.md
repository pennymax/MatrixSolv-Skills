# Cryptocurrency Applicability Analysis Template

Use this template when analyzing papers that do NOT explicitly discuss cryptocurrency applications.

---

## Cryptocurrency Market Applicability

### Paper Information
- **Title**: [Paper Title]
- **Original Domain**: [e.g., Stock market, Weather, Energy]
- **Method Type**: [e.g., Time series forecasting, Anomaly detection]

---

### 1. Relevance Assessment

**Overall Crypto Applicability**: [HIGH / MEDIUM / LOW]

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| Method-market fit | | |
| Data compatibility | | |
| Volatility handling | | |
| Real-time feasibility | | |
| **Average** | | |

---

### 2. Method-Market Fit Analysis

#### Strengths for Crypto Markets

| Paper's Strength | Crypto Benefit |
|------------------|----------------|
| [e.g., Handles distribution shift] | [e.g., Suits crypto regime changes] |
| [e.g., Low latency inference] | [e.g., Enables HFT applications] |
| [e.g., Robust to outliers] | [e.g., Handles flash crashes] |

#### Potential Challenges

| Challenge | Severity | Mitigation |
|-----------|----------|------------|
| [e.g., Assumes stationarity] | HIGH/MED/LOW | [e.g., Add regime detection] |
| [e.g., Requires large datasets] | HIGH/MED/LOW | [e.g., Use multi-asset training] |
| [e.g., Slow inference] | HIGH/MED/LOW | [e.g., Model distillation] |

---

### 3. Crypto-Specific Considerations

#### Data Characteristics Comparison

| Aspect | Paper's Data | Crypto Reality | Gap Analysis |
|--------|--------------|----------------|--------------|
| **Frequency** | [e.g., Daily] | Tick to daily | [Adaptation needed?] |
| **Volatility** | [e.g., 1-2% daily] | 5-20%+ daily | [Scaling required?] |
| **Distribution** | [e.g., Near-normal] | Fat-tailed, skewed | [Robustness issue?] |
| **Stationarity** | [e.g., Assumed] | Highly non-stationary | [Critical concern?] |
| **Missing data** | [e.g., Rare] | Exchange outages common | [Handling needed?] |
| **Market hours** | [e.g., 6.5h/day] | 24/7/365 | [Model adjustment?] |

#### Market Microstructure

| Factor | Paper's Assumption | Crypto Reality |
|--------|-------------------|----------------|
| Liquidity | [e.g., High] | Varies by asset/exchange |
| Spread | [e.g., Tight] | 5-100+ bps |
| Market impact | [e.g., Linear] | Non-linear, thin books |
| Order types | [e.g., Market/Limit] | + Conditional, TWAP, etc. |

---

### 4. Recommended Crypto Assets

Based on method characteristics:

#### Primary Recommendations

| Asset | Ticker | Why Suitable | Caution |
|-------|--------|--------------|---------|
| Bitcoin | BTC | [e.g., Best data quality, liquidity] | [e.g., Correlation with macro] |
| Ethereum | ETH | [e.g., DeFi ecosystem, smart contracts] | [e.g., Gas fee volatility] |

#### Secondary Recommendations

| Asset | Ticker | Why Suitable | Caution |
|-------|--------|--------------|---------|
| [e.g., Solana] | SOL | [e.g., Higher volatility for testing] | [e.g., Network outages] |
| [e.g., BNB] | BNB | [e.g., Exchange token dynamics] | [e.g., Centralization risk] |

#### Not Recommended

| Asset Type | Reason |
|------------|--------|
| [e.g., Meme coins] | [e.g., Manipulation, no fundamentals] |
| [e.g., Low-cap alts] | [e.g., Insufficient liquidity] |

---

### 5. Implementation Roadmap

#### Phase 1: Validation (1-2 weeks)
- [ ] Obtain historical crypto data (BTC/ETH minimum)
- [ ] Adapt preprocessing for crypto characteristics
- [ ] Run baseline experiments on historical data
- [ ] Compare with paper's reported metrics

#### Phase 2: Adaptation (2-4 weeks)
- [ ] Modify model for 24/7 trading
- [ ] Add crypto-specific features (funding rates, on-chain, etc.)
- [ ] Implement proper backtesting with realistic costs
- [ ] Test across multiple market regimes

#### Phase 3: Live Testing (4+ weeks)
- [ ] Paper trading with real-time data
- [ ] Monitor for distribution shift
- [ ] Measure actual vs. expected performance
- [ ] Iterate based on findings

---

### 6. Risk Assessment

#### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Model degradation | | | |
| Data quality issues | | | |
| Latency problems | | | |
| Overfitting to regime | | | |

#### Market Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Flash crash | | | |
| Exchange failure | | | |
| Regulatory change | | | |
| Liquidity crisis | | | |

---

### 7. Verdict

#### Crypto Applicability Score: [X/10]

| Score Range | Interpretation |
|-------------|----------------|
| 8-10 | Directly applicable, high potential value |
| 5-7 | Applicable with moderate modifications |
| 3-4 | Significant adaptation required |
| 1-2 | Not recommended for crypto markets |

#### Summary

**Strengths**:
1. [Key strength 1]
2. [Key strength 2]
3. [Key strength 3]

**Weaknesses**:
1. [Key weakness 1]
2. [Key weakness 2]
3. [Key weakness 3]

#### Final Recommendation

[Detailed recommendation: Should this method be pursued for crypto? What modifications are essential? What's the expected effort vs. potential reward?]

---

### 8. References & Resources

#### Crypto Data Sources
- Binance API: https://binance-docs.github.io/apidocs/
- CoinGecko API: https://www.coingecko.com/en/api
- Glassnode: https://glassnode.com/
- CryptoCompare: https://min-api.cryptocompare.com/

#### Related Crypto ML Papers
- [List relevant papers that have applied similar methods to crypto]

#### Useful Libraries
- `ccxt`: Unified crypto exchange API
- `ta-lib`: Technical analysis
- `vectorbt`: Backtesting framework
- `freqtrade`: Trading bot framework
