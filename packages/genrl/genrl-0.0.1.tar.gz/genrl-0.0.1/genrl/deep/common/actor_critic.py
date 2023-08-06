from genrl.deep.common.base import BaseActorCritic
from genrl.deep.common.policies import MlpPolicy
from genrl.deep.common.values import MlpValue


class MlpActorCritic(BaseActorCritic):
    """
    MLP Actor Critic
    :param state_dim: (int) state dimension of environment
    :param action_dim: (int) action dimension of environment
    :param hidden: (tuple or list) sizes of hidden layers
    :param val_type: (str) type of value function.
        'V' for V(s), 'Qs' for Q(s), 'Qsa' for Q(s,a)
    :param disc: (bool) discrete action space?
    """

    def __init__(
        self,
        state_dim,
        action_dim,
        hidden=(32, 32),
        val_type="V",
        disc=True,
        *args,
        **kwargs
    ):
        super(MlpActorCritic, self).__init__(disc)

        self.actor = MlpPolicy(state_dim, action_dim, hidden, disc, **kwargs)
        self.critic = MlpValue(state_dim, action_dim, val_type, hidden)


actor_critic_registry = {"mlp": MlpActorCritic}


def get_actor_critic_from_name(name_):
    if name_ in actor_critic_registry:
        return actor_critic_registry[name_]
    raise NotImplementedError
