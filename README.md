# MatrixSolv-Skills

A collection of Claude Code skills for machine learning research, paper analysis, deep learning training, and cryptocurrency data analysis.

## Overview

This repository contains specialized skills designed to enhance Claude Code's capabilities in ML/AI research and development workflows.

## Available Skills

| Skill | Description | Use Case |
|-------|-------------|----------|
| [paper-reader](./paper-reader/) | Structured methodology for reading and analyzing ML/Quant research papers | Analyzing academic papers from arXiv, SSRN, NeurIPS, ICML, etc. |
| [deep-learning-training-recipe](./deep-learning-training-recipe/) | Systematic methodology for training neural networks based on Karpathy's 6-step recipe | Training ML models, debugging convergence issues, RL training |
| [skill-from-masters](./skill-from-masters/) | Create high-quality skills by discovering and incorporating proven methodologies from domain experts | Creating new skills based on expert frameworks and best practices |
| [binance-data](./binance-data/) | Binance public historical data query and download assistant | Downloading klines, trades, aggTrades, funding rates, metrics from Binance |
| [pdf](./pdf/) | PDF → Markdown converter using Marker with plain-text fallback | Reading PDF files efficiently in Claude Code without blowing up context window |

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
cp -r MatrixSolv-Skills/skill-from-masters ~/.claude/skills/
cp -r MatrixSolv-Skills/binance-data ~/.claude/skills/
cp -r MatrixSolv-Skills/pdf ~/.claude/skills/

# For Codex
cp -r MatrixSolv-Skills/paper-reader ~/.codex/skills/
cp -r MatrixSolv-Skills/deep-learning-training-recipe ~/.codex/skills/
cp -r MatrixSolv-Skills/skill-from-masters ~/.codex/skills/
cp -r MatrixSolv-Skills/binance-data ~/.codex/skills/
cp -r MatrixSolv-Skills/pdf ~/.codex/skills/
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

### Skill From Masters

A meta-skill that helps you create high-quality skills by discovering and incorporating proven methodologies from domain experts. Features include:

- **5-Layer Narrowing Framework**: Systematically narrow broad requests to specific, actionable skill definitions
- **3-Layer Search**: Local methodology database → Web search for experts → Deep dive on primary sources
- **Methodology Database**: Curated collection of 100+ expert frameworks across 15+ domains
- **Skill Taxonomy**: 11 skill type categories (Summary, Insight, Generation, Decision, etc.)
- **Golden Examples**: Finds exemplary outputs to define quality bar
- **Anti-Patterns**: Identifies common mistakes to encode "don't do this"

**Triggers**: "help me create a skill for X", "I want to make a skill that does Y"

**Dependency**: Works with skill-creator for final skill generation.

### Binance Data

A comprehensive skill for querying and downloading Binance public historical market data. Features include:

- **Multiple Data Types**: klines, trades, aggTrades, fundingRate, metrics
- **Market Support**: Spot, USD-M Futures (um), COIN-M Futures (cm)
- **Data Schema Reference**: Complete field definitions for all data types
- **Download Script**: Batch download with date range, multiple symbols, auto-skip existing files
- **URL Builder**: Construct correct download URLs for any data type

**Supported Data:**
| Data Type | Markets | Period |
|-----------|---------|--------|
| klines | spot, um, cm | daily, monthly |
| trades | spot, um, cm | daily, monthly |
| aggTrades | spot, um, cm | daily, monthly |
| fundingRate | um, cm | monthly only |
| metrics | um, cm | daily only |

**Triggers**: "Binance data", "download klines", "funding rate", "crypto historical data", "币安数据"

### PDF

A composable skill that converts PDF files to Markdown for efficient context-window usage. Features include:

- **Marker Conversion**: Uses [Marker](https://github.com/VikParuchuri/marker) ML-based converter preserving LaTeX formulas, tables, and heading structure
- **Automatic Fallback**: Falls back to `pdftotext` (poppler) or PyMuPDF if Marker fails
- **Caching**: Checks for existing `.md` file before converting — skip conversion on repeat reads
- **Composable**: Designed as a preprocessing step for other skills (e.g., `paper-reader`)
- **Page Selection**: Convert specific pages only for large PDFs (`--pages 0,5-10`)

**Options:**
| Flag | Effect |
|------|--------|
| `--no-images` | Skip image extraction (default for context efficiency) |
| `--pages 0,5-10` | Convert only specified pages |
| `--force` | Overwrite existing .md |
| `-o path` | Custom output path |

**Requirements**: `pip install marker-pdf` (recommended) or `poppler-utils` (fallback)

**Triggers**: PDF file references, "convert PDF to markdown", "read this PDF"

## Requirements

- Claude Code CLI
- Python 3.8+ (for some skill features)
- Additional dependencies listed in each skill's README

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT
