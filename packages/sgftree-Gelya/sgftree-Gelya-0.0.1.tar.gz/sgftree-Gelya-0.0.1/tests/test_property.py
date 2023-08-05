import pytest

from sgftree import Property


@pytest.mark.parametrize(
    "label, data, expected",
    [
        ("B", ["aa"], "B[aa]"),
        ("W", ["aa", "aa"], "W[aa]"),
        ("TR", ["aa", "ab"], "TR[aa][ab]"),
        ("TR", ["aa", "ac", "ab"], "TR[aa][ab][ac]"),
    ],
)
def test_property_create(label, data, expected):
    new_prop = Property(label, data)
    assert str(new_prop) == expected


@pytest.mark.parametrize(
    "prop1, prop2, expected",
    [
        (Property("TR", ["aa"]), Property("TR", ["aa"]), "TR[aa]"),
        (Property("TR", ["aa"]), Property("TR", ["ab"]), "TR[aa][ab]"),
        (Property("TR", ["aa", "ab"]), Property("TR", ["ab", "ac"]), "TR[aa][ab][ac]"),
    ],
)
def test_property_merge(prop1, prop2, expected):
    prop1.merge(prop2)
    assert str(prop1) == expected
