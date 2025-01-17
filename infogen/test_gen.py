# ！/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) 2017-2020 Rhilip <rhilipruan@gmail.com>

from gen import Gen

if __name__ == '__main__':
    douban_link_list = [
        "https://movie.douban.com/subject/1308452130/",  # Douban not exist
        "https://movie.douban.com/subject/3541415/",  # Douban Normal Foreign
        "https://movie.douban.com/subject/1297880/",  # Douban Normal Chinese
        "https://movie.douban.com/subject/5295054/",  # Fix No year error in Douban
        "https://douban.com/subject/30395527/",  # Wide Douban Link without subdomain
        "https://www.douban.com/subject/26970964/"  # Wide Douban Link with subdomain like `www`
    ]

    imdb_link_list = [
        "http://www.imdb.com/title/tt4925292/",  # Imdb through Douban
        "https://www.imdb.com/title/tt0083662/",  # Fix without duration and douban rate
    ]

    bgm_link_list = [
        "https://bgm.tv/subject/2071342495",  # Bangumi not exist
        "https://bgm.tv/subject/207195",  # Bangumi Normal
        "https://bgm.tv/subject/212279/",  # Bangumi Multiple characters
        "https://bangumi.tv/subject/220312",  # Bangumi Other Domain
        "http://chii.in/subject/12345",  # Bangumi Other Domain
        "https://bgm.tv/subject/204027",  # Fix No story error in Bangumi
    ]

    steam_link_list = [
        "http://store.steampowered.com/app/20650135465430/",  # Steam Not Exist
        "http://store.steampowered.com/app/550/",  # Steam Short Link (Store)
        "http://store.steampowered.com/app/240720/Getting_Over_It_with_Bennett_Foddy/",  # Steam Full Link
        "https://steamcommunity.com/app/668630",  # Another Type of Steam Link (Hub)
        "http://store.steampowered.com/app/420110",  # Steam Link With Age Check (One click type)
        "http://store.steampowered.com/app/489830/",  # Steam Link With Age Check (Birth Choose type)
        "https://store.steampowered.com/app/517630/Just_Cause_4/"  # New Age Check pass in Steam
        "https://store.steampowered.com/app/968790",  # Fix tag class miss
        "https://store.steampowered.com/app/734730/Ancient_Frontier_Steel_Shadows/",  # Fix no review
    ]

    indienova_link_list = [
        "https://indienova.com/game/111",  # Indienova not exist
        "https://indienova.com/game/abzu--1",  # Indienova Normal
        "https://indienova.com/game/shop-titans",  # Indienova Without Details
        "https://indienova.com/game/super-web-kittens-act-i",  # Indienova Without Tags
        "https://indienova.com/game/summer-islands",  # Indienova Without Age Rating
        "https://indienova.com/game/hellblade-senuas-sacrifice",  # Indienova With Many Price
    ]

    epic_link_list = [
        "https://store.epicgames.com/zh-CN/p/oute",  # Epic not exist
        "https://store.epicgames.com/zh-CN/p/outerwilds",  # Epic Normal
        "https://store.epicgames.com/zh-Hant/p/control",  # Edit regex for other language
        "https://store.epicgames.com/zh-CN/p/borderlands-3",  # Fix KeyError('recommended'), language "-"
        "https://store.epicgames.com/zh-CN/p/grand-theft-auto-v?lang=zh-CN",  # Fix miss site key
        "https://store.epicgames.com/zh-CN/p/saints-row",  #Fix KeyError('legalTags')
    ]

    gog_link_list = [
        "https://www.gog.com/zh/game/stard",  #GOG not exist
        "gog.com/zh/game/stardew_valley",  #GOG without www&https
        "https://www.gog.com/game/stardew_valley",  #GOG without language
        "https://www.gog.com/zh/game/stardew_valley", #GOG Normal
    ]

    other_link_list = [
        "http://jdaklvhgfad.com/adfad",  # No support link
    ]

    dict_link_list = [
        # Douban
        {'site': 'douban', 'sid': 3541415},  # Input dict object
        {'site': 'douban', 'sid': 'tt0083662'},  # IMDb though Douban
        # IMDb
        {'site': 'imdb', 'sid': 83662},
        {'site': 'imdb', 'sid': 'tt0083662'},
        {'site': 'imdb', 'sid': 'tt0111161'}
    ]

    test_link_list = [
        #{'site': 'imdb', 'sid': 'tt0111161'}
    ]
    # test_link_list.extend(douban_link_list)
    # test_link_list.extend(imdb_link_list)
    # test_link_list.extend(bgm_link_list)
    # test_link_list.extend(steam_link_list)
    # test_link_list.extend(indienova_link_list)
    # test_link_list.extend(epic_link_list)
    test_link_list.extend(gog_link_list)
    # test_link_list.extend(other_link_list)
    # test_link_list.extend(dict_link_list)

    for link in test_link_list:
        print("Test link: {}".format(link))
        gen = Gen(link).gen(_debug=True)
        if gen["success"]:
            print("Format text:\n", gen["format"])
            import json

            print(json.dumps(gen, ensure_ascii=False, sort_keys=True))
        else:
            print("Error : {}".format(gen["error"]))
        print("--------------------")
