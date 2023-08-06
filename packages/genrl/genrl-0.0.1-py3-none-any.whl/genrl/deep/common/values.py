from genrl.deep.common.base import BaseValue
from genrl.deep.common.utils import mlp


def _get_val_model(
    arch, val_type, state_dim, hidden, action_dim=None,
):
    if val_type == "V":
        return arch([state_dim] + list(hidden) + [1])
    elif val_type == "Qsa":
        return arch([state_dim + action_dim] + list(hidden) + [1])
    elif val_type == "Qs":
        return arch([state_dim] + list(hidden) + [action_dim])
    else:
        raise ValueError


class MlpValue(BaseValue):
    """
    MLP Value Function
    :param state_dim: (int) state dimension of environment
    :param action_dim: (int) action dimension of environment
    :param val_type: (str) type of value function.
        'V' for V(s), 'Qs' for Q(s), 'Qsa' for Q(s,a)
    :param hidden: (tuple or list) sizes of hidden layers
    """

    def __init__(self, state_dim, action_dim=None, val_type="V", hidden=(32, 32)):
        super(MlpValue, self).__init__()

        self.state_dim = state_dim
        self.action_dim = action_dim

        self.model = _get_val_model(mlp, val_type, state_dim, hidden, action_dim)


value_registry = {"mlp": MlpValue}


def get_value_from_name(name_):
    if name_ in value_registry:
        return value_registry[name_]
    raise NotImplementedError
