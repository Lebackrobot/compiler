# -*- coding: utf-8 -*-
class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __repr__(self):
        return '(' + self.type + ' ' + self.text + ')'