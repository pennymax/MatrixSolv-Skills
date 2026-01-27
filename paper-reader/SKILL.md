---
name: paper-reader
description: Structured methodology for reading and understanding machine learning and quantitative trading research papers from PDF. Use when analyzing academic papers from arXiv, SSRN, NeurIPS, ICML, JFE, or similar sources. Supports four reading modes - (1) Quick screening to decide if paper is worth reading, (2) Deep understanding of methods and contributions, (3) Implementation-focused analysis for reproducing results, (4) Critical evaluation of limitations and validity. Triggers on requests like "analyze this paper", "summarize this research", "help me understand this ML paper", "evaluate this trading strategy paper", or when given a PDF research paper to read.
---

# Paper Reader

Read and analyze machine learning and quantitative trading research papers using structured expert methodologies.

## Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `<url/path>` | Paper URL or local file path | `https://arxiv.org/abs/2410.09836` |
| `--mode` | Analysis mode | `--mode deep` |
| `--output` | Output directory for saving reports | `--output ./papers/my-paper/` |

**Usage Examples**:
```bash
# Basic usage (output to console)
/paper-reader https://arxiv.org/abs/2410.09836

# Deep analysis with output directory
/paper-reader https://arxiv.org/abs/2410.09836 --mode deep --output ./analysis/

# Quick screening
/paper-reader paper.pdf --mode quick

# Implementation-focused analysis
/paper-reader https://arxiv.org/abs/2410.09836 --mode implement --output ./impl-notes/
```

## Reading Modes

Select mode based on user's goal:

| Mode | Goal | Output Files |
|------|------|--------------|
| `quick` | Decide if worth reading | `quick-screening.md` |
| `deep` | Full understanding | `deep-analysis.md`, `crypto-applicability.md` |
| `implement` | Reproduce/implement | `deep-analysis.md`, `implementation-notes.md`, `crypto-applicability.md` |
| `critical` | Evaluate validity | `deep-analysis.md`, `critical-evaluation.md`, `crypto-applicability.md` |

Default to `deep` if unspecified.

## Quality Requirements (MANDATORY)

**CRITICAL**: All outputs MUST meet minimum quality standards. Do NOT produce abbreviated or skeleton reports.

### Deep Analysis Minimum Requirements

The `deep-analysis.md` file MUST include ALL of the following sections with substantive content:

| Section | Minimum Content |
|---------|-----------------|
| Executive Summary | 3-5 sentences summarizing core contribution |
| Problem & Motivation | Research question, importance, gap in existing work, key assumptions |
| Proposed Approach | Core idea, key components table, technical details with equations, architecture diagram, comparison with prior work |
| Experiments & Results | Datasets table, main results table with numbers, key findings (3+), ablation studies |
| Strengths & Weaknesses | 3+ strengths, 3+ weaknesses, acknowledged and unacknowledged limitations |
| Relevance Assessment | Scoring table (5 criteria), recommended action |
| Key Takeaways | Main contributions, ideas to explore, related papers |
| Quick Reference | One-line summary, key equation/algorithm, citation |
| Code Discovery Results | Search results table, repository structure (if found), evaluation, recommendation |

**Minimum Length**: `deep-analysis.md` should be **250+ lines** for a thorough analysis.

### Crypto Applicability Minimum Requirements

| Section | Minimum Content |
|---------|-----------------|
| Relevance Assessment | Scoring table with 4+ criteria |
| Method-Market Fit | Strengths table, challenges table with mitigations |
| Crypto-Specific Considerations | Data characteristics comparison table |
| Recommended Assets | Primary and secondary recommendations with reasons |
| Implementation Roadmap | Phased plan with checkboxes |
| Risk Assessment | Technical and market risk tables |
| Verdict | Score (1-10), summary, final recommendation |

**Minimum Length**: `crypto-applicability.md` should be **150+ lines**.

### OpenReview Summary Requirements

If OpenReview reviews are found, the summary MUST include:
- Paper decision and venue
- Reviewer ratings (if accessible)
- Key strengths identified by reviewers
- Key concerns raised
- Author response summary (if available)

## Output File Naming Convention

