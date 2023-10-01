from aiogram.dispatcher.filters.state import State, StatesGroup


class Main(StatesGroup):
    start = State()
    form_chosen = State()
