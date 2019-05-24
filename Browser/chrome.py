from Speechmanager.speech_manager import speech as sp
from pynput.keyboard import Key,Controller
from Speechmanager.TTS import tts
from Write import writing
keyboard = Controller()

class chromelib:
    #functionalty of chrome
    @staticmethod
    def OpenNewWindow():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('n')
            keyboard.release('n')
    @staticmethod
    def OpenNewIncognitoWindow():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('n')
                keyboard.release('n')
    @staticmethod
    def OpenNewTab():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('t')
            keyboard.release('t')
    @staticmethod
    def ReopenLastClosedTab():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('t')
                keyboard.release('t')
    @staticmethod
    def JumpToNextOpenTab():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('Key.tab')
            keyboard.release('Key.tab')
    @staticmethod
    def JumpToPreviousOpenTab():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('Key.tab')
                keyboard.release('Key.tab')
    @staticmethod
    def MinimizeCurrentWindow():
        with keyboard.pressed(Key.alt):
            with keyboard.pressed(Key.space):
                keyboard.press('n')
                keyboard.release('n')
    @staticmethod
    def CloseCurrentWindow():
        with keyboard.pressed(Key.alt):
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
    @staticmethod
    def CloseCurrentTab():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('w')
            keyboard.release('w')
    @staticmethod
    def QuitChrome():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('q')
                keyboard.release('q')
    @staticmethod
    def StopLoadingPage():
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
    @staticmethod
    def PrintCurrentPage():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('p')
            keyboard.release('p')
    @staticmethod
    def SaveCurrentPage():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('s')
            keyboard.release('s')
    @staticmethod
    def ReloadCurrentPage():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('r')
            keyboard.release('r')
    @staticmethod
    def EverythingOnPageBigger():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('+')
            keyboard.release('+')
    @staticmethod
    def EverythingOnPageSmaller():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('-')
            keyboard.release('-')
    @staticmethod
    def EverythingOnPageDefaultSize():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('0')
            keyboard.release('0')
    @staticmethod
    def DeletePreviousWord():
        with keyboard.pressed(Key.ctrl):
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
    @staticmethod
    def GoToTopOfPage():
        keyboard.press(Key.home)
        keyboard.release(Key.home)
    @staticmethod
    def GoToEndOfPage():
        keyboard.press(Key.end)
        keyboard.release(Key.end)
    @staticmethod
    def OpenChromeMenu():
        with keyboard.pressed(Key.alt):
            keyboard.press('e')
            keyboard.release('e')
    @staticmethod
    def OpenFindBar():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('f')
            keyboard.release('f')
    @staticmethod
    def write():
        writing.write()
    @staticmethod
    def JumpToNextMatchOfFindBarsearch():
        with keyboard.pressed(Key.ctrl):
            keyboard.press('g')
            keyboard.release('g')
    @staticmethod
    def JumpToPreviousMatchOfFindBarsearch():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press('g')
                keyboard.release('g')
    @staticmethod
    def ClearBrowsingDataOption():
        with keyboard.pressed(Key.ctrl):
            with keyboard.pressed(Key.shift):
                keyboard.press(Key.delete)
                keyboard.release(Key.delete)
