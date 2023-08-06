import pytest
import numpy as np
import gym

from genrl import SARSA, QLearning
from genrl.classical import Trainer


class TestTrainer:
    def test_trainer(self):
        env = gym.make("FrozenLake-v0")
        agent = QLearning(env)
        trainer = Trainer(
            agent, env, mode="dyna", model="tabular", n_episodes=50, start_steps=0
        )
        ep_rs = trainer.train()
