from typing import Any
from node import Node


class Stack:
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self.__top: Node | None = None
        self.__size = 0

    def empty(self) -> bool:
        """Return True when stack is empty, False otherwise."""
        return not self.__top

    def push(self, item: Any) -> None:
        """Push an item into the stack."""
        self.__top = Node(item, self.__top)
        self.__size += 1

    def pop(self) -> Any:
        """Remove and return the most recently pushed item from the stack."""
        if self.empty():
            raise Exception('stack is empty')
        this = self.__top.val
        self.__top = self.__top.link
        self.__size -= 1
        return this

    def top(self) -> Any:
        """Return the most recently pushed item into the stack."""
        if self.empty():
            raise Exception('stacck is empty')
        return self.__top.val

    def __len__(self) -> int:
        """Implement len(self)."""
        return self.__size
