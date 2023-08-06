
# (C) Michael DeHaan <michaeldehaan.net>, 2020

from classforge.fields import Field

class Class(object):

    __SLOTS__ = [ '_cf_fields' ]

    def __init__(self, *args, **kwargs):

        self._cf_fields = {}

        supers = self.__class__.mro()
        for super in supers:
            members = super.__dict__.keys()
            for attribute in members:
                value = super.__dict__[attribute]
                if attribute not in self._cf_fields:
                    if isinstance(value, Field):
                        self._cf_fields[attribute] = value.copy()

        for (k,v) in kwargs.items():
            self._cf_fields[k]._INTERNAL_set(self, k, v)


    def __setattr__(self, what, value):

        if what in Class.__SLOTS__:
            object.__setattr__(self, what, value)
            return

        field = self._cf_fields.get(what)
        field._INTERNAL_set(self, what, value)

    def explain_field(self, what):

        fields = object.__getattribute__(self, '_cf_fields')
        return fields[what].show()

    def __getattribute__(self, what):

        fields = super(Class, self).__getattribute__('_cf_fields')
        if what in fields:
            return fields[what]._INTERNAL_get(self, what)
        return super(Class, self).__getattribute__(what)

    def to_dict(self):
        data = dict()
        for (k,v) in self._cf_fields.items():
            data[k] = v.value
            if isinstance(v.value, Class):
                data[k] = v.value.to_dict()
        return data

    @classmethod
    def from_dict(cls, values):
        new_dict = dict()
        for (k,v) in values.items():
            field = getattr(cls, k)
            v2 = v
            if type(v) == dict and field.type != dict:
                v2 = field.type.from_dict(v)
            new_dict[k] = v2
        return cls(**new_dict)


