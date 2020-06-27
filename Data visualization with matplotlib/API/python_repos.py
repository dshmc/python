import requests
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",'\t', r.status_code)

# Сохранение ответа API в переменной.
response_dict = r.json()
print("Total repositories:", '\t',response_dict['total_count'])

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Построение визуализации.
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation =45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width - 1000
chart = pygal.Bar( my_config, style=my_style)
chart.title = 'Most-Starred Python Projeсt on GitHub'
chart.x_labels = names
"""
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of Django.'},
    {'value': 14798, 'label': 'Description of Flask.'},
    ]   
"""
chart.add('', stars)
chart.render_to_file('python_repos.svg')