**IMPORTANT**: When `--output` is specified:

1. **Create a subdirectory** named after the paper (simplified, lowercase, hyphenated)
2. Place all output files in this subdirectory
3. Use fixed filenames for each file type

### Paper Directory Naming Rules

Generate directory name from paper title:
- Convert to lowercase
- Replace spaces with hyphens
- Remove special characters (colons, parentheses, etc.)
- Truncate to ~50 characters if too long
- Keep key identifying words

**Examples**:
| Paper Title | Directory Name |
|-------------|----------------|
| TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting | `timemixer-multiscale-mixing` |
| Attention Is All You Need | `attention-is-all-you-need` |
| BERT: Pre-training of Deep Bidirectional Transformers | `bert-pretraining-transformers` |

### File Names

| File | Filename | Description |
|------|----------|-------------|
| Quick Screening | `quick-screening.md` | Quick mode output |
| Deep Analysis | `deep-analysis.md` | Main analysis report |
| Implementation Notes | `implementation-notes.md` | Code/algorithm details |
| Critical Evaluation | `critical-evaluation.md` | Validity assessment |
| Crypto Applicability | `crypto-applicability.md` | Crypto market analysis |
| OpenReview Summary | `openreview-summary.md` | Expert reviews (if found) |

### Directory Structure Example

```
<output-dir>/
└── <paper-name>/                  # e.g., timemixer-multiscale-mixing/
    ├── deep-analysis.md           # Main report (always created for deep/implement/critical)
    ├── crypto-applicability.md    # Crypto analysis (if applicable)
    ├── implementation-notes.md    # Implementation details (implement mode)
    ├── critical-evaluation.md     # Critical assessment (critical mode)
    └── openreview-summary.md      # Expert reviews (if found)
```

**CRITICAL**: You MUST create the paper subdirectory BEFORE writing any files. Use `mkdir -p` to ensure the directory exists.

## Workflow

**⚠️ MANDATORY WORKFLOW COMPLIANCE ⚠️**

You MUST execute ALL steps in order. Do NOT skip steps or combine them incorrectly.

**Pre-flight Checklist (Before Starting)**:
```
□ Parse arguments: URL/path, --mode, --output
□ If --output specified, prepare output directory path: <output>/<paper-name>/
□ Confirm mode (default: deep)
```

**Execution Order (STRICT)**:
1. Step 1: Extract Paper Content → Get title, content, code links
2. Step 2: Identify Paper Type → Classify for evaluation framework
3. Step 3: Execute Reading Mode → Generate main analysis
4. Step 4: Supplementary Information → Code search, OpenReview (ALL methods in order)
5. Step 5: Quality Verification → Check ALL requirements before completing

**DO NOT**:
- Skip to writing files before completing Step 1-3
- Skip OpenReview API attempt and go directly to fallback
- Use Playwright for OpenReview (it times out due to heavy JS)
- Submit incomplete reports that don't meet minimum line requirements
- Write files to wrong directory structure

---

### Step 1: Extract Paper Content

**First, fetch the paper content.** Code links are typically embedded in the paper itself.

Use WebFetch for URLs or the `pdf` skill for local files:

```
WebFetch prompt (comprehensive extraction):
"Extract the complete paper content including:
1. Title, authors, affiliations, abstract
2. GitHub/GitLab repository URLs (check abstract, footnotes, acknowledgments)
3. Code availability statements
4. Full methodology with technical details
5. Experiment details: datasets, baselines, results
6. Conclusion and limitations

Return ALL URLs found with their location in the paper."
```

```python
# For local PDFs
import pdfplumber
with pdfplumber.open("paper.pdf") as pdf:
    text = "\n".join(page.extract_text() or "" for page in pdf.pages)
```

**Code Link Extraction**: During content extraction, note any code/repository links found in:
- Abstract (most common for arXiv papers)
- Footnotes on first page
- "Code Availability" section
- Acknowledgments

**After Step 1 Completion**: If `--output` is specified, create the output directory:
```bash
# Generate paper directory name from title
# Example: "TimeMixer: Decomposable Multiscale Mixing" → "timemixer-multiscale-mixing"
mkdir -p <output-dir>/<paper-name>/
```

