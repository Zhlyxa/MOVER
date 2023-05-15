from typing import Literal


def moveToLib(userName, fullpath: str, versionPy: Literal['311', '310', '39']):
    """Функция отправки ваших файлов как модуля в глобальное окружение питон

    Args:
        fullpath (``str``): полный путь до вашего файла 
        versionPy (``int``): версия питона (пример ``311``)
    """
    fullpath = fullpath.replace('\\', '/')
    with (
        open(f"C:/Users/{userName}/AppData/Local/Programs/Python/Python{versionPy}/Lib/{fullpath[fullpath.rfind('/')+1:]}", 'w') as fileInLib,
        open(fullpath, 'r') as fileToRead
    ):
        fileInLib.write(fileToRead.read())