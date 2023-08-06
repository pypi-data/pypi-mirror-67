# -*- coding:Utf-8 -*-
from __future__ import print_function
"""
"""
import pdb
import inspect

class Project(object):
    """ Generic Project Meta Class

    """

#        sns.set_style("white")

    def __init__(self):
        self.v1 = 3
        self.__inspect__()

    def __inspect__(self):
        self.lmembers = []
        self.lmeth = []
        for name,data in inspect.getmembers(self):
            if name.startswith('__'):
                continue
            if callable(data):
                nclass = data.__repr__().split('method ')[1].split('.')[0]
                self.lmeth.append((nclass,name))
            else:
                self.lmembers.append(name)

    def help(self, letter='az', typ='mt'):
        """ generic help

        Parameters
        ----------

        typ : string
            'mb' | 'mt'

            mb :members
            mt :methods

        letters : string

        """

        if typ == 'mb':
            for m in self.lmembers:
                print(m)

        if typ == 'mt':
            for s in self.lmeth:
                if s[1][0] != '_':
                    if len(letter) > 1:
                        if (s[1][0] >= letter[0]) & (s[1][0] < letter[1]):
                            try:
                                doc = eval(
                                    'self.'+s[1]+'.__doc__').split('\n')
                                print(s[0]+'.'+s[1] + ': ' + doc[0])
                            except:
                                print(s[0]+'.'+s[1])
                    else:
                        if (s[0][0] == letter[0]):
                            try:
                                doc = eval(
                                    'self.'+s+'.__doc__').split('\n')
                                print(s+': ' + doc[0])
                            except:
                                pass
