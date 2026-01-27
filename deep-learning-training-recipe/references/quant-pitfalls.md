# Quantitative Strategy Development Pitfalls

Common mistakes and best practices for ML in quantitative trading.

## The Overfitting Problem

Quantitative strategies are extremely prone to overfitting because:
- Financial data is noisy with low signal-to-noise ratio
- Multiple hypothesis testing inflates false discovery rate
- Survivorship bias in historical data
- Regime changes make past patterns unreliable

## Data Leakage Sources

### Point-in-Time Violations
- Using data that wasn't available at prediction time
- Fundamental data: earnings announced after market close but dated to quarter end
- Index membership: using current constituents for historical analysis

### Lookahead Bias
- Features computed using future information
- Normalization using full dataset statistics
- Target leakage in feature engineering

### Train/Test Contamination
- Random splits instead of temporal splits
- Overlapping windows between train and test
- Information leakage through correlated assets

## Validation Methods

### Walk-Forward Validation
```
Fold 1: Train [2010-2014] → Val [2015] → Test [2016]
Fold 2: Train [2011-2015] → Val [2016] → Test [2017]
Fold 3: Train [2012-2016] → Val [2017] → Test [2018]
...
```

### Combinatorial Purged Cross-Validation (CPCV)
- Removes overlapping samples between train and test
- Accounts for serial correlation in financial data
- More robust than standard k-fold for time series

### Embargo Period
- Gap between training and test periods
- Prevents information leakage from autocorrelation
- Typical: 1-5 days for daily strategies

## Transaction Cost Modeling

### Components to Include
- **Commission**: Broker fees per trade
- **Spread**: Bid-ask spread cost
- **Slippage**: Price movement during execution
- **Market impact**: Price movement caused by your order

### Realistic Estimates
| Asset Class | Typical Cost (bps) |
|-------------|-------------------|
| Large-cap equity | 5-20 |
| Small-cap equity | 20-100 |
| Futures | 1-5 |
| FX majors | 1-3 |
| Crypto | 10-50 |

## Multiple Testing Correction

### The Problem
- Testing 100 strategies, expect 5 to pass at p=0.05 by chance
- More backtests = more false discoveries

### Solutions
- **Deflated Sharpe Ratio**: Adjusts for number of trials
- **Bonferroni correction**: Divide alpha by number of tests
- **False Discovery Rate (FDR)**: Control expected proportion of false positives
- **Out-of-sample validation**: Reserve truly untouched data

### Sharpe Ratio Haircuts
| Number of Backtests | Minimum Sharpe for Significance |
|--------------------|--------------------------------|
| 1 | 1.0 |
| 10 | 1.5 |
| 100 | 2.0 |
| 1000 | 2.5 |

## Regime Robustness

### Test Across Market Conditions
- Bull markets (2009-2020)
- Bear markets (2008, 2020 March, 2022)
- High volatility (VIX > 30)
- Low volatility (VIX < 15)
- Rising rates vs falling rates

### Red Flags
- Strategy only works in one regime
- Performance concentrated in few time periods
- Relies on specific market anomaly that may disappear

## Implementation Checklist

### Data Quality
- [ ] Point-in-time data used (no lookahead)
- [ ] Survivorship bias addressed
- [ ] Corporate actions adjusted (splits, dividends)
- [ ] Missing data handled appropriately

### Validation
- [ ] Temporal train/test split (not random)
- [ ] Embargo period between train and test
- [ ] Walk-forward or CPCV validation used
- [ ] Multiple testing correction applied

### Costs
- [ ] Transaction costs modeled realistically
- [ ] Slippage estimated conservatively
- [ ] Capacity constraints considered
- [ ] Strategy still profitable after costs

### Robustness
- [ ] Tested across multiple market regimes
- [ ] Sensitive to hyperparameter changes?
- [ ] Works on related but different assets?
- [ ] Performance not concentrated in few periods

### Production Readiness
- [ ] Execution latency acceptable
- [ ] Data pipeline reliable
- [ ] Risk limits defined
- [ ] Monitoring and alerting in place

## References

- Marcos López de Prado - "Advances in Financial Machine Learning"
- Bailey & López de Prado - "The Deflated Sharpe Ratio"
- de Prado - "The 7 Reasons Most Machine Learning Funds Fail"