### Step 2: Identify Paper Type

Classify the paper to apply appropriate evaluation framework:

| Type | Indicators | Evaluation Focus |
|------|------------|------------------|
| **ML Theory** | Novel architecture, loss function, optimization | Architecture innovation, theoretical soundness |
| **ML Applied** | Benchmark results, SOTA comparison | Experiment rigor, reproducibility |
| **Quant Finance** | Alpha, Sharpe, backtest results | Signal stability, implementation feasibility |
| **ML+Quant** | ML for trading, prediction models | Both ML rigor AND trading viability |

### Step 3: Execute Reading Mode

#### Quick Mode

Extract and analyze in order:
1. **Title + Abstract** - Core claim and approach
2. **Figures/Tables** - Key results at a glance
3. **Conclusion** - What they claim to achieve
4. **Introduction (last paragraph)** - Contribution summary

**Output file**: `quick-screening.md`

```markdown
## Quick Screening: [Paper Title]

**Core Claim**: [One sentence]
**Approach**: [Method in 2-3 sentences]
**Key Results**: [Main numbers/findings]
**Code Available**: [Yes/No - URL if yes]
**Verdict**: [READ / SKIP / SKIM] - [Reason]
**Crypto Applicability**: [HIGH / MEDIUM / LOW / NOT APPLICABLE]
```

#### Deep Mode

Analyze using IMRaD structure:

**Introduction Analysis:**
- What problem is being solved?
- Why is it important?
- What gap in existing work?
- What is the hypothesis/claim?

**Methods Analysis:**
- What is the core approach?
- What are the key assumptions?
- What data is used?
- What baselines are compared?

**Results Analysis:**
- What metrics are reported?
- How significant are improvements?
- Are results statistically valid?
- What ablations are shown?

**Discussion Analysis:**
- What limitations are acknowledged?
- What future work is suggested?
- How generalizable are findings?

**Output files**:
- `deep-analysis.md` (use `references/deep-analysis-template.md`)
- `crypto-applicability.md` (if applicable)

#### Implement Mode

Focus on reproducibility with **code reuse priority**:

##### Algorithm Extraction (if implementing from scratch)

Only proceed here if no suitable existing code found:

1. **Algorithm Extraction**
   - Identify all algorithms (main + auxiliary)
   - Extract pseudocode or create from description
   - Note hyperparameters and their values

2. **Data Requirements**
   - Dataset specifications
   - Preprocessing steps
   - Train/val/test splits

3. **Architecture Details** (for ML papers)
   - Layer configurations
   - Activation functions
   - Normalization methods
   - Input/output dimensions

4. **Implementation Checklist**
   - Required libraries
   - Compute requirements
   - Training time estimates
   - Known implementation pitfalls

**Output files**:
- `deep-analysis.md`
- `implementation-notes.md` (use `references/implementation-template.md`)
- `crypto-applicability.md` (if applicable)

#### Critical Mode

Evaluate validity and limitations:

**For ML Papers:**
- [ ] Fair baseline comparison?
- [ ] Sufficient ablation studies?
- [ ] Statistical significance reported?
- [ ] Reproducibility info provided?
- [ ] Compute requirements disclosed?
- [ ] Failure cases discussed?

**For Quant Papers:**
- [ ] Out-of-sample testing?
- [ ] Transaction costs included?
- [ ] Slippage accounted for?
- [ ] Survivorship bias addressed?
- [ ] Look-ahead bias avoided?
- [ ] Multiple testing correction?

**Output files**:
- `deep-analysis.md`
- `critical-evaluation.md` (use `references/critical-template.md`)
- `crypto-applicability.md` (if applicable)

### Step 4: Supplementary Information (After Main Analysis)

**After understanding the paper content**, gather supplementary information to enhance the analysis.

#### 4.1 External Code Search (If Not Found in Paper)

If no code link was found during Step 1, search external sources:

**Search Priority Order**:

1. **Papers With Code** (Highest reliability for ML papers)
   ```
   WebSearch: site:paperswithcode.com "[paper title]"
   ```

