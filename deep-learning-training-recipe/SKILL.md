---
name: deep-learning-training-recipe
description: |
  Systematic methodology for training neural networks based on Andrej Karpathy's 6-step recipe.
  Covers deep learning, reinforcement learning, and quantitative strategy development.

  Use this skill when:
  (1) Starting a new ML/DL project from scratch
  (2) Debugging a model that won't converge or performs poorly
  (3) Optimizing model performance systematically
  (4) Training RL agents or developing quantitative trading strategies
  (5) Reviewing ML training code for best practices

  Triggers: "train model", "debug neural network", "model not converging", "improve accuracy",
  "RL training", "quantitative strategy", "hyperparameter tuning", "overfitting"
---

# Deep Learning Training Recipe

A systematic methodology for training neural networks, based on Andrej Karpathy's proven 6-step approach, extended for reinforcement learning and quantitative strategy development.

## Core Philosophy

Neural network training fails silently. Unlike traditional software where bugs throw exceptions, misconfigurations in ML simply produce worse results. Success requires patience, attention to detail, and building from simple to complex while validating at each step.

## The 6-Step Training Recipe

### Step 1: Become One with the Data

Before writing any model code, deeply understand the data.

**Actions:**
- Inspect thousands of examples manually
- Look for duplicates, corrupted samples, class imbalances, and biases
- Understand what features matter (local vs global, spatial position, temporal patterns)
- Write visualization code to explore distributions and outliers
- For time series: check for lookahead bias and data leakage

**Checklist:**
- [ ] Visualized representative samples from each class/category
- [ ] Identified and handled missing values, outliers, corrupted data
- [ ] Understood feature distributions and correlations
- [ ] Verified no data leakage between train/val/test splits
- [ ] Documented data quality issues and preprocessing decisions

### Step 2: Set Up End-to-End Training Skeleton

Start with the simplest possible model and verify correctness before adding complexity.

**Actions:**
- Fix random seed for reproducibility
- Disable data augmentation initially
- Start with a linear classifier or tiny network
- Verify loss starts at correct value (e.g., `-log(1/n_classes)` for softmax)
- Initialize final layer weights correctly (small or zero for regression)
- Establish human baseline performance
- **Critical: Overfit a single batch first** - if the model can't memorize 1 batch, something is broken

**Verification Tests:**
```python
# 1. Verify initial loss
# For n-class classification with softmax: loss ≈ -log(1/n)
expected_loss = -np.log(1/num_classes)
assert abs(initial_loss - expected_loss) < 0.1

# 2. Overfit single batch test
for _ in range(1000):
    loss = train_step(single_batch)
assert loss < 0.01  # Should reach near-zero loss

# 3. Input-independent baseline
# Model with zeroed/random inputs should perform at chance level
```

**Checklist:**
- [ ] Random seed fixed for reproducibility
- [ ] Initial loss matches theoretical expectation
- [ ] Model can overfit a single batch to near-zero loss
- [ ] Data flows correctly through the pipeline (visualize just before model input)
- [ ] Gradients flow to all parameters (no dead layers)

### Step 3: Overfit

Get a model large enough to fit the training set before worrying about generalization.

**Actions:**
- Don't be a hero - copy architectures from related papers (ResNet-50, Transformer, etc.)
- Use Adam optimizer with lr=3e-4 as starting point
- Add complexity one element at a time
- Disable learning rate decay initially
- If model can't overfit training set, it lacks capacity or has bugs

**Guidelines:**
- Architecture: Start with proven architectures, not custom designs
- Optimizer: Adam 3e-4 → SGD with momentum for fine-tuning
- Batch size: Larger is generally better for stability (32-256 typical)
- Epochs: Train until training loss plateaus

**Checklist:**
- [ ] Using proven architecture appropriate for the task
- [ ] Training loss decreasing consistently
- [ ] Model can achieve near-zero training loss (overfitting is the goal here)
- [ ] No NaN/Inf in losses or gradients

### Step 4: Regularize

Trade training accuracy for validation accuracy through regularization.

**Priority Order (most to least effective):**
1. **Get more real data** - Always the best option
2. **Data augmentation** - Domain-appropriate transforms
3. **Pretrained models** - Transfer learning when available
4. **Reduce input dimensionality** - Remove irrelevant features
5. **Decrease model size** - Fewer parameters
6. **Reduce batch size** - More gradient noise acts as regularization
7. **Dropout** - Use sparingly with batch norm (0.1-0.3)
8. **Weight decay** - L2 regularization (1e-4 to 1e-2)
9. **Early stopping** - Stop when validation loss increases
10. **Label smoothing** - For classification (0.1 typical)

