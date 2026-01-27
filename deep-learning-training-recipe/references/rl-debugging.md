# Reinforcement Learning Debugging Guide

Based on Andy Jones' RL debugging methodology and Stable Baselines best practices.

## Why RL Debugging Is Hard

**Poor Feedback:**
- Errors aren't local - bugs spread throughout the system quickly
- Performance is noisy - weak correlation between implementation quality and reward
- High run-to-run variability makes bug detection difficult

**Difficult Simplification:**
- Few narrow interfaces between components
- Large stateful components (environment state, network weights, replay buffer)
- Few reliable abstractions

## Core Debugging Strategies

1. **Design reliable tests** - Tests should clearly pass or fail, not be pseudorandom
2. **Design fast tests** - Iteration should take seconds, not days
3. **Localize errors** - Find tests that cut your system in half
4. **Be Bayesian** - Prioritize areas likely to contain bugs AND where bugs are easily spotted
5. **Pursue anomalies** - Chase weird behavior immediately; don't hope it goes away

## Probe Environments

Use these progressive test environments to isolate specific functionality:

| Probe | Setup | Tests |
|-------|-------|-------|
| 1 | One action, zero obs, one timestep, +1 reward | Value network isolation |
| 2 | One action, random obs, one timestep, obs-dependent reward | Backpropagation |
| 3 | One action, zero-then-one obs, two timesteps, +1 at end | Reward discounting |
| 4 | Two actions, zero obs, one timestep, action-dependent reward | Policy gradient |
| 5 | Two actions, random obs, one timestep, action-and-obs dependent reward | Full interaction |

## Common Bug Locations

- Reward discounting around episode resets
- Advantage calculations around resets
- Buffering/batching - pairing wrong rewards with wrong observations
- Observation normalization applied inconsistently
- Action space bounds not enforced

## Essential Logging Metrics

### Policy Metrics
- **Relative policy entropy**: Should start near 1, fall rapidly, then flatten
- **KL divergence**: Between old and new policy; should be small but positive

### Value Metrics
- **Residual variance**: `var(target - predicted) / var(target)` - should decrease
- **Terminal correlation**: Value in final state vs final reward
- **Value target distribution**: Should be in range [-10, +10], ideally [-3, +3]

### Training Metrics
- **Advantage distribution**: Should be [-10, +10] and approximately mean-zero
- **Episode length distribution**: Detect degenerate behavior (always dying immediately, etc.)
- **Gradient statistics**: Abs-max and mean-square of gradients

## Algorithm Selection Guide

### Discrete Actions
- **Single process**: DQN with extensions (double DQN, prioritized replay)
- **Multiprocessed**: PPO or A2C

### Continuous Actions
- **Single process**: SAC, TD3, or TQC (state-of-the-art)
- **Multiprocessed**: PPO, TRPO, or A2C
- **Critical**: Normalization is essential for continuous action algorithms

### Goal-Conditioned
- Use HER combined with SAC/TD3/DDPG/DQN depending on action space

## Validation Progression

Test on environments with gradual difficulty:

**Continuous actions:**
1. Pendulum (easy)
2. HalfCheetah (medium)
3. BipedalWalkerHardcore (hard)

**Discrete actions:**
1. CartPole-v1
2. LunarLander
3. Pong
4. Other Atari games

## Reference Implementations

Recommended codebases to work from:
- **cleanrl** - Single-file implementations, easy to understand
- **stable-baselines3** - Production-ready, well-tested
- **spinning-up** - Educational, well-documented
- **OpenSpiel** - Multi-agent and game theory

## Common Fixes Checklist

- [ ] Reward scale in [-1, +1] to [-10, +10] range
- [ ] Batch size appropriate for task complexity
- [ ] Network size not too large (start small)
- [ ] Observation normalization applied (VecNormalize for PPO/A2C)
- [ ] Action space normalized to [-1, 1] for continuous
- [ ] Multiple seeds tested (at least 3-5)
- [ ] Reference implementation consulted for hyperparameters
