import random
import sys
import uuid
from ppy_common import PPyCException


class PyCommon:

    @staticmethod
    def uuid() -> str:
        unique_id = str(uuid.uuid1())
        return unique_id.upper()

    @staticmethod
    def get_random(length=12) -> str:
        unique_id = PyCommon.uuid()
        unique_id = unique_id.replace("-", "")
        unique_id = unique_id[:length]
        return unique_id.lower()

    @staticmethod
    def get_random_6digit():
        random_number = random.randint(0, 999999)
        return "{:06d}".format(random_number)

    @staticmethod
    def import_from_string(import_name: str, silent: bool = False):
        if not import_name:
            return None
        import_name = import_name.replace(":", ".")
        try:
            try:
                __import__(import_name)
            except ImportError:
                if "." not in import_name:
                    raise
            else:
                return sys.modules[import_name]

            module_name, obj_name = import_name.rsplit(".", 1)
            module = __import__(module_name, globals(), locals(), [obj_name])
            try:
                if hasattr(module, obj_name):
                    return getattr(module, obj_name)
            except AttributeError as e:
                raise ImportError(e)

        except ImportError as e:
            if not silent:
                error = "Emport Name: " + import_name
                error += "\n" + str(e)
                raise PPyCException(error)

        return None