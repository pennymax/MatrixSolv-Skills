# Quantitative Trading Paper Evaluation Criteria

Detailed criteria for evaluating quantitative finance and trading strategy research papers.

## Signal Quality Assessment

### Information Coefficient (IC) Analysis

**What is IC:**
- Correlation between predicted signal and future returns
- Measures predictive power of a signal
- Typical range: 0.01 - 0.10 for good signals

**IC Evaluation:**

| IC Value | Interpretation |
|----------|----------------|
| > 0.10 | Exceptional (verify carefully - may be overfit) |
| 0.05 - 0.10 | Strong signal |
| 0.02 - 0.05 | Moderate signal (typical for real alpha) |
| 0.01 - 0.02 | Weak but potentially usable |
| < 0.01 | Noise |

**IC Stability:**
- Rolling IC should be consistent across time
- Check IC in different market regimes
- Beware of IC that's high only in certain periods

### Information Ratio (IR)

**Formula:** IR = IC × √(Breadth)

**Interpretation:**
- IR > 0.5: Good strategy
- IR > 1.0: Excellent strategy
- IR > 2.0: Verify carefully (likely overfit)

### T-Statistics

**Requirements:**
- t-stat > 2.0 for statistical significance
- Adjust for multiple testing (Bonferroni, FDR)
- Report degrees of freedom

## Backtest Validity

### Critical Biases to Check

#### 1. Look-Ahead Bias
**Definition:** Using information not available at decision time

**Common Sources:**
- Point-in-time data issues
- Using revised economic data
- Future information in features
- Improper timestamp handling

**How to Detect:**
- Check data timestamps carefully
- Verify point-in-time database usage
- Look for suspiciously good results

#### 2. Survivorship Bias
**Definition:** Only including assets that survived to present

**Impact:**
- Overstates returns by 1-2% annually
- Understates risk

**Mitigation:**
- Use survivorship-bias-free databases
- Include delisted securities
- Account for mergers/acquisitions

#### 3. Data Snooping / Overfitting
**Definition:** Finding patterns by testing many hypotheses

**Warning Signs:**
- Many parameters relative to data
- Complex rules without economic rationale
- Results don't hold out-of-sample
- Strategy only works on specific period

**Mitigation:**
- Out-of-sample testing
- Walk-forward validation
- Multiple testing correction
- Economic rationale for signals

### Transaction Cost Modeling

**Components to Include:**

| Cost Type | Typical Range | Notes |
|-----------|---------------|-------|
| Commission | 0.1-1 bp | Varies by broker/volume |
| Spread | 1-10 bp | Depends on liquidity |
| Market Impact | 5-50 bp | Depends on order size |
| Slippage | 1-5 bp | Execution vs. signal price |

**Red Flags:**
- No transaction costs mentioned
- Unrealistically low costs
- Ignoring market impact for large positions
- Not accounting for capacity constraints

### Walk-Forward Validation

**Proper Protocol:**
1. In-sample: Develop and tune strategy
2. Out-of-sample: Test without modification
3. Walk-forward: Rolling in-sample/out-of-sample

**Time Periods:**
- Pre-2008: Different market regime
- 2008-2010: Crisis period
- Post-2010: Modern HFT era
- Strategy should work across regimes

## Performance Metrics

### Return Metrics

| Metric | Formula | Good Value |
|--------|---------|------------|
| Annual Return | Geometric mean | > Risk-free + 5% |
| Sharpe Ratio | (Return - Rf) / Volatility | > 1.0 |
| Sortino Ratio | (Return - Rf) / Downside Vol | > 1.5 |
| Calmar Ratio | Return / Max Drawdown | > 1.0 |

### Risk Metrics

| Metric | What It Measures | Concern Level |
|--------|------------------|---------------|
| Max Drawdown | Worst peak-to-trough | > 20% concerning |
| Volatility | Return standard deviation | Context-dependent |
| VaR (95%) | Worst 5% of days | Should be disclosed |
| Tail Risk | Extreme loss frequency | Often underestimated |

### Robustness Metrics

| Metric | Purpose |
|--------|---------|
| Win Rate | % of profitable trades |
| Profit Factor | Gross profit / Gross loss |
| Average Win/Loss | Ratio of avg win to avg loss |
| Recovery Time | Time to recover from drawdown |

## Implementation Feasibility

### Data Requirements

**Questions to Ask:**
- Is the data publicly available?
- What is the cost?
- What is the latency?
- Is there survivorship-bias-free history?

**Data Quality Issues:**
- Missing data handling
- Corporate action adjustments
- Time zone considerations
- Data vendor differences

### Execution Requirements

| Factor | Assessment Questions |
|--------|---------------------|
| Latency | How fast must signals be acted on? |
| Frequency | How often does strategy trade? |
| Capacity | How much capital can strategy handle? |
| Liquidity | Are target assets liquid enough? |

### Capacity Constraints

**Estimating Capacity:**
- ADV (Average Daily Volume) of traded assets
- Typical rule: Trade < 1-5% of ADV
- Market impact increases with size

**Warning Signs:**
- No capacity discussion
- Backtested on illiquid assets
- Unrealistic position sizes

## Red Flags Specific to Quant Papers

### Too Good to Be True

| Metric | Suspicious Level |
|--------|------------------|
| Sharpe Ratio | > 3.0 without HFT |
| Annual Return | > 50% consistently |
| Win Rate | > 70% for trend following |
| Max Drawdown | < 5% for equity strategies |

### Missing Information

**Must Be Disclosed:**
- [ ] Exact backtest period
- [ ] Universe selection criteria
- [ ] Rebalancing frequency
- [ ] Transaction cost assumptions
- [ ] Slippage model
- [ ] Data source

### Methodology Issues

1. **In-Sample Optimization**
   - Parameters tuned on full dataset
   - No true out-of-sample test

2. **Selection Bias**
   - Cherry-picked time period
   - Favorable market conditions only

3. **Curve Fitting**
   - Too many parameters
   - Complex rules without rationale

## Quality Scoring for Quant Papers

### Backtest Credibility Score

| Score | Description |
|-------|-------------|
| 5 | Institutional quality - All biases addressed, realistic costs, robust validation |
| 4 | Strong - Minor issues, mostly credible |
| 3 | Moderate - Some concerns, needs verification |
| 2 | Weak - Significant issues, likely overfit |
| 1 | Unreliable - Major biases, not trustworthy |

### Implementation Readiness Score

| Score | Description |
|-------|-------------|
| 5 | Ready to implement - All details provided |
| 4 | Minor gaps - Some details need clarification |
| 3 | Moderate gaps - Significant work to implement |
| 2 | Major gaps - Core methodology unclear |
| 1 | Not implementable - Insufficient information |