2. **GitHub with Author Name + Method Name**
   ```
   GitHub Search: "[first author name]" "[method name or acronym]"
   Example: "Yanru Sun" "TFPS"
   ```

3. **GitHub with Paper Title**
   ```
   GitHub Search: "[paper title keywords]" language:Python
   ```

4. **Author's GitHub Profile**
   - Search GitHub users for author profiles
   - Check their repositories

**Evaluate Found Code**:

| Criteria | Weight | Check |
|----------|--------|-------|
| Official (by authors) | ★★★ | Is it from paper authors? |
| Stars/Forks | ★★ | Community validation |
| Recency | ★★ | Last update < 2 years? |
| Documentation | ★★ | README, examples exist? |
| License | ★★★ | Permissive for our use? |

#### 4.2 OpenReview Search (For ML Conference Papers)

**When to search**: For papers from NeurIPS, ICLR, ICML, AAAI, ACL, EMNLP, or other ML conferences.

**⚠️ CRITICAL: USE API FIRST - Playwright is unreliable for OpenReview**

OpenReview uses heavy JavaScript rendering. Playwright frequently times out or fails to load content. **Always use the API method first.**

---

**Step 1: Search for OpenReview URL**
```
WebSearch: site:openreview.net "[paper title]" [venue] [year]
Example: site:openreview.net "iTransformer" ICLR 2024
```

Extract forum ID from URL: `https://openreview.net/forum?id=JePfAI8fah` → `JePfAI8fah`

---

**Step 2: Fetch Reviews via API (PRIMARY METHOD)**

**MANDATORY**: You MUST use the Bash tool to execute the API script. This is the ONLY reliable method.

```bash
# Execute from skill directory
cd /home/pennymax/.claude/skills/paper-reader && python -c "
from scripts.openreview_api import OpenReviewFetcher, format_reviews_markdown

forum_id = 'JePfAI8fah'  # Replace with actual forum ID

try:
    fetcher = OpenReviewFetcher()
    reviews = fetcher.get_reviews(forum_id=forum_id)

    if reviews:
        print(f'SUCCESS: Found {len(reviews)} reviews')
        result = {
            'success': True,
            'paper': {
                'title': 'Paper Title',  # Replace with actual title
                'venue': 'ICLR 2024',     # Replace with actual venue
                'decision': 'Accept',      # Replace if known
                'url': f'https://openreview.net/forum?id={forum_id}'
            },
            'reviews': [r.to_dict() for r in reviews]
        }
        print(format_reviews_markdown(result))
    else:
        print('No reviews found')
except Exception as e:
    print(f'API Error: {e}')
"
```

**API Requirements**: `pip install openreview-py` (usually pre-installed)

---

**Step 3: Fallback - Inform User (ONLY IF API FAILS)**

If the API fails (e.g., network error, package not installed), provide the URL:
```
"OpenReview reviews available at: https://openreview.net/forum?id=[forum_id]
API fetch failed: [error message]
Please visit the link to view reviews manually."
```

**DO NOT use Playwright for OpenReview** - it consistently times out due to heavy JavaScript rendering.

---

**Output**: Save to `openreview-summary.md` if reviews found.

#### 4.3 Update Analysis Report

After gathering supplementary information:
1. Add `Code Discovery Results` section to the main report
2. Create `openreview-summary.md` if reviews were found
3. Update recommendations based on code availability and reviewer feedback

### Step 5: Quality Verification (BEFORE COMPLETING)

**MANDATORY**: Before finishing, verify all outputs meet quality requirements.

#### Directory Structure Check (If --output specified)

```
□ Output directory exists: <output-dir>/<paper-name>/
□ All files are in the correct subdirectory (NOT in <output-dir>/ directly)
□ Directory name follows naming convention (lowercase, hyphenated)
```

#### Checklist for Deep Mode

