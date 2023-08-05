from typing import Optional, Dict, Any, Callable, List, Type

from pywood._machine import Machine
from pywood.states import BaseState


def handle_update(update,
                  states: List[Type[BaseState]],
                  current_state_getter: Callable,
                  data: Optional[Any] = None,
                  state_attrs: Optional[Dict[str, Any]] = None,
                  ):
    """

    :param update:
    :type update:

    :param states:
    :type states:

    :param current_state_getter:
    :type current_state_getter:

    :param data: (optional) данные, которые будут переданы во все обработчики
    :type data: Any

    :param state_attrs: (optional) словарь, содержащий аттрибуты, которые
    будут добавлены к экземпляру класса состояния
    :type state_attrs: Dict[str, Any]

    :return:
    """
    machine = Machine(current_state_getter=current_state_getter,
                      states=states)
    machine.process(update=update, data=data, state_attrs=state_attrs)
