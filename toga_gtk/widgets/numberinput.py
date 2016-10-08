from gi.repository import Gtk

from toga.interface import NumberInput as NumberInputInterface

from .base import WidgetMixin

class NumberInput(WidgetMixin, NumberInputInterface):

    def __init__(self, id=None, style=None, min=0, max=100, step=1, **ex):
        super().__init__(id=id, style=style, min=min, max=max, step=step, **ex)
        self._create()

    def create(self):

        self._impl = Gtk.Box()
        self._impl._interface = self

        adjustment = Gtk.Adjustment(0, self._config["min_value"], self._config["max_value"], 1, 10, 0)

        self._spinimpl = Gtk.SpinButton()
        self._spinimpl.set_adjustment(adjustment)
        self._spinimpl.set_numeric(True)
        self._spinimpl._interface = self
        self._impl.pack_start(self._spinimpl, False, False, 0)

        self.style.width = 90
        self.style.height = 32

    def _get_value(self):
        return 0

    def _set_value(self, value):
        pass