**Checklist:**
- [ ] Validation loss tracked separately from training loss
- [ ] Gap between train/val loss is reasonable (<2x)
- [ ] Tried at least 3 regularization techniques
- [ ] Early stopping implemented with patience

### Step 5: Tune Hyperparameters

Systematically explore the hyperparameter space.

**Actions:**
- Use random search over grid search (more efficient)
- Consider Bayesian optimization (Optuna, Ray Tune)
- Focus on: learning rate, batch size, model size, regularization strength
- Log everything - you'll need to analyze results

**Key Hyperparameters by Priority:**
1. Learning rate (most important)
2. Batch size
3. Number of layers / hidden units
4. Regularization strength (dropout, weight decay)
5. Optimizer-specific params (momentum, beta values)

**Checklist:**
- [ ] Learning rate sweep performed (1e-5 to 1e-1, log scale)
- [ ] Multiple random seeds tested for best config
- [ ] Results logged and visualized
- [ ] Best config validated on held-out test set

### Step 6: Squeeze Out the Juice

Final optimizations for production.

**Actions:**
- Model ensembles (typically +2% accuracy)
- Knowledge distillation if compute-limited
- Train longer than intuition suggests
- Test time augmentation
- Stochastic weight averaging

**Checklist:**
- [ ] Ensemble of top models tested
- [ ] Final model evaluated on completely held-out test set
- [ ] Results documented with confidence intervals
- [ ] Model artifacts saved (weights, config, preprocessing)

---

## Reinforcement Learning Extensions

RL training has unique challenges. See [references/rl-debugging.md](references/rl-debugging.md) for detailed guidance.

**Key Differences from Supervised Learning:**
- Feedback is delayed and noisy
- Bugs spread throughout the system (poisoned replay buffer)
- High run-to-run variance is normal

**Critical RL Practices:**

1. **Scale rewards to [-1, +1] or [-10, +10]** - Hand-tune, don't use adaptive schemes initially

2. **Use large batch sizes:**
   - Simple tasks (Pong): ~1k
   - Medium tasks (Atari): ~10k
   - Complex tasks (Dota): ~100k+

3. **Start with small networks** - 4 layers of 256 units often sufficient

4. **Avoid pixel observations initially** - Use state-based envs first

5. **Use probe environments** to verify components:
   ```
   Probe 1: One action, zero obs, +1 reward → tests value network
   Probe 2: One action, random obs, obs-dependent reward → tests backprop
   Probe 3: Two actions, action-dependent reward → tests policy
   ```

6. **Assume you have a bug** - Bugs are far more common than architecture issues

7. **Work from reference implementations** - cleanrl, stable-baselines3, spinning-up

---

## Quantitative Strategy Extensions

ML for trading has additional pitfalls. See [references/quant-pitfalls.md](references/quant-pitfalls.md) for details.

**Critical Practices:**

1. **Prevent data leakage:**
   - No future information in features
   - Proper train/val/test time splits (not random)
   - Account for publication lag in fundamental data

2. **Use walk-forward validation:**
   ```
   Train: [2010-2015] → Val: [2016] → Test: [2017]
   Train: [2011-2016] → Val: [2017] → Test: [2018]
   ...
   ```

3. **Account for transaction costs:**
   - Include slippage, commissions, market impact
   - Strategies that work without costs often fail with them

4. **Beware of overfitting:**
   - More parameters + more backtests = more overfitting
   - Use combinatorial purged cross-validation (CPCV)
   - Deflated Sharpe ratio for multiple testing

5. **Test on multiple regimes:**
   - Bull markets, bear markets, high volatility, low volatility
   - Strategy should be robust across regimes

---

## Common Failure Modes

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Loss is NaN | Learning rate too high, bad initialization | Reduce LR, check init |
| Loss doesn't decrease | LR too low, bug in loss/data | Increase LR, verify single-batch overfit |
| Train loss good, val loss bad | Overfitting | Add regularization, get more data |
| High variance across runs | Unstable training | Larger batch, lower LR, gradient clipping |
| RL reward flat | Reward scale wrong, exploration issue | Scale rewards, check entropy |

---

## Quick Reference

**Starting Point Config:**
```yaml
optimizer: Adam
learning_rate: 3e-4
batch_size: 64
weight_decay: 1e-4
dropout: 0.1
epochs: 100
early_stopping_patience: 10
```

**Debugging Priority:**
1. Verify data pipeline (visualize inputs)
2. Check loss computation
3. Verify gradients flow (no dead layers)
4. Test single-batch overfitting
5. Then worry about architecture/hyperparameters

## Resources

- [references/rl-debugging.md](references/rl-debugging.md) - Detailed RL debugging guide
- [references/quant-pitfalls.md](references/quant-pitfalls.md) - Quantitative strategy pitfalls
