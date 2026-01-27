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

### Quick Install (Recommended)

Use the automatic installer script that detects your environment and installs all skills:

```bash
# Clone the repository
git clone https://github.com/pennymax/MatrixSolv-Skills.git
cd MatrixSolv-Skills

# Run the installer
./install.sh
```

The installer will:
- Automatically detect Claude Code and/or Codex installations
- Install all skills to the appropriate directories
- Verify the installation

**Installer Options:**
```bash
./install.sh                  # Install to all detected environments
./install.sh --claude-code-only   # Install only to Claude Code
./install.sh --codex-only         # Install only to Codex
./install.sh --help               # Show help
```

### Manual Installation

Copy the desired skill directory to your skills folder:

```bash
# Clone the repository
git clone https://github.com/pennymax/MatrixSolv-Skills.git

# For Claude Code
cp -r MatrixSolv-Skills/paper-reader ~/.claude/skills/
cp -r MatrixSolv-Skills/deep-learning-training-recipe ~/.claude/skills/

# For Codex
cp -r MatrixSolv-Skills/paper-reader ~/.codex/skills/
cp -r MatrixSolv-Skills/deep-learning-training-recipe ~/.codex/skills/
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
