from collections.abc import Iterable, Hashable, Iterator
from typing import Any

from main.sorted_frozen_set_dtypes import SupportsRichComparisonT, SupportsRichComparison


class SortedFrozenSet:
    def __init__(self, items: Iterable[SupportsRichComparisonT] | None = None) -> None:
        self._items: tuple[SupportsRichComparisonT, ...] = tuple(sorted(set(items)) if items is not None else set())

    def __contains__(self, item: Hashable) -> bool:
        return item in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[SupportsRichComparison]:
        return iter(self._items)
        # for item in self._items:
        #     yield item
    def __getitem__(self, index: int | slice) -> SupportsRichComparison | "SortedFrozenSet":
        items: SupportsRichComparison | tuple[SupportsRichComparison] = self._items[index]

        if isinstance(index, slice) and isinstance(items, tuple):
            return SortedFrozenSet(items)
        return items

    def __repr__(self) -> str:
        return (f"{type(self).__name__}"
                f"({f'[{", ".join(map(repr, self._items))}]' if self._items else ''})")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._items == other._items

    def __hash__(self) -> int:
        return hash(self._items)