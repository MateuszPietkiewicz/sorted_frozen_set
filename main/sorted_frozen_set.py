from collections.abc import Iterable, Hashable, Iterator

from main.sorted_frozen_set_dtypes import SupportsRichComparisonT, SupportsRichComparison


class SortedFrozenSet:
    def __init__(self, items: Iterable[SupportsRichComparisonT] | None = None) -> None:
        self._items: list[SupportsRichComparisonT] = sorted(set(items)) if items is not None else []

    def __contains__(self, item: Hashable) -> bool:
        return item in self._items

    # for item_ in self._items:
    #     if item_ == item:
    #         return True
    # return False

    # return item in self._items

    # return self._items.__contains__(item)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[SupportsRichComparison]:
        return iter(self._items)
        # for item in self._items:
        #     yield item