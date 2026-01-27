# Implementation Notes Template

Use this template for `implement` mode when the goal is to reproduce or implement the paper's method.

---

## Implementation Notes: [Paper Title]

**Target**: Reproduce [specific result/method]
**Estimated Effort**: [X days/weeks]
**Difficulty**: [Easy / Medium / Hard / Expert]

---

### 0. Code Discovery Results

> **IMPORTANT**: Always complete this section FIRST before implementing anything.

**Links Found in Paper:**

| Source | URL | Type |
|--------|-----|------|
| Paper text/footnote | [URL] | Official / Project Page |
| Code Availability section | [URL] | Official |
| Supplementary materials | [URL] | Official |
| Author's homepage | [URL] | Official |

**GitHub Search Results:**

| Repository | Stars | Last Update | Official? | License |
|------------|-------|-------------|-----------|---------|
| [owner/repo](URL) | ⭐ X | YYYY-MM | Yes/No | MIT/Apache/etc |
| [owner/repo](URL) | ⭐ X | YYYY-MM | Yes/No | MIT/Apache/etc |

**Code Quality Assessment:**

| Repository | Docs | Tests | Examples | Dependencies | Verdict |
|------------|------|-------|----------|--------------|---------|
| [repo 1] | ✅/❌ | ✅/❌ | ✅/❌ | Compatible/Issues | ⭐⭐⭐ |
| [repo 2] | ✅/❌ | ✅/❌ | ✅/❌ | Compatible/Issues | ⭐⭐ |

**Decision:**

- [ ] **USE EXISTING**: Found official/high-quality implementation → [repo URL]
- [ ] **FORK & ADAPT**: Found code but needs updates → [repo URL]
- [ ] **IMPLEMENT FROM SCRATCH**: No suitable code found

**If Using Existing Code:**

```bash
# Clone command
git clone [repo URL]
cd [repo name]

# Setup (from their README)
pip install -r requirements.txt  # or conda env create -f environment.yml

# Verify it works
python [example script]
```

**Adaptation Notes:**
- [ ] Need to modify [component] for our use case
- [ ] Need to update dependencies: [list]
- [ ] Need to add [feature] not in original

---

> **If implementing from scratch, continue with sections below. Otherwise, skip to Section 7 (Validation Strategy).**

---

### 1. Algorithm Overview

**Main Algorithm:**

```
Algorithm: [Name]
Input: [What it takes]
Output: [What it produces]

1. [Step 1]
2. [Step 2]
3. [Step 3]
   3.1 [Sub-step]
   3.2 [Sub-step]
4. [Step 4]

Return: [Output]
```

**Auxiliary Algorithms:**

| Algorithm | Purpose | Complexity |
|-----------|---------|------------|
| [Name 1] | [What it does] | O(n) |
| [Name 2] | [What it does] | O(n log n) |

---

### 2. Architecture Details (ML Papers)

**Model Architecture:**

```
Layer 1: [Type] - Input: [dim] → Output: [dim]
    - Activation: [function]
    - Normalization: [type]

Layer 2: [Type] - Input: [dim] → Output: [dim]
    - ...

Output Layer: [Type] - Input: [dim] → Output: [dim]
```

**Key Modules:**

| Module | Implementation | Notes |
|--------|----------------|-------|
| [Attention] | [Standard / Custom] | [Special considerations] |
| [Encoder] | [Architecture] | [Details] |

---

### 3. Hyperparameters

**Training Hyperparameters:**

| Parameter | Value | Sensitivity | Notes |
|-----------|-------|-------------|-------|
| Learning Rate | X | High | [Schedule if any] |
| Batch Size | X | Medium | [Memory constraints] |
| Epochs | X | Low | [Early stopping criteria] |
| Optimizer | [Name] | - | [Specific settings] |
| Weight Decay | X | Medium | - |

**Model Hyperparameters:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Hidden Dim | X | - |
| Num Layers | X | - |
| Dropout | X | - |

