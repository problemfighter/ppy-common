class DataUtil:

    @staticmethod
    def get_dict_value(data: dict, key: str, default=None):
        if not data or not key:
            return default
        elif key in data:
            return data[key]
        return default

    @staticmethod
    def get_object_fields(data_object: object):
        fields = []
        for field in dir(data_object):
            if not field.startswith('__'):
                fields.append(field)
        return fields

    @staticmethod
    def copy_object_to_object(source_object: object, dst_object: object):
        fields = DataUtil.get_object_fields(dst_object)
        if fields and source_object:
            for field in fields:
                if hasattr(source_object, field):
                    setattr(dst_object, field, getattr(source_object, field))
        return dst_object

    @staticmethod
    def copy_dict_to_object(dictionary: dict, data_object: object):
        if dictionary and data_object:
            for dict_key in dictionary:
                value = dictionary[dict_key]
                if hasattr(data_object, dict_key):
                    setattr(data_object, dict_key, value)
        return data_object

    @staticmethod
    def round_amount(amount, after_point=3):
        if not amount:
            return amount
        return round(amount, after_point)

    @staticmethod
    def parse_float(value):
        if value is None:
            return value
        return float(str(value))

    @staticmethod
    def parse_int(value):
        if value is None:
            return value
        return int(str(value))

    @staticmethod
    def percentage_value(amount, percentage):
        if amount is None or percentage is None:
            return amount
        return (amount * percentage) / 100
