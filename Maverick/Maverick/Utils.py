# -*- coding: utf-8 -*-

import os
import shutil
import codecs
import hashlib
import chardet
import json
from .Config import g_conf
from enum import Enum


class Color(Enum):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37


def print_color(text: str, fg: Color = Color.BLACK.value, end='\n'):
    print('\033[%sm%s\033[0m' % (fg, text), end=end)


def logged_func(delim='\n'):
    def inner(func):
        def wrapper(*args, **kwargs):
            log_start(func.__name__, delim)
            func(*args, **kwargs)
            log_end()
        return wrapper
    return inner


def copytree(src, dst, syamlinks=False, ignore=None):
    for item in os.listdir(src):
        s = unify_joinpath(src, item)
        d = unify_joinpath(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, syamlinks, ignore)
        else:
            shutil.copy2(s, d)


def log_start(message, delim):
    print_color('Start ' + message, Color.YELLOW.value, end='...'+delim)


def log_end():
    print_color('done.', Color.YELLOW.value)


def safe_write(path, content, codec="utf-8"):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

    with codecs.open(path, "w+", encoding=codec) as f:
        f.write(content)


def safe_read(path):
    if not os.path.exists(path):
        return ""
    
    # utf-8 is prefered
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, 'rb') as f:
            content = f.read()
            encoding = chardet.detect(content)['encoding'] or 'utf-8'
            return content.decode(encoding=encoding)


def gen_hash(str):
    h1 = hashlib.md5()
    h1.update(str.encode(encoding='utf-8'))
    return h1.hexdigest()


def unify_joinpath(left, right):
    path = os.path.join(left, right)
    return path.replace('\\', '/')


g_translation = None


def tr(str, locale="english"):
    """translation support

    translate str according to translation file
    """
    global g_translation
    if g_translation is None:
        path = unify_joinpath('./locale', g_conf.language+".json")
        g_translation = json.loads(safe_read(path) or '{}')

    return g_translation.get(str, str)
