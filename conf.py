# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "https://sourbell.im/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "sourbell/meme.github.io@gh-pages"
}

# 站点设置
site_name = "Bristle Tail"
site_logo = "${static_prefix}logo.jpg"
site_build_date = "2020-08-21T12:19+08:00"
author = "Bristletail"
email = "i@sourbell.im"
author_homepage = "https://sourbell.im"
description = "Keep resolutions"
key_words = ['Maverick', 'sourbell', 'Bristletail', 'blog']
language = 'chinese'
locale = 'Asia/Shanghai'
background_img = ''
external_links = [
    {
        "name": "小花的架子鼓",
        "url": "https://blog.junli.de/",
        "brief": "🌵Julie 的部落格 🌵"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "X5qiy62TtnWiqWRM7tnsnrnl-9Nh9j0Va",
    "appKey": "ERjI9kNprFRou6YbfXyftEG5",
    "visitor": "True",
    "recordIP": True
}

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/sourbell",
        "icon": "fab fa-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/sourbell",
        "icon": "fab fa-github-alt"
    },
    {
        "name": "Steam",
        "url": "https://steamcommunity.com/id/sourbell/",
        "icon": "fab fa-steam-symbol"
    },
    {
        "name": "PSN",
        "url": "https://my.playstation.com/profile/Bristle2tail",
        "icon": "fab fa-playstation"
    },
    {
        "name": "BattleNet",
        "url": "https://d3.blizzard.cn/profile/sourbell-5971",
        "icon": "fab fa-battle-net"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<script src="https://kit.fontawesome.com/8780f0a025.js" crossorigin="anonymous"></script>
<style>.fab:before{margin:0 .2em;}</style>
'''

footer_addon = ''

body_addon = ''
