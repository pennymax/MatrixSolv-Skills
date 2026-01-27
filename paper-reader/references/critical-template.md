# Critical Evaluation Template

Use this template for `critical` mode to assess paper validity and limitations.

---

## Critical Evaluation: [Paper Title]

**Overall Assessment**: [Strong Accept / Weak Accept / Borderline / Weak Reject / Strong Reject]
**Confidence**: [High / Medium / Low]

---

### 1. Claims vs Evidence

**Main Claims:**

| Claim | Evidence Provided | Strength |
|-------|-------------------|----------|
| [Claim 1] | [What supports it] | Strong / Moderate / Weak |
| [Claim 2] | [What supports it] | Strong / Moderate / Weak |
| [Claim 3] | [What supports it] | Strong / Moderate / Weak |

**Unsupported Claims:**
- [Claim made without sufficient evidence]

**Overclaims:**
- [Where authors overstate their results]

---

### 2. Methodology Critique

#### For ML Papers

**Experimental Design:**

| Criterion | Status | Issue |
|-----------|--------|-------|
| Fair baselines | [Yes/No/Partial] | [Details] |
| Appropriate metrics | [Yes/No/Partial] | [Details] |
| Statistical significance | [Yes/No/Partial] | [Details] |
| Multiple seeds | [Yes/No/Partial] | [Details] |
| Error bars/CI | [Yes/No/Partial] | [Details] |

**Potential Issues:**
- [ ] Cherry-picked results
- [ ] Unfair baseline comparison (old/weak baselines)
- [ ] Hyperparameter tuning on test set
- [ ] Missing important baselines
- [ ] Inappropriate evaluation metrics
- [ ] Insufficient ablation studies

**Reproducibility Assessment:**

| Element | Provided | Quality |
|---------|----------|---------|
| Code | [Yes/No/Partial] | [Usable/Incomplete/Missing] |
| Data | [Yes/No/Partial] | [Public/Private/Synthetic] |
| Hyperparameters | [Yes/No/Partial] | [Complete/Partial/Missing] |
| Training details | [Yes/No/Partial] | [Complete/Partial/Missing] |
| Compute specs | [Yes/No/Partial] | [Complete/Partial/Missing] |

#### For Quant Papers

**Backtest Validity:**

| Criterion | Status | Severity |
|-----------|--------|----------|
| Look-ahead bias | [Clean/Suspect/Present] | [Critical/Major/Minor] |
| Survivorship bias | [Addressed/Ignored] | [Critical/Major/Minor] |
| Transaction costs | [Realistic/Understated/Ignored] | [Critical/Major/Minor] |
| Slippage | [Modeled/Ignored] | [Critical/Major/Minor] |
| Market impact | [Considered/Ignored] | [Critical/Major/Minor] |

**Statistical Concerns:**

| Issue | Status | Notes |
|-------|--------|-------|
| Multiple testing | [Corrected/Uncorrected] | [Bonferroni/FDR/None] |
| Data snooping | [Low/Medium/High risk] | [Details] |
| Overfitting | [Low/Medium/High risk] | [Details] |
| Sample size | [Adequate/Marginal/Insufficient] | [N = X] |

**Out-of-Sample Testing:**
- In-sample period: [Dates]
- Out-of-sample period: [Dates]
- Walk-forward validation: [Yes/No]
- Regime robustness: [Tested/Not tested]

---

### 3. Red Flags

**Serious Concerns:**
- [ ] Results too good to be true
- [ ] Missing critical details
- [ ] Inconsistent numbers across tables
- [ ] No comparison with obvious baselines
- [ ] Evaluation on non-standard/private data only
- [ ] Claims not supported by experiments

**Yellow Flags:**
- [ ] Limited ablation studies
- [ ] Single dataset evaluation
- [ ] No failure case analysis
- [ ] Vague methodology description
- [ ] Missing error analysis

---

### 4. Novelty Assessment

**Technical Novelty:**

| Component | Novelty Level | Prior Work |
|-----------|---------------|------------|
| [Component 1] | [High/Medium/Low/None] | [Citation] |
| [Component 2] | [High/Medium/Low/None] | [Citation] |

**Contribution Type:**
- [ ] New problem formulation
- [ ] New method/algorithm
- [ ] New theoretical insight
- [ ] New benchmark/dataset
- [ ] Engineering contribution
- [ ] Empirical study

**Incremental vs Significant:**
[Assessment of whether this is incremental improvement or significant advance]

---

### 5. Practical Applicability

**For Production Use:**

| Factor | Assessment | Blocker? |
|--------|------------|----------|
| Computational cost | [Feasible/Expensive/Prohibitive] | [Yes/No] |
| Data requirements | [Available/Obtainable/Unavailable] | [Yes/No] |
| Latency | [Acceptable/Marginal/Too slow] | [Yes/No] |
| Maintenance complexity | [Low/Medium/High] | [Yes/No] |

**Hidden Costs:**
- [Cost not mentioned in paper]
- [Practical challenge not addressed]

---

### 6. What's Missing

**Experiments That Should Have Been Done:**
1. [Missing experiment 1]
2. [Missing experiment 2]

**Questions Left Unanswered:**
1. [Question 1]
2. [Question 2]

**Comparisons That Should Have Been Made:**
1. [Missing baseline/comparison]

---

### 7. Summary Verdict

**Strengths:**
1. [Key strength 1]
2. [Key strength 2]

**Weaknesses:**
1. [Key weakness 1]
2. [Key weakness 2]

**Bottom Line:**
> [2-3 sentence summary of whether to trust/use this paper and why]

**Recommendation:**
- [ ] Trust and implement
- [ ] Implement with caution (verify claims first)
- [ ] Wait for independent replication
- [ ] Interesting idea, flawed execution
- [ ] Skip - fundamental issues

---

### 8. Follow-up Questions for Authors

If you could ask the authors:
1. [Question about methodology]
2. [Question about results]
3. [Question about applicability]
