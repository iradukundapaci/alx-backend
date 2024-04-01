#!/usr/bin/env python3
"""
Pagination handle class
"""
from typing import Tuple
import csv
import math
from typing import List
from os import path, getcwd


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Function to retrieve pagination page

        args:
            page: page number
            page_size: amount of elements to retrieve

        return: list of list of elements
        """
        assert isinstance(page, int) and isinstance(
            page_size, int
        ), "page and page_size should be integers"
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function to create tuple pagination object

    args:
        page: page number
        page_size: size of elements

    return: tuple of page and page size
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    return tuple([start_index, end_index])


server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, "Bob")
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))
