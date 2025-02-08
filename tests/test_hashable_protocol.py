from main.sorted_frozen_set import SortedFrozenSet


def test_equel_sets_have_the_Same_hash_code():
    s1 = SortedFrozenSet([5, 2, 1, 4])
    s2 = SortedFrozenSet([5, 2, 1, 4])

    assert hash(s1) == hash(s2)