#! python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Dough(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        return NotImplemented


class ThickCrustDough(Dough):
    def __str__(self):
        return "Extra grube ciasto"


class ThinCrustDough(Dough):
    def __str__(self):
        return "Cienkie ciasto"