```
□ deep-analysis.md created and contains:
  □ Executive Summary (3-5 sentences)
  □ Problem & Motivation (research question, importance, gap, assumptions)
  □ Proposed Approach (core idea, components table, technical details, equations)
  □ Experiments & Results (datasets table, results table, findings, ablations)
  □ Strengths & Weaknesses (3+ each, limitations)
  □ Relevance Assessment (scoring table, recommendation)
  □ Key Takeaways (contributions, ideas, related papers)
  □ Quick Reference (one-liner, equation, citation)
  □ Code Discovery Results (search results, evaluation)
  □ File is 250+ lines

□ crypto-applicability.md created (if applicable) and contains:
  □ Relevance Assessment (scoring table)
  □ Method-Market Fit (strengths, challenges)
  □ Crypto-Specific Considerations (comparison table)
  □ Recommended Assets (with reasons)
  □ Implementation Roadmap (phased plan)
  □ Risk Assessment (technical, market)
  □ Verdict (score, recommendation)
  □ File is 150+ lines

□ OpenReview (for ML conference papers):
  □ Searched for OpenReview URL via WebSearch
  □ Extracted forum ID from URL
  □ Executed API fetch via Bash (scripts/openreview_api.py)
  □ Created openreview-summary.md if reviews found
  □ If API failed, provided URL for manual access
```

#### If Quality Check Fails

If any output does not meet requirements:
1. **Do NOT submit incomplete work**
2. Go back and expand the deficient sections
3. Re-verify before completing

## OpenReview Reference

### Supported Venues

| Venue | ID Pattern | Notes |
|-------|------------|-------|
| NeurIPS | `NeurIPS.cc/YYYY` | 2017+ |
| ICLR | `ICLR.cc/YYYY` | 2018+ |
| ICML | `ICML.cc/YYYY` | 2019+ |
| AAAI | `AAAI.org/YYYY` | Limited |
| ACL | `aclweb.org/ACL/YYYY` | 2020+ |
| EMNLP | `EMNLP/YYYY` | 2020+ |

### Output Template for `openreview-summary.md`

```markdown
## Expert Reviews (OpenReview)

**Source**: [OpenReview Forum](https://openreview.net/forum?id=XXX)
**Decision**: Accept/Reject
**Reviewer Consensus**: [Summary of reviewer agreement/disagreement]

### Key Reviewer Insights

**Strengths Identified by Reviewers**:
- [Aggregated strengths from multiple reviewers]

**Concerns Raised**:
- [Common weaknesses mentioned]
- [Unresolved questions]

**Author Response Summary**:
- [Key points from rebuttal if available]
```

### Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| "No papers found" | Title mismatch or not on OpenReview | Try exact title from PDF |
| "API v2 failed" | Old conference | Script auto-falls back to v1 |
| Low similarity score | Wrong paper matched | Add venue/year filters |
| Empty reviews | Reviews not public yet | Check if review period ended |

## Domain-Specific Evaluation

### ML Paper Checklist

**Architecture Innovation:**
- What is novel vs existing components?
- Computational complexity analysis?
- Memory requirements?

**Experiment Rigor:**
- Standard benchmarks used?
- Multiple random seeds?
- Error bars/confidence intervals?
- Comparison with recent SOTA?

**Reproducibility:**
- Code available?
- Hyperparameters specified?
- Training details complete?

### Quant Paper Checklist

**Signal Evaluation (from Grinold-Kahn framework):**
- Information Coefficient (IC) reported?
- IC stability across time periods?
- Information Ratio (IR) calculated?
- T-statistics for significance?

**Backtest Validity:**
- Walk-forward validation used?
- Regime changes tested (pre/post 2010)?
- Transaction costs realistic?
- Capacity constraints discussed?

**Implementation Feasibility:**
- Data availability?
- Execution latency requirements?
- Capital requirements?
- Regulatory constraints?

## Cryptocurrency Applicability Analysis

**IMPORTANT**: If the paper does NOT explicitly discuss cryptocurrency applications, ADD this section to evaluate potential applicability to crypto markets.

**Output file**: `crypto-applicability.md` (use `references/crypto-applicability-template.md`)

### When to Include This Section

