from enum import Enum
from typing import Annotated
import time
from annotated_types import Ge, Le
import clr
clr.AddReference('PiUsbNet')
import PiUsbNet

class Color(Enum):
    Pos1 = 1
    Pos2 = 2
    Pos3 = 3


class GenericDevice:

    def __init__(self, color, pfilter):
        self.pfilter = pfilter
        self._color = color
        self.changed_time_ms = time.time()*1000


    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, value):
        with open('log.txt', 'a') as the_file:
            the_file.write(str(time.time() * 1000) + 'setter color(self)\n')

        self._color = value
        self.changed_time_ms = time.time()*1000
        self.pfilter.MoveTo(int(value.value))
        # the busy()? will be called within 10ms but the wheel will not yet start moving
        # so we need to block busy() with 10ms buffer after setter is called
        
    def busy(self):
        if self.pfilter.IsMoving or (time.time()*1000 - self.changed_time_ms) < 10: # or (time.time()*1000 - self.changed_time_ms) > 5000:
            return True
        else:
            return False
     


def filter_position_changed(sender: PiUsbNet.Filter, args: PiUsbNet.FilterPositionChangedEventArgs):
    print(f'Filter position: {args.Position}')

pifilter: PiUsbNet.Filter = PiUsbNet.Filter()
pifilter.PositionChanged += filter_position_changed
pifilter.Open(108)

device = GenericDevice(Color.Pos1, pifilter)
devices = {'picard_filter': device}
# no easy way to integrate PyDevice logging with Micro-Manager so we use temp file to write info into
with open('temp_pydevice_log.txt', 'a') as the_file:
    the_file.write(str(time.time() * 1000) + 'done loading\n')

if __name__ == "__main__":
    import sys
    import os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from bootstrap import PyDevice

    device = PyDevice(devices['picard_filter'])
    print(device)
    assert device.device_type == 'Device'