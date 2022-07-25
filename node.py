from typing import Any, Optional


class Node:
    def __init__(self, val: Any, link: Optional['Node'] = None):
        self.val = val
        self.link = link

    def _valid_link(self, link: Optional['Node']) -> bool:
        return isinstance(link, self.__class__) or link is None

    @property
    def link(self) -> Optional['Node']:
        return self.__link

    @link.setter
    def link(self, link: Optional['Node']) -> None:
        if not self._valid_link(link):
            raise TypeError
        self.__link = link
