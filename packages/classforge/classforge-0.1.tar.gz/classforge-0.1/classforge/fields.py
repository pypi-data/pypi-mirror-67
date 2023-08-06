# (C) Michael DeHaan <michaeldehaan.net>, 2020



class Field(object):

    __slots__ = [
        '_id',
        'name',
        'type',
        'default',
        'nullable',
        'mutable',
        'accessor',
        'mutator',
        '_mutated',
        'choices',
        'value'
    ]

    def __init__(self, name=None, type=None, default=None, nullable=True, mutable=True, mutator=None, accessor=None, choices=None):

        assert mutator is None or (isinstance(mutator, str))
        assert accessor is None or (isinstance(accessor, str))

        self._id = 0
        self.type = type
        self.default = default
        self.nullable = nullable
        self.mutable = mutable
        self.mutator = mutator
        self._mutated = False
        self.accessor = accessor
        self.choices = choices
        self.value = None

        if default is not None and self.value is None:
            self.value = default

    def show(self):
        return dict(
            type = self.type,
            default = self.default,
            nullable = self.nullable,
            mutable = self.mutable,
            mutator = self.mutator,
            accessor = self.accessor,
            choices = self.choices,
            value = self.value,
            _id = self._id,
        )

    def copy(self):
        obj = Field(type=self.type, default=self.default, nullable=self.nullable, mutable=self.mutable, mutator=self.mutator, accessor=self.accessor, choices=self.choices)
        obj._mutated = False
        obj.value = self.value
        obj._id = self._id + 1
        return obj

    def _INTERNAL_get(self, parent, name):
        fn = self._find_function(parent, self.accessor, self._access, "get_%s" % name)
        val = fn(self.value)
        return val


    def _INTERNAL_set(self, parent, name, value):

        self._mutated = True

        if not self.mutable and self._mutated:
            raise ValueError("field is immutable: %s" % name)

        if value is None and not self.nullable:
            raise ValueError("field is not nullable: %s" % name)

        if (self.nullable and value is not None) and (self.type is not None):
            if not isinstance(value, self.type):
                raise ValueError("invalid field type. got %s, expected: %s" % (value, self.type))

        if self.choices is not None:
            if not value in self.choices:
                raise ValueError("rejected value: %s" % name)

        fn = self._find_function(parent, self.mutator, self._mutate, "set_%s" % name)
        val = fn(value)
        self.value = val

    def _find_function(self, parent, member, default_func, func_pattern):

        if member is None:
            fn2 = getattr(parent, func_pattern, None)
            if fn2 is not None:
                return fn2
        else:
            fn3 = getattr(parent, member, None)
            if fn3 is None:
                raise AttributeError("missing function: %s" % member)
            return fn3
        return default_func

    def _access(self, value):
        return value

    def _mutate(self, value):
        return value



