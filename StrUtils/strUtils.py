# -*- coding:utf-8 -*-
from collections.abc import Iterable


def format_for(s, ls=None, jmark=None, startm=None, endm=None):
    """
    :param s: 元字符串
    :param jmark: 中间连接需要的符号
    :param ls: 需要连接到字符串上的字符串
    :param startm: 连接开始符号
    :param endm: 连接结束符号
    :return: 返回新字符串
    """
    if isinstance(ls, Iterable) and len(ls) != 0:
        if jmark is not None:
            if startm is not None:
                if endm is None:
                    s = format_s(s, ls, jmark, startm)
                    return s
                else:
                    s = format_e(s, ls, jmark, startm, endm)
                    return s

            else:
                if endm is not None:
                    s = format_ls(s, ls)
                    s += endm
                    return s
            s = format_j(s, ls, jmark)
        else:
            s = s + (startm if startm is not None else "")
            s = format_ls(s, ls) + (endm if endm is not None else "")
    else:
        print("缺少序列！")
    return s


def format_ls(s, ls):
    for i in ls:
        s += str(i)
    return s


def format_j(s, ls, jmark):
    s = s + jmark
    for i in ls:
        s += (str(i) + jmark)
    s = s[: len(s) - 1]
    return s


def format_s(s, ls, jmark, startm):
    s = s + startm + (format_j(s, ls, jmark)[len(s)+1:])
    return s


def format_e(s, ls, jmark, startm, endm):
    s = format_s(s, ls, jmark, startm)
    s = s + endm
    return s


if __name__ == '__main__':
    data = "1"
    data = format_for(data, ls=range(2, 10), jmark='+', startm='(', endm=')')
    print(data)


