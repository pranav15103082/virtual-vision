from Speechmanager.speech_manager import speech as sp
from pynput.keyboard import Key,Controller
from Speechmanager.TTS import tts
from Write import writing
keyboard = Controller()

class wordlib:
    #functionalty of mswordcommands
    @staticmethod
    def write():
        writing.write()
    @staticmethod
    def read():
        wordlib.select_all()
        with keyboard.pressed(Key.alt):
            keyboard.press('s')
            keyboard.release('s')
            wordlib.deselect()

    @staticmethod
    def save():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
            #todo
    @staticmethod
    def select_all():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('a')
            keyboard.release('a')
    @staticmethod
    def deselect():
        keyboard.press('Key.right')
        keyboard.release('Key.right')
    @staticmethod
    def bold():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('b')
            keyboard.release('b')
    @staticmethod
    def italic():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('i')
            keyboard.release('i')
    @staticmethod
    def underline():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('u')
            keyboard.release('u')
    @staticmethod
    def center_text():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('e')
            keyboard.release('e')
    @staticmethod
    def open_file():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('o')
            keyboard.release('o')
            #todo
    @staticmethod
    def copy():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('c')
            keyboard.release('c')
    @staticmethod
    def paste():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
    @staticmethod
    def close():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('w')
            keyboard.release('w')
            #todo
    @staticmethod
    def decrease_font_size():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('[')
            keyboard.release('[')
    @staticmethod
    def increase_font_size():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(']')
            keyboard.release(']')
    @staticmethod
    def cut_text():
        wordlib.select_all()
        with keyboard.pressed(Key.ctrl):
            keyboard.press('x')
            keyboard.release('x')
    @staticmethod
    def undo():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('z')
            keyboard.release('z')
    @staticmethod
    def redo():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('y')
            keyboard.release('y')
    @staticmethod
    def left_align_text():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('l')
            keyboard.release('l')
    @staticmethod
    def right_align_text():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('r')
            keyboard.release('r')
    @staticmethod
    def create_new_document():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('n')
            keyboard.release('n')
    @staticmethod
    def split_document_window():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.alt):
                keyboard.press('s')
                keyboard.release('s')
    @staticmethod
    def print_document():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('p')
            keyboard.release('p')
        #todo
    @staticmethod
    def double_underline():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('d')
                keyboard.release('d')
    @staticmethod
    def subscript():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('=')
            keyboard.release('=')
    @staticmethod
    def superscript():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('=')
                keyboard.release('=')
    @staticmethod
    def one_char_left():
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    @staticmethod
    def one_char_right():
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    @staticmethod
    def one_word_left():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.left)
            keyboard.release(Key.left)
    @staticmethod
    def one_word_right():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.right)
            keyboard.release(Key.right)
    @staticmethod
    def one_para_up():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.up)
            keyboard.release(Key.up)
    @staticmethod
    def one_para_down():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.down)
            keyboard.release(Key.down)
    @staticmethod
    def one_line_up():
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    @staticmethod
    def one_line_down():
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    @staticmethod
    def end_of_line():
        keyboard.press(Key.end)
        keyboard.release(Key.end)
    @staticmethod
    def beg_of_line():
        keyboard.press(Key.home)
        keyboard.release(Key.home)
    @staticmethod
    def end_of_document():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.end)
            keyboard.release(Key.end)
    @staticmethod
    def beg_of_document():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.home)
            keyboard.release(Key.home)
    @staticmethod
    def delete_one_char_left():
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    @staticmethod
    def delete_one_char_right():
        keyboard.press(Key.delete)
        keyboard.release(Key.delete)
    @staticmethod
    def delete_one_word_left():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
    @staticmethod
    def delete_one_word_right():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.delete)
            keyboard.release(Key.delete)
    @staticmethod
    def new_line():
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    @staticmethod
    def caps_lock():
        keyboard.press(Key.capslock)
        keyboard.release(Key.capslock)
