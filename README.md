# MatrixSolv-Skills

A collection of Claude Code skills for machine learning research, paper analysis, and deep learning training.

## Overview

This repository contains specialized skills designed to enhance Claude Code's capabilities in ML/AI research and development workflows.

## Available Skills

| Skill | Description | Use Case |
|-------|-------------|----------|
| [paper-reader](./paper-reader/) | Structured methodology for reading and analyzing ML/Quant research papers | Analyzing academic papers from arXiv, SSRN, NeurIPS, ICML, etc. |
| [deep-learning-training-recipe](./deep-learning-training-recipe/) | Systematic methodology for training neural networks based on Karpathy's 6-step recipe | Training ML models, debugging convergence issues, RL training |

## Installation

Copy the desired skill directory to your Claude Code skills folder:

```bash
# Clone the repository
git clone https://github.com/pennymax/MatrixSolv-Skills.git

# Copy a specific skill
cp -r MatrixSolv-Skills/paper-reader ~/.claude/skills/
cp -r MatrixSolv-Skills/deep-learning-training-recipe ~/.claude/skills/
```

## Skill Details

### Paper Reader

A comprehensive skill for reading and analyzing machine learning and quantitative trading research papers. Features include:

- **Four Reading Modes**: Quick screening, deep analysis, implementation-focused, and critical evaluation
- **Paper Type Support**: ML theory, ML applied, quantitative finance, and hybrid papers
- **OpenReview Integration**: Automatically fetch expert reviews from major ML conferences
- **Cryptocurrency Applicability Analysis**: Evaluate research methods for crypto market applications

**Triggers**: "analyze this paper", "summarize this research", "help me understand this ML paper"

### Deep Learning Training Recipe

A systematic methodology for training neural networks, based on Andrej Karpathy's proven 6-step approach:

1. **Become One with the Data** - Deeply understand your data before writing model code
2. **Set Up End-to-End Training Skeleton** - Start simple, verify correctness
3. **Overfit** - Ensure model has enough capacity
4. **Regularize** - Trade training accuracy for validation accuracy
5. **Tune Hyperparameters** - Systematic exploration
6. **Squeeze Out the Juice** - Final optimizations

Extended for reinforcement learning and quantitative strategy development.

**Triggers**: "train model", "debug neural network", "model not converging", "RL training"

## Requirements

- Claude Code CLI
- Python 3.8+ (for some skill features)
- Additional dependencies listed in each skill's README

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT
