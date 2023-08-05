#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import gen_browser_header.main.GenUA as gen_ua

import gen_browser_header.self.SelfEnum as self_enum
import gen_browser_header.helper.Helper as gbh_helper

def gen_header(setting, url, num=None):
    '''
    :param setting:
    :param url: 根据url生成host
    :param num:
    :return:
    '''
    ua = []
    if num is not None:
        # 如果只需要一个header，优选返回firefox的ua
        if num == 1:
            # print(setting.browser_type)
            if self_enum.BrowserType.FireFox in setting.browser_type:
                # print('num =1 browse=ff')
                ua += gen_ua.generate_firefox_ua(setting=setting, num=1)
            elif self_enum.BrowserType.Chrome in setting.browser_type:
                # print('num =1 browse=ch')
                ua += gen_ua.generate_chrome_ua(setting=setting, num=1)
        # 如果需要多个header
        else:
            # 如果可以产生ff的ua，先产生
            if self_enum.BrowserType.FireFox in setting.browser_type:
                ua += gen_ua.generate_firefox_ua(setting=setting, num=num)

            # 如果生成的ff的ua数量不满足，再尝试生成chrome的ua
            if len(ua) < num:
                if self_enum.BrowserType.Chrome in setting.browser_type:
                    ua += gen_ua.generate_chrome_ua(setting=setting, num=num)
    # num = None，生成最大数量的ua
    else:
        if self_enum.BrowserType.FireFox in setting.browser_type:
            ua += gen_ua.generate_firefox_ua(setting=setting)
        if self_enum.BrowserType.Chrome in setting.browser_type:
            ua += gen_ua.generate_chrome_ua(setting=setting)

    header = []
    host = gbh_helper.extract_host_from_url(url)
    for single_ua in ua:
        # setting.header_no_ua['User-Agent'] = single_ua
        # tmp_header = setting.header_no_ua
        # tmp_header['User-Agent'] = single_ua
        if 'Firefox' in single_ua:
            header.append({**setting.firefox_header_no_ua,
                           **{'User-Agent': single_ua},
                           **{'Host': host}
                           })
        elif 'Chrome' in single_ua:
            header.append({**setting.chrome_header_no_ua,
                           **{'User-Agent': single_ua},
                           **{'Host': host}
                           })
    return header


if __name__ == '__main__':
    import gen_browser_header.setting.Setting as setting

    cur_setting = setting.GbhSetting()
    cur_setting.proxy_ip = ['10.11.12.13:9090']
    cur_setting.browser_type = {self_enum.BrowserType.FireFox}
    cur_setting.firefox_ver = {'min': 74, 'max': 75}
    cur_setting.os_type = {self_enum.OsType.Win64}
    cur_setting.chrome_type = {self_enum.ChromeType.Stable}
    cur_setting.chrome_max_release_year = 1
    r = gen_header(setting=cur_setting, url='https://packaging.python.org/tutorials/packaging-projects/')
    print(r)
