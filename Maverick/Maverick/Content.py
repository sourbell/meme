# -*- coding: utf-8 -*-

from .Metadata import Metadata
from .Utils import safe_read
from .Renderer import Renderer

import re
import yaml
import codecs


def group_by_tagname(tag):
    def criteria(content):
        return tag in content.get_meta('tags')
    return criteria


def group_by_category(category):
    def criteria(content):
        return category in content.get_meta('categories')
    return criteria


class Content():
    def __init__(self, path):
        content = safe_read(path)

        # parse frontmatter
        r = re.compile(r'---([\s\S]*?)---')
        m = r.match(content)

        self.meta = Metadata(yaml.safe_load(m.group(1)))
        self.meta['path'] = path
        self.text = content[len(m.group(0)):]

        self.skip = not self.get_meta('status').lower() in [
            "publish", "published"]

        self._parsed = None
        self._excerpt = None

    @property
    def excerpt(self):
        if self._excerpt is None:
            self._excerpt = Renderer.excerpt(self)
        return self._excerpt

    @property
    def parsed(self):
        if self._parsed is None:
            self._parsed = Renderer.markdown(self)
        return self._parsed

    def get_meta(self, key, default=None):
        return self.meta.get(key, default)

    @staticmethod
    def cmp_by_date(content_1, content_2):
        date_1 = content_1.get_meta('date')
        date_2 = content_2.get_meta('date')
        if date_1 < date_2:
            return -1
        elif date_1 > date_2:
            return 1
        else:
            return 0


class ContentList(list):
    """Content List.

    Convinient for sorting and slicing.
    """

    def __init__(self, from_obj=[]):
        list.__init__(self, from_obj)

    def re_group(self, _func):
        """subset items with _func(item) = True
        """
        resultList = ContentList()
        for meta in self:
            if _func(meta) == True:
                resultList.append(meta)
        return resultList
