# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/master/COPYING

import os

import pytest

import pylint.lint

LIB_DIR = os.path.dirname(os.__file__)
MODULES_TO_CHECK = [f for f in os.listdir(LIB_DIR) if f.endswith(".py")
                    or os.path.exists(os.path.join(LIB_DIR, f, '__init__.py'))]
MODULES_TO_CHECK = MODULES_TO_CHECK


@pytest.mark.parametrize("test_module_name", MODULES_TO_CHECK)
def test_libmodule(test_module_name):
    os.chdir(LIB_DIR)
    try:
        pylint.lint.Run([test_module_name])
    except SystemExit as ex:
        assert ex.code != 32
        return

    assert False, "shouldn't get there"
