import student_management as sms


def setup_function():
    sms.students.clear()


def test_add_student():
    result = sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    assert result is True
    assert len(sms.students) == 1
    assert sms.students[0]["id"] == "101"
    assert sms.students[0]["name"] == "Kavya"
    assert sms.students[0]["age"] == 20
    assert sms.students[0]["course"] == "Computer Science"


def test_empty_student_id():
    result = sms.add_student(
        "",
        "Kavya",
        20,
        "Computer Science"
    )

    assert result is False
    assert len(sms.students) == 0


def test_duplicate_student_id():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    result = sms.add_student(
        "101",
        "Rahul",
        21,
        "Engineering"
    )

    assert result is False
    assert len(sms.students) == 1


def test_empty_name():
    result = sms.add_student(
        "101",
        "",
        20,
        "Computer Science"
    )

    assert result is False


def test_invalid_age():
    result = sms.add_student(
        "101",
        "Kavya",
        -5,
        "Computer Science"
    )

    assert result is False


def test_invalid_age_type():
    result = sms.add_student(
        "101",
        "Kavya",
        "twenty",
        "Computer Science"
    )

    assert result is False


def test_empty_course():
    result = sms.add_student(
        "101",
        "Kavya",
        20,
        ""
    )

    assert result is False


def test_find_student_by_id():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    student = sms.find_student_by_id("101")

    assert student is not None
    assert student["name"] == "Kavya"


def test_find_non_existing_student():
    student = sms.find_student_by_id("999")

    assert student is None


def test_search_students_by_name():
    sms.add_student(
        "101",
        "Kavya Kansagara",
        20,
        "Computer Science"
    )

    sms.add_student(
        "102",
        "Rahul Sharma",
        21,
        "Engineering"
    )

    sms.add_student(
        "103",
        "Kavita Patel",
        19,
        "Science"
    )

    found_students = sms.search_students_by_name("kav")

    assert len(found_students) == 2


def test_search_by_name_case_insensitive():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    found_students = sms.search_students_by_name("KAVYA")

    assert len(found_students) == 1
    assert found_students[0]["name"] == "Kavya"


def test_update_student_name():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    result = sms.update_student(
        "101",
        "name",
        "Kavya Kansagara"
    )

    assert result is True
    assert sms.students[0]["name"] == "Kavya Kansagara"


def test_update_student_age():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    result = sms.update_student(
        "101",
        "age",
        21
    )

    assert result is True
    assert sms.students[0]["age"] == 21


def test_update_student_course():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    result = sms.update_student(
        "101",
        "course",
        "Software Engineering"
    )

    assert result is True
    assert sms.students[0]["course"] == "Software Engineering"


def test_update_non_existing_student():
    result = sms.update_student(
        "999",
        "name",
        "Unknown"
    )

    assert result is False


def test_update_invalid_age():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    result = sms.update_student(
        "101",
        "age",
        -10
    )

    assert result is False
    assert sms.students[0]["age"] == 20


def test_update_invalid_field():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    result = sms.update_student(
        "101",
        "city",
        "Pune"
    )

    assert result is False


def test_delete_student():
    sms.add_student(
        "101",
        "Kavya",
        20,
        "Computer Science"
    )

    result = sms.delete_student("101")

    assert result is True
    assert len(sms.students) == 0


def test_delete_non_existing_student():
    result = sms.delete_student("999")

    assert result is False