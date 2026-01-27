# ML Paper Evaluation Criteria

Detailed criteria for evaluating machine learning research papers.

## Architecture & Method Evaluation

### Innovation Assessment

**Novelty Levels:**
- **High**: New paradigm, fundamentally different approach
- **Medium**: Novel combination of existing ideas, significant improvement
- **Low**: Incremental modification, minor tweak
- **None**: Re-implementation or application of existing method

**Questions to Ask:**
1. What is genuinely new vs borrowed from prior work?
2. Is the novelty in the problem, method, or application?
3. Would a practitioner have thought of this?

### Theoretical Soundness

**Check for:**
- Mathematical correctness of derivations
- Validity of assumptions
- Complexity analysis (time and space)
- Convergence guarantees (if claimed)

**Red Flags:**
- Hand-wavy proofs
- Unrealistic assumptions
- Missing complexity analysis
- Claims without theoretical backing

## Experimental Rigor

### Baseline Selection

**Good Baselines:**
- Recent SOTA methods (within 1-2 years)
- Classic strong baselines
- Ablated versions of proposed method
- Simple baselines (to show problem isn't trivial)

**Bad Signs:**
- Only comparing to old methods
- Missing obvious competitors
- Weak/strawman baselines
- No ablation studies

### Statistical Validity

**Required Elements:**
- Multiple random seeds (≥3, ideally 5+)
- Error bars or confidence intervals
- Statistical significance tests
- Clear reporting of variance

**Metrics to Check:**

| Domain | Standard Metrics |
|--------|------------------|
| Classification | Accuracy, F1, AUC-ROC, Precision, Recall |
| Regression | MSE, MAE, R², MAPE |
| Generation | FID, IS, BLEU, ROUGE |
| Ranking | NDCG, MRR, MAP |
| RL | Return, Success Rate, Sample Efficiency |

### Dataset Evaluation

**Dataset Quality:**
- Is it standard/well-known?
- Is it appropriate for the task?
- Is it large enough?
- Are there known issues/biases?

**Split Validity:**
- No data leakage between splits
- Temporal splits for time-series
- Stratified splits for imbalanced data
- Cross-validation where appropriate

## Reproducibility Checklist

### Code & Data

| Element | Ideal | Acceptable | Problematic |
|---------|-------|------------|-------------|
| Code | Public repo, documented | Available on request | Not available |
| Data | Public, preprocessed | Public raw | Private/proprietary |
| Pretrained models | Available | Training code provided | Neither |

### Implementation Details

**Must be specified:**
- [ ] Model architecture (all layers, dimensions)
- [ ] Optimizer and learning rate schedule
- [ ] Batch size and training epochs
- [ ] Regularization (dropout, weight decay)
- [ ] Data augmentation
- [ ] Hardware used
- [ ] Training time
- [ ] Random seed handling

### Hyperparameter Reporting

**Questions:**
- How were hyperparameters selected?
- Was there a validation set for tuning?
- Are all hyperparameters reported?
- Is there sensitivity analysis?

## Common ML Paper Issues

### Evaluation Pitfalls

1. **Test Set Contamination**
   - Tuning on test set
   - Information leakage in preprocessing

2. **Unfair Comparisons**
   - Different compute budgets
   - Different hyperparameter tuning effort
   - Different data preprocessing

3. **Cherry-Picking**
   - Reporting best run only
   - Selective metric reporting
   - Favorable dataset selection

### Methodology Issues

1. **Overclaiming**
   - "State-of-the-art" without proper comparison
   - Generalizing from limited experiments
   - Causal claims from correlational evidence

2. **Missing Analysis**
   - No failure case analysis
   - No computational cost comparison
   - No scalability discussion

## Quality Scoring Rubric

### Overall Paper Quality

| Score | Description |
|-------|-------------|
| 5 | Exceptional - Novel, rigorous, reproducible, significant impact |
| 4 | Strong - Good novelty, solid experiments, minor issues |
| 3 | Acceptable - Some novelty, adequate experiments, notable gaps |
| 2 | Weak - Limited novelty, flawed experiments, major issues |
| 1 | Poor - No novelty, unreliable results, fundamental problems |

### Component Scores

| Component | Weight | Criteria |
|-----------|--------|----------|
| Novelty | 25% | New ideas, not incremental |
| Technical Quality | 25% | Sound methodology, correct math |
| Experiments | 30% | Rigorous, fair, comprehensive |
| Clarity | 10% | Well-written, reproducible |
| Significance | 10% | Impact on field, practical value |
