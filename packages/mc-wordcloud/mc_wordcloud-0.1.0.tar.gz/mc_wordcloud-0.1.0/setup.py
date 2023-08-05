import setuptools
setuptools.setup(
    name = "mc_wordcloud",
    version = "0.1.0",
    author = "魔扣少儿编程",
    author_email = "2443927272@qq.com",
    url = "https://github.com/LucasKKK/mc_wordcloud", 
    data_files = [('mc_wordcloud', [
        'mc_wordcloud/weapon_list.txt',
        'mc_wordcloud/hero_name.txt',
        'mc_wordcloud/tool_list.txt'
    ])
    ],
    packages = ['mc_wordcloud'],     #多个文件夹手动添加
    include_package_data = True,
    #packages = setuptools.find_packages(),

    install_requires = ['wordcloud', 'matplotlib'],
    zip_safe = False

)
