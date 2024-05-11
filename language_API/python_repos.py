import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 获取语言前10个项目数据
def get_data(language):
    # 执行API调用并存储响应
    URL = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=star'
    r = requests.get(URL)
    print("Status code:", r.status_code)
    # 将API响应存储在一个变量中
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])
    # 研究有关仓库的信息
    repo_dicts = response_dict['items']
    # names, plot_dicts = [], []
    plot_dicts = []
    for repo_dict in repo_dicts[:10]:
        # names.append(repo_dict['name'])
        # 加str解决“'NoneType' object has no attribute 'decode'”问题
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': str(repo_dict['description']),
            'xlink': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)
    return plot_dicts


# 可视化
# my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
# my_config.x_label_rotation = 45
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
# 主标签是y轴上为5000整数倍的刻度
# my_config.major_label_font_size = 18
# label显示字符数
# my_config.truncate_label = 15
# 是否显示水平辅助线
my_config.show_y_guides = True
my_config.width = 1000

# 渲染图标
# chart = pygal.Bar(my_config, style=my_style)
chart = pygal.Bar(my_config)
chart.title = 'Most-Starred JavaScript, Ruby, C, Java, Perl, Haskell, Go Projects on GitHub'
chart.x_labels = range(1, 11)

# 循环添加数据
languages = ['JavaScript', 'Ruby', 'C', 'Java', 'Perl', 'Haskell', 'Go']
for language in languages:
    plot_dicts = get_data(language)
    chart.add(language, plot_dicts)

chart.render_to_file('data/python_repos.svg')