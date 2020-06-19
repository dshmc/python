from pygal_maps_world import i18n

def get_country_code(country_name):
    """Возвращает для заданой страны ее код Pygal, состоящий из 2 букв."""
    for code, name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
        #Если страна не найдена, вернуть None
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))