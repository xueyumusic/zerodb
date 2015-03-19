from zope.interface import moduleProvides
from BTrees.Interfaces import IIntegerFloatBTreeModule
from BTrees.IFBTree import IFBTree as DefaultIFBTree
from BTrees.IFBTree import *


class IFBTree(DefaultIFBTree):
    max_internal_size = 200000
    max_leaf_size = 100000

BTree = IFBTree

moduleProvides(IIntegerFloatBTreeModule)