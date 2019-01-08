#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xumeng"
__date__ = "2019/1/7 19:09"

import requests
import re


'''
基于金山词霸的翻译器
'''
trans_pattern = r'base-list([\w\W]*?)</ul>'
word_pattern = r'<span>([\w\W]*?)</span>'
words_pattern = r'in-base-top([\w\W]*?)</div>'


def trans_word(wd):
    url = 'http://www.iciba.com/' + wd
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                                 '(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    html = str(r.content, encoding='utf-8')
    result = re.findall(trans_pattern, html)
    if result:
        result = result[0]
        result = re.findall(word_pattern, result)
        trans_result = wd + '\n'
        for r in result:
            trans_result += r + '\n'
    else:
        result = re.findall(words_pattern, html)[0]
        result = re.findall(r'<div[\w\W]*?>([\w\W]*)', result)[0]
        trans_result = result
    return trans_result


def main():
    while True:
        wd = input('输入您要翻译的内容(q退出)：')
        if wd == 'q':
            exit()
        res = trans_word(wd)
        print(res)


if __name__ == "__main__":
    main()
