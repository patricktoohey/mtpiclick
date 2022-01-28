import time
import pyautogui
from .point import point
from pywinauto import application
from pyautogui import (
    moveTo, keyDown, keyUp, press
)

def moveClick(target, sleep=True):
    """

    Parameters
    ----------
    target :
        

    Returns
    -------

    """
    pyautogui.moveTo(target.x, target.y, 1, tween=pyautogui.easeInOutQuad)
    pyautogui.moveTo(target.x, target.y, 1)
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    if sleep:
        time.sleep(0)

class window:
    """ """
    def __init__(self, exe, reference):
        try:
            self.app = application.Application(backend="uia").connect(path = exe)
            self.dlg = self.app.window(title_re=reference)            
        except:
            self.app = application.Application(backend="uia").start(exe)    
            time.sleep(30)
            self.dlg = self.app.window(title_re=reference)

    @staticmethod
    def center(control):
        rect = control.rectangle()
        left = rect.left
        top = rect.top
        bottom = rect.bottom
        right = rect.right
        x = int(left - (left - right)/2)
        y = int(bottom - (bottom - top)/2)
        return point(x, y)

    def move(self, target):
        control = self.get(target)
        center = window.center(control)
        moveTo(center.x, center.y, 1)
        moveTo(center.x + 1, center.y + 1, 1)

    def click(self, target, value = ""):
        control = self.get(target, value)
        center = window.center(control)
        moveClick(center)

    def search(self, target, value):
        control = self.find(target, value)
        center = window.center(control)
        moveClick(center, sleep=False)

    def find(self, target, value):
        for index in range(4):
            for element in target.options:
                control = self.dlg.child_window(auto_id = element, found_index = index)
                found = window.value(control)
                if (found == value):
                    return control

    @staticmethod
    def value(control):
        return control.legacy_properties()['Name']

    def click_if(self, target, condition):
        control = self.get(target)

        if (window.value(control) == condition):
            self.click(target)

    def get(self, target, value=""):
        self.app.top_window().set_focus()
        if value == "":
            return self.dlg.child_window(auto_id = target)

        for index in range(4):
            control = self.dlg.child_window(auto_id = target, found_index=index)
            if (window.value(control) == value):
                return control
    
