from pygal_maps_world import i18n

def get_country_code(country_name):
    """Возвращает для заданой страны ее код Pygal, состоящий из 2 букв."""
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
        #Если страна не найдена, вернуть None
    return None
