import time
import pygetwindow
import uiautomator2
def connect_game():
    adb=r"d:/platform-tools-latest-windows/platform-tools/adb.exe"
    fgo_windo=pygetwindow.getWindowsWithTitle("BlueStacks App Player")[0]
    android=uiautomator2.connect("emulator-5554")#c6tskfnzwkayzhnf
    fgo_windo.restore()
    fgo_windo.resizeTo(1280,720)
    fgo_windo.activate()
    time.sleep(1)
    fgo_left=fgo_windo.left
    fgo_top=fgo_windo.top
    fgo_width=fgo_windo.width
    fgo_height=fgo_windo.height
    print(android.window_size())
    print(fgo_width, fgo_height)
    return android