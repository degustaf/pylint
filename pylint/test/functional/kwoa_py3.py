# pylint: disable=invalid-name,missing-docstring,multiple-statements

test_lambda = lambda *, x: x


def test_fn(*, x): return x


def test_fn2(*, x):
    return x