| Paper Type | Include Crypto Analysis? |
|------------|-------------------------|
| Time series forecasting | **YES** - Always relevant |
| Anomaly detection | **YES** - Market manipulation detection |
| Reinforcement learning | **YES** - Trading strategy potential |
| NLP/Sentiment analysis | **YES** - Social media signals |
| Graph neural networks | **YES** - On-chain analysis |
| General ML architecture | **MAYBE** - If applicable to sequential data |
| Pure theory (no experiments) | **NO** - Unless directly relevant |

### Analysis Depth by Mode

#### Quick Mode: Crypto Applicability (1-2 sentences)

Add to Quick Screening output:

```markdown
**Crypto Applicability**: [HIGH / MEDIUM / LOW / NOT APPLICABLE]
- [One sentence explanation]
```

**Quick Assessment Criteria:**
- HIGH: Directly applicable (time series, trading, anomaly detection)
- MEDIUM: Potentially applicable with modifications
- LOW: Significant adaptation needed
- NOT APPLICABLE: No clear relevance

#### Deep Mode: Crypto Applicability Analysis

Add dedicated section to Deep Analysis:

```markdown
## Cryptocurrency Market Applicability

### Relevance Assessment: [HIGH / MEDIUM / LOW]

### Method-Market Fit Analysis

**Strengths for Crypto Markets:**
- [How the method's strengths align with crypto characteristics]
- [E.g., "Handles non-stationarity well → suits regime changes in crypto"]

**Potential Challenges:**
- [Crypto-specific challenges the method may face]
- [E.g., "Assumes continuous trading → needs adaptation for exchange outages"]

### Crypto-Specific Considerations

| Aspect | Paper's Approach | Crypto Reality | Gap |
|--------|------------------|----------------|-----|
| Data frequency | [e.g., Daily] | [e.g., Tick-level available] | [Adaptation needed?] |
| Volatility regime | [e.g., Moderate] | [e.g., Extreme, 10x+ stocks] | [Robustness concern?] |
| Market hours | [e.g., 6.5h/day] | [24/7/365] | [Model adjustment?] |
| Transaction costs | [e.g., 10bps] | [e.g., 5-50bps + slippage] | [Cost model update?] |

### Recommended Crypto Assets for Testing

Based on method characteristics, suggest appropriate crypto assets:

| Asset Type | Examples | Why Suitable |
|------------|----------|--------------|
| Large-cap | BTC, ETH | [Liquidity, data quality] |
| Mid-cap | SOL, AVAX | [Higher volatility, still liquid] |
| DeFi tokens | UNI, AAVE | [If method handles regime changes] |
| Stablecoins | USDT/USDC pairs | [For spread/arbitrage methods] |

### Implementation Priority: [HIGH / MEDIUM / LOW]

**Verdict**: [Recommendation for crypto implementation]
```

#### Implement Mode: Crypto Implementation Guide

Add to Implementation Notes:

```markdown
## Crypto Implementation Considerations

### Data Sources

| Source | Data Type | Latency | Cost | Notes |
|--------|-----------|---------|------|-------|
| Binance API | OHLCV, Trades | Real-time | Free | Rate limits apply |
| CoinGecko | Price, Market cap | 1-5 min | Free tier | Good for daily |
| Glassnode | On-chain metrics | Daily | Paid | BTC/ETH focus |
| Kaiko | Institutional-grade | Real-time | Expensive | Best quality |
| CryptoCompare | Historical | Varies | Freemium | Good coverage |

### Crypto-Specific Preprocessing

```python
# Example: Handling 24/7 crypto data
def preprocess_crypto_data(df):
    # 1. Handle missing data (exchange outages)
    df = df.fillna(method='ffill', limit=10)

    # 2. Normalize for extreme volatility
    df['returns'] = df['close'].pct_change()
    df['returns_winsorized'] = df['returns'].clip(-0.5, 0.5)

    # 3. Add crypto-specific features
    df['hour_of_day'] = df.index.hour  # 24h patterns
    df['is_weekend'] = df.index.dayofweek >= 5  # Different dynamics

    # 4. Volume normalization (varies wildly)
    df['volume_zscore'] = (df['volume'] - df['volume'].rolling(168).mean()) / df['volume'].rolling(168).std()

    return df
