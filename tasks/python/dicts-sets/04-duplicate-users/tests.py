from solution import find_duplicates


def user(id, email):
    return {"id": id, "email": email}


def test_example():
    users = [user(1, "Ann@Test.io"), user(2, "bob@test.io"), user(3, " ann@test.io "),
             user(4, "BOB@test.io"), user(5, "zed@test.io")]
    assert find_duplicates(users) == [[1, 3], [2, 4]]


def test_no_duplicates():
    assert find_duplicates([user(1, "a@x.io"), user(2, "b@x.io")]) == []


def test_empty():
    assert find_duplicates([]) == []


def test_ids_keep_input_order():
    users = [user(9, "a@x.io"), user(3, "A@x.io"), user(5, "a@x.io")]
    assert find_duplicates(users) == [[9, 3, 5]]


def test_groups_in_first_appearance_order():
    users = [user(1, "b@x.io"), user(2, "a@x.io"), user(3, "a@x.io"), user(4, "b@x.io")]
    assert find_duplicates(users) == [[1, 4], [2, 3]]
