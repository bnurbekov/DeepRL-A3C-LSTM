### Environment

I was not able to make ppaquette_gym_doom work on my machine. Thus, in the interests of time I implemented lightweight gym-like interface for Vizdoom (which is slightly different from OpenAI Gym's interface).

### Model

A2C (Advantage Actor - Critic) + LSTM.

Main point of reference: https://arxiv.org/pdf/1609.05521v1.pdf

### Further improvements

1) Implement unsupervised auxilary tasks to mitigate the reward sparseness in the environment (https://arxiv.org/abs/1611.05397).
2) Apply generalized advantage estimation.
3) Try out TRPO and Natural Gradient techniques.
4) Learning from demonstration for pre-training.