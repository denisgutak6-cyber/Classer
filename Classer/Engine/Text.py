import sys
from .VGUI import TextWindow
from .VGUI import Lang
from .INFO import ErrorCodes

END = "\n"

class Methods:
    #Помилка
    def error(EC):
        'Викликається при критичних помилках. Ця функція відкриває вікно з заголовком Engine Error і типом 0'
        TextWindow.cr_window(Lang.Engine_Error, EC, 0)
        sys.exit(1)
    #Попередження
    def warning(TXT):
        'Викликається коли користувачеві потрібно зробити попередження. Ця функція відкриває вікно з заголовком Engine Warning і типом 1'
        TextWindow.cr_window(Lang.Engine_Warn, TXT, 1)

    def info(TXT):
        'Викликається коли потрібно вивести якусь інформацію. Ця функція відкриває вікно з заголовком Engine Information і типом 2'
        TextWindow.cr_window(Lang.Engine_INFO, TXT, 2)
#Вивід Тексту
@staticmethod
def println(*args, sep=" "):
    try:
        text = sep.join(str(arg) for arg in args)
        sys.stdout.write(text + END)
    except Exception:
        Methods.error(ErrorCodes.E2)

#Вивід тексту з типом
@staticmethod
def printdi(Type, TEXT):
    println(f"[{Type}] {TEXT}")
