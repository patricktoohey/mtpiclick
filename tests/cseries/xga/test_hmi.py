import pytest
from mtpiclick.click import window
from mtpiclick.cseries.xga.hmi import hmi
from mtpiclick.cseries.xga.login import login
from mtpiclick.cseries.xga.keyboard import keyboard
from mtpiclick.cseries.xga.menu import menu
from mtpiclick.cseries.xga.scope import scope

@pytest.fixture(scope="module")
def cmain():
    path = r"C:\Users\toohey-1\Downloads\0_SoftwareVersions\C-Series\C3570 Test\5.32 2021-7\xmain_c.exe"
    reference = hmi.reference
    return window(path, reference)

@pytest.fixture(scope="module")
def keys():
    path = r"C:\Users\toohey-1\Downloads\0_SoftwareVersions\C-Series\C3570 Test\5.32 2021-7\xmain_c.exe"
    reference = keyboard.reference
    return window(path, reference)

def test_logout(cmain):
    cmain.click(hmi.lock)

def test_home(cmain):
    cmain.move(hmi.home)

def test_start(cmain):
    cmain.click_if(hmi.start, "Start ")

def test_login_password(cmain, keys):
    cmain.move(hmi.home)
    cmain.click(hmi.lock)
    cmain.click(login.password)
    keys.click(keyboard.key_3)
    keys.click(keyboard.ok)
    cmain.click(login.ok)
    cmain.move(hmi.home)
    cmain.click(hmi.lock)
    cmain.move(hmi.home)

def test_package_setup(cmain):
    cmain.click(hmi.menu)
    cmain.search(menu, "Packages")
    cmain.search(menu, "Active Package")
    cmain.search(menu, "Main Package Setup")

def test_loadcell_advanced(cmain):
    cmain.click(hmi.menu)
    cmain.search(menu, "Setup")
    cmain.search(menu, "System")
    cmain.click(menu.down)
    cmain.search(menu, "Loadcell Advanced Setup")

def test_scope(cmain):
    cmain.click(hmi.menu)
    cmain.search(menu, "Information")
    cmain.search(menu, "XRTC")
    cmain.search(menu, "XRTC: Oscilloscope")
    
def test_capture(snagit):
    snagit.click

def test_loadcell_advanced(cmain):
    cmain.click(scope.legend)
    cmain.click(scope.start)