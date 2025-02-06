# picardfw-pydevice
pyDevice micro-manager adapter for [Picard filter wheel](https://picardindustries.com/products/optical-devices/usb-filter-wheel/)

Based on [pyDevice](https://github.com/micro-manager/mmCoreAndDevices/tree/main/DeviceAdapters/PyDevice)

Requires installation of Picard filterwheel software; copy following DLLs from Picard SDK folder in the same folder with the script:
- PiUsb.dll
- PiUsbNet.dll
- PiUsbNet.xml

Requires installation of `pip install pythonnet` library (in main or venv)

Haven't tested with venv

Andrey Andreev, aandreev@emila.org
(c) Ellison Institute 2025
