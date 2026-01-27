# Paper Reader

A Claude Code skill for reading and analyzing machine learning and quantitative trading research papers using structured expert methodologies.

## Features

- **Four Reading Modes**:
  - `quick` - Quick screening to decide if a paper is worth reading
  - `deep` - Full understanding of methods and contributions
  - `implement` - Implementation-focused analysis for reproducing results
  - `critical` - Critical evaluation of limitations and validity

- **Paper Type Support**:
  - Machine Learning (theory and applied)
  - Quantitative Finance
  - ML + Quant hybrid papers

- **OpenReview Integration**: Automatically fetch expert reviews from NeurIPS, ICLR, ICML, and other conferences

- **Cryptocurrency Applicability Analysis**: Evaluate how research methods can be applied to crypto markets

## Installation

Copy this skill to your Claude Code skills directory:

```bash
cp -r paper-reader ~/.claude/skills/
```

## Usage

```bash
# Basic usage
/paper-reader https://arxiv.org/abs/2410.09836

# Deep analysis with output directory
/paper-reader https://arxiv.org/abs/2410.09836 --mode deep --output ./analysis/

# Quick screening
/paper-reader paper.pdf --mode quick

# Implementation-focused analysis
/paper-reader https://arxiv.org/abs/2410.09836 --mode implement --output ./impl-notes/
```

## Output Files

| Mode | Output Files |
|------|--------------|
| `quick` | `quick-screening.md` |
| `deep` | `deep-analysis.md`, `crypto-applicability.md` |
| `implement` | `deep-analysis.md`, `implementation-notes.md`, `crypto-applicability.md` |
| `critical` | `deep-analysis.md`, `critical-evaluation.md`, `crypto-applicability.md` |

## Project Structure

```
paper-reader/
├── SKILL.md                 # Main skill definition
├── scripts/
│   └── openreview_api.py    # OpenReview API integration
└── references/
    ├── deep-analysis-template.md
    ├── implementation-template.md
    ├── critical-template.md
    ├── openreview-template.md
    ├── crypto-applicability-template.md
    ├── ml-evaluation-criteria.md
    └── quant-evaluation-criteria.md
```

## Requirements

- Claude Code CLI
- Python 3.8+ (for OpenReview API)
- `pdfplumber` (for local PDF processing)

## License

MIT
