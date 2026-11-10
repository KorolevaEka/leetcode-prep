from solution import max_collinear


def test_examples():
    assert max_collinear([(0, 0), (1, 2), (2, 4), (5, 1)]) == 3
    assert max_collinear([(3, 3), (3, 3), (3, 3)]) == 3
    assert max_collinear([]) == 0


def test_small():
    assert max_collinear([(1, 1)]) == 1
    assert max_collinear([(1, 1), (2, 5)]) == 2


def test_vertical_and_horizontal():
    assert max_collinear([(2, 0), (2, 5), (2, -3), (7, 7)]) == 3
    assert max_collinear([(0, 4), (5, 4), (-2, 4), (1, 1)]) == 3


def test_points_on_both_sides_of_anchor():
    assert max_collinear([(0, 0), (1, 1), (-1, -1), (-2, -2), (5, 0)]) == 4
    assert max_collinear([(0, 0), (-1, 2), (1, -2), (2, -4), (3, 1)]) == 4


def test_unreduced_directions():
    assert max_collinear([(0, 0), (1, 2), (2, 4), (3, 6)]) == 4
    assert max_collinear([(0, 0), (2, 4), (3, 6), (1, 2), (9, 1)]) == 4


def test_duplicates_count_on_the_line():
    assert max_collinear([(1, 1), (1, 1), (2, 2), (3, 3), (0, 5)]) == 4
    assert max_collinear([(0, 0), (0, 0), (1, 5), (2, 7)]) == 3


def test_floats_would_confuse_lines():
    big = 10**9
    pts = [(0, 0), (big, big - 1), (big - 1, big - 2), (2 * big, 2 * big - 2)]
    assert max_collinear(pts) == 3
    assert max_collinear([(0, 0), (big, big - 1), (big - 1, big - 2)]) == 2


def test_matches_brute_force():
    import random
    from itertools import combinations
    rng = random.Random(11)
    for _ in range(150):
        pts = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(rng.randint(0, 9))]
        if len(pts) <= 2:
            expected = len(pts)
        else:
            expected = max(pts.count(point) for point in pts)
            for a, b in combinations(range(len(pts)), 2):
                (x1, y1), (x2, y2) = pts[a], pts[b]
                if (x1, y1) == (x2, y2):
                    continue
                cnt = sum(1 for (x, y) in pts if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1))
                expected = max(expected, cnt)
        assert max_collinear(pts) == expected


def test_large_grid():
    pts = [(x, y) for x in range(40) for y in range(20)]
    assert max_collinear(pts) == 40
