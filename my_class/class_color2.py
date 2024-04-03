class Color:
    def __init__(self, Rgb, name):
        self._Rgb = None
        self._rgb = Rgb
        self._name = name

    def _set_name(self, name):
        if name:
            self._name = name
        else:
            raise ValueError(f'invalid name {name!r}')

    def _get_name(self):
        return self._name

    def _del_name(self):
        print('Deliting...')
        del self._name

    # name = property(fget=_get_name, fset=_set_name)
    name = property()
    name = name.setter(_set_name)
    name = name.getter(_get_name)


c = Color(0x254564, 'red')
c.name = 5
print(c.name)
help(c)
