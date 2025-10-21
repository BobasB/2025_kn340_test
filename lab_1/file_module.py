def func_for_module_import():
    return "This function is for module import testing."

def test_func_return_value():
    """
    Пробуємо створити тест всередині модуля"""
    assert type(func_for_module_import()) is str, "Функція має повертати стрічку"
