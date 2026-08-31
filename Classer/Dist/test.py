import Engine as En

En.colorix.init()

En.Text.println(En.colorix.RED + "TEST" + En.colorix.RESET)
En.Text.printdi("INFO", "TEST")

En.VGUI.TextWindow.cr_window("Hello", "This is test", 2)
