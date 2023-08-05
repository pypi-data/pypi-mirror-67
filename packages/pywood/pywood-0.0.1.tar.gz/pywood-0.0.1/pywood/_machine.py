"""Класс определяющий основную функциональность."""
from __future__ import annotations

from typing import List, Type, Callable, TypeVar, Union

from pywood.exceptions import StateDoesNotExistError
from pywood.exceptions import StateError
from pywood.states import BaseState

Update = TypeVar('Update')


class Machine:
    """Класс определяющий работу с состояниями."""

    def __init__(self,
                 *,
                 current_state_getter: Callable,
                 states: List[Type[BaseState]]):
        """Проинициализировать класс определяющий работу с состояниями.

        :param current_state_getter: функция, принимающая Update и \
        возвращающая либо строку, которая является названием текущего \
        состояния, либо сам класс текущего состояния
        :type current_state_getter: функция

        :param states: список состояний чата
        :type states: список из классов унаследованных от State
        """
        self._current_state_getter = current_state_getter
        self._states = states

    def _get_state_from_state_name(self, state_name: str) -> Type[BaseState]:
        """Получить класс состояния из названия класса состояния."""
        for state in self._states:
            if state.__name__ == state_name:
                return state
        raise StateDoesNotExistError

    def _get_current_state(self, state: Union[str, Type[BaseState]]):
        """Получить текущее состояние"""
        if isinstance(state, str):
            return self._get_state_from_state_name(state)
        elif issubclass(state, BaseState):
            return state
        else:
            raise StateError("Вы должны передать строку с названием класса "
                             "состояния или сам класс состояния")

    @staticmethod
    def _add_attrs(obj, attrs):
        for key, value in attrs.items():
            setattr(obj, key, value)

    def process(self,
                update: Update,
                state_attrs=None,
                data=None,
                ):
        """Обработать объект типа Update."""
        state_cls = self._get_current_state(self._current_state_getter(update))
        state = state_cls()
        if state_attrs:
            Machine._add_attrs(state, state_attrs)
        state._traverse_handlers(update, data)
