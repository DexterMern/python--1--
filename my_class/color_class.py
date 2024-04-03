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

    def _set_Rgb(self, Rgb):
        self._rgb = Rgb

    def _get_Rgb(self):
        return self._Rgb

    name = property(_get_name, _set_name)
    Rgb = property(_get_Rgb, _set_Rgb)


c = Color(0x6783f5, 'light blue')
print(c._get_name())
c._set_Rgb(0x091B66)
c._set_name('blue')
rgb = c._get_Rgb()
