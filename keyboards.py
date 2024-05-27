from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from states import  User_states



def create_keyboard(*args):
    return ReplyKeyboardMarkup([[KeyboardButton(text=text) for text in args]], resize_keyboard=True)


keyboards_dict = {
    User_states.BASE: create_keyboard("Моия пари", "Отмена"),
    User_states.Createing_pari: create_keyboard("отмена")

}