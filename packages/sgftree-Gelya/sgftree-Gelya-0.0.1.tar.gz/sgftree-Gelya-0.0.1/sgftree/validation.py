SGF_COODINATES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
STONES = ["K", "Q", "R", "B", "N"]


def validate_move(data: list, size: int = 19):
    if not data:
        return []

    value = data[0]
    assert len(value) == 2, f"Incorrect move: {value}"

    x, y = value
    assert any([
        x in SGF_COODINATES[:size] and y in SGF_COODINATES[:size],
        (value == "tt" and size <= 19)
    ]), f"Incorrect coordinates: {value}"

    return [value]


def validate_none(data: list, size: int = 19):
    return []


def validate_number(data: list, size: int = 19):
    assert data, "No number found"

    value = data[0]
    assert value.isdigit(), f"Not a number: {value}"

    return [int(value)]


def validate_double(data: list, size: int = 19):
    assert data, "No number found"

    value = data[0]
    try:
        return [float(value)]
    except ValueError:
        raise AssertionError(f"Not a double: {value}")


def validate_point(value: str, size: int = 19):
    assert len(value) == 2, f"Incorrect point: {value}"
    x, y = value
    assert x in SGF_COODINATES[:size] and y in SGF_COODINATES[:size], f"Incorrect coordinates: {value}"

    return value


def validate_points(data: list, size: int = 19):
    assert data, "No points found"

    for value in data:
        validate_point(value, size)

    return data


def validate_stone(value: str, size: int = 19):
    assert len(value) == 2 if ":" not in value else len(value) == 4, f"Incorrect stone: {value}"

    stone, xy = value.split(":") if ":" in value else (None, value)
    assert stone is None or stone in STONES
    validate_point(xy, size)

    return value


def validate_stones(data: list, size: int = 19):
    assert data, "No stones found"

    for value in data:
        validate_stone(value, size)

    return data


def validate_color(data: str, size: int = 19):
    assert data, "No color found"

    value = data[0]
    assert value in ["B", "W"]

    return [value]


property_values = {}