```

### Backtesting Adjustments

| Factor | Traditional | Crypto Adjustment |
|--------|-------------|-------------------|
| Slippage | 1-5 bps | 10-50 bps (size dependent) |
| Trading fees | 5-10 bps | 10-30 bps (maker/taker) |
| Funding rates | N/A | ±0.01-0.1% per 8h (perpetuals) |
| Liquidation risk | Margin call | Instant liquidation |
| Market impact | Linear | Non-linear, thin books |

### Risk Considerations

- [ ] Flash crash handling (e.g., May 2021, -50% in hours)
- [ ] Exchange risk (FTX-style failures)
- [ ] Regulatory risk (varies by jurisdiction)
- [ ] Smart contract risk (for DeFi applications)
- [ ] Oracle manipulation (for on-chain strategies)
```

#### Critical Mode: Crypto Validity Assessment

Add to Critical Evaluation:

```markdown
## Crypto Market Validity Assessment

### Transferability Concerns

| Concern | Severity | Explanation |
|---------|----------|-------------|
| Distribution shift | [HIGH/MED/LOW] | [Crypto distributions differ from paper's data] |
| Regime changes | [HIGH/MED/LOW] | [Bull/bear cycles more extreme] |
| Market efficiency | [HIGH/MED/LOW] | [Crypto less efficient → opportunity or noise?] |
| Data quality | [HIGH/MED/LOW] | [Exchange data reliability issues] |

### Critical Questions for Crypto Application

1. **Stationarity**: Does the method assume stationarity? Crypto is highly non-stationary.
2. **Tail risk**: How does the method handle 10-sigma events (common in crypto)?
3. **Correlation breakdown**: Does it account for correlation spikes during crashes?
4. **Survivorship bias**: Are failed tokens/exchanges considered?
5. **Market manipulation**: Is the method robust to wash trading, spoofing?

### Red Flags for Crypto Application

- [ ] Method assumes normal distribution → Crypto has fat tails
- [ ] Trained on low-volatility assets → May fail in crypto
- [ ] Requires stable correlations → Crypto correlations are unstable
- [ ] Assumes efficient markets → Crypto has known inefficiencies
- [ ] Ignores market microstructure → Critical for crypto execution

### Verdict

**Crypto Applicability Score**: [1-10]

| Score | Meaning |
|-------|---------|
| 8-10 | Directly applicable, high potential |
| 5-7 | Applicable with modifications |
| 3-4 | Significant adaptation needed |
| 1-2 | Not recommended for crypto |

**Recommendation**: [Detailed recommendation for crypto application]
```

### Crypto Analysis Template

See `references/crypto-applicability-template.md` for full template.

## Output Summary

### Files by Mode

| Mode | Output Files |
|------|--------------|
| `quick` | `quick-screening.md` |
| `deep` | `deep-analysis.md`, `crypto-applicability.md` |
| `implement` | `deep-analysis.md`, `implementation-notes.md`, `crypto-applicability.md` |
| `critical` | `deep-analysis.md`, `critical-evaluation.md`, `crypto-applicability.md` |

### Optional Files (created if applicable)

| File | Condition |
|------|-----------|
| `openreview-summary.md` | OpenReview reviews found |
| `crypto-applicability.md` | Paper type is relevant to crypto |

### Console Output Formats

When no `--output` specified, adapt output to user needs:

| Request | Format |
|---------|--------|
| "summarize" | 1-paragraph summary |
| "analyze" | Full structured report |
| "key points" | Bullet list (5-10 items) |
| "can I implement this?" | Implementation feasibility assessment |
| "is this paper good?" | Critical evaluation |
| "explain the method" | Technical explanation with examples |

## References

- `references/deep-analysis-template.md` - Full analysis report template
- `references/implementation-template.md` - Implementation notes template
- `references/critical-template.md` - Critical evaluation template
- `references/openreview-template.md` - OpenReview analysis template
- `references/crypto-applicability-template.md` - Cryptocurrency applicability analysis template
- `references/ml-evaluation-criteria.md` - ML paper evaluation details
- `references/quant-evaluation-criteria.md` - Quant paper evaluation details
- `scripts/openreview_api.py` - OpenReview API integration module
