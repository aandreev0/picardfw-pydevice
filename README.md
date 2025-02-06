# Picard Filterwheel pyDevice adapter for Micro-Manager 
pyDevice micro-manager adapter for [Picard filter wheel](https://picardindustries.com/products/optical-devices/usb-filter-wheel/)

![picard filter wheel](https://github.com/user-attachments/assets/12e6140c-92a9-4ca5-ab08-eea1db585683)


Based on [pyDevice](https://github.com/micro-manager/mmCoreAndDevices/tree/main/DeviceAdapters/PyDevice)

Tested in nightly build MM 2.0.3 20250129, Device API 71, MMCore 11.3.0

Requires installation of Picard filterwheel software; copy following DLLs from Picard SDK folder in the same folder with the script:
- PiUsb.dll
- PiUsbNet.dll
- PiUsbNet.xml

Requires installation of `pip install pythonnet` library (in main or venv)

Haven't tested with venv

Andrey Andreev, aandreev@emila.org
(c) Ellison Institute 2025
