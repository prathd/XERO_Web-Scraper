from riq_child import RIQChild
from item import Item

class Items(RIQChild) :
    _cache = []
    _cache_index = 0
    _page_index = 0
    _page_length = 50

    _parent = None

    def __init__(self, itemtype) :
        self._parent = itemtype
        self._object_class = Item

    def node(self) :
        return '/'+self._parent.id()+'/items'