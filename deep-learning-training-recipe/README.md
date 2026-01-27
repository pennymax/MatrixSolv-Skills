# Deep Learning Training Recipe

A systematic methodology for training neural networks based on **Andrej Karpathy's 6-step recipe**, extended for reinforcement learning and quantitative strategy development.

## Overview

This is a Claude Code skill that provides structured guidance for ML practitioners. Neural network training fails silently - unlike traditional software where bugs throw exceptions, misconfigurations in ML simply produce worse results. This skill helps you build from simple to complex while validating at each step.

## The 6-Step Recipe

1. **Become One with the Data** - Deeply understand your data before writing model code
2. **Set Up End-to-End Training Skeleton** - Start simple, verify correctness
3. **Overfit** - Ensure model has enough capacity
4. **Regularize** - Trade training accuracy for validation accuracy
5. **Tune Hyperparameters** - Systematic exploration
6. **Squeeze Out the Juice** - Final optimizations

## Contents

- `SKILL.md` - Core training methodology with checklists
- `references/rl-debugging.md` - RL-specific debugging guide (based on Andy Jones' methodology)
- `references/quant-pitfalls.md` - Quantitative strategy development pitfalls

## Usage

This skill is designed for use with [Claude Code](https://github.com/anthropics/claude-code). It triggers automatically when you:

- Start a new ML/DL project
- Debug a model that won't converge
- Train RL agents
- Develop quantitative trading strategies
- Review ML training code

## Sources

- [Andrej Karpathy - A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/)
- [Andy Jones - Debugging Reinforcement Learning Systems](https://andyljones.com/posts/rl-debugging.html)
- [Stable Baselines3 - RL Tips and Tricks](https://stable-baselines3.readthedocs.io/en/master/guide/rl_tips.html)
- Marcos López de Prado - "Advances in Financial Machine Learning"

## License

MIT
