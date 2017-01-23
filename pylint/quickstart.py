import importlib
import pkgutil

import pylint.checkers as checkers
# import pylint.extensions as extensions


def load_msgs(mod, acc):
    for _, modname, ispkg in pkgutil.iter_modules(mod.__path__):
        submodule = importlib.import_module(mod.__name__ + "." + modname)

        for cls_name in dir(submodule):
            cls = getattr(submodule, cls_name)
            if isinstance(cls, type) and issubclass(cls, checkers.BaseChecker):
                acc.update(cls.msgs)

        if ispkg:
            acc = load_msgs(submodule, acc)

    return acc


def Run():
    msgs = load_msgs(checkers, {})
    print(msgs.keys())


if __name__ == "__main__":
    Run()