**Hyperparameters NOT Specified in Paper:**
- [Parameter 1] - Need to tune
- [Parameter 2] - Assume default

---

### 4. Data Requirements

**Dataset Specifications:**

| Dataset | Source | Size | Format |
|---------|--------|------|--------|
| [Name] | [URL/Source] | [N samples] | [CSV/Parquet/etc] |

**Preprocessing Pipeline:**

```python
# Step 1: Load data
data = load_data(path)

# Step 2: Clean
data = remove_nulls(data)
data = handle_outliers(data, method='winsorize', limits=(0.01, 0.99))

# Step 3: Feature engineering
features = create_features(data)
# - [Feature 1]: [How computed]
# - [Feature 2]: [How computed]

# Step 4: Normalize
features = normalize(features, method='z-score')

# Step 5: Split
train, val, test = split(features, ratios=[0.7, 0.15, 0.15])
```

**Data Splits:**
- Training: [Date range or %]
- Validation: [Date range or %]
- Test: [Date range or %]

---

### 5. Implementation Checklist

**Dependencies:**

```
# Core
python>=3.8
pytorch>=2.0  # or tensorflow>=2.x
numpy>=1.20

# Domain-specific
[library1]>=X.Y
[library2]>=X.Y

# Optional
wandb  # for logging
```

**Compute Requirements:**

| Resource | Minimum | Recommended | Paper Used |
|----------|---------|-------------|------------|
| GPU | [Type] | [Type] | [Type] |
| VRAM | X GB | X GB | X GB |
| RAM | X GB | X GB | - |
| Storage | X GB | X GB | - |

**Estimated Training Time:**
- Paper reported: [X hours on Y GPU]
- Our estimate: [X hours on Y GPU]

---

### 6. Known Pitfalls

**From Paper:**
1. [Pitfall mentioned by authors]
2. [Sensitivity to X]

**From Experience/Community:**
1. [Common implementation mistake]
2. [Numerical stability issue]
3. [Data leakage risk]

**Debugging Tips:**
- If [symptom], check [cause]
- Monitor [metric] during training
- Sanity check: [simple test to verify correctness]

---

### 7. Validation Strategy

**Reproduce Paper Results:**

| Metric | Paper Reports | Our Target | Acceptable Range |
|--------|---------------|------------|------------------|
| [Metric 1] | X | X | X ± Y |
| [Metric 2] | X | X | X ± Y |

**Sanity Checks:**
- [ ] Overfit on small batch (loss → 0)
- [ ] Gradient flow (no vanishing/exploding)
- [ ] Output distribution matches expected
- [ ] Baseline reproduces known results

---

### 8. Code Structure

```
project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── loaders.py
├── models/
│   ├── [model_name].py
│   └── layers.py
├── training/
│   ├── train.py
│   ├── evaluate.py
│   └── losses.py
├── configs/
│   └── default.yaml
├── scripts/
│   ├── preprocess.py
│   └── run_experiment.py
└── notebooks/
    └── analysis.ipynb
```

---

### 9. Quick Start Code

```python
# Minimal working example

import torch
from model import PaperModel
from data import load_dataset

# Config
config = {
    'hidden_dim': 256,
    'num_layers': 4,
    'learning_rate': 1e-4,
}

# Data
train_loader, val_loader = load_dataset('path/to/data')

# Model
model = PaperModel(**config)
optimizer = torch.optim.Adam(model.parameters(), lr=config['learning_rate'])

# Training loop
for epoch in range(100):
    for batch in train_loader:
        loss = model.training_step(batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    # Validation
    val_metric = evaluate(model, val_loader)
    print(f"Epoch {epoch}: {val_metric}")
```

---

### 10. Next Steps

**Immediate:**
1. [ ] Set up environment
2. [ ] Download/prepare data
3. [ ] Implement core model

**After Basic Implementation:**
1. [ ] Reproduce main result
2. [ ] Run ablations
3. [ ] Adapt for our use case
