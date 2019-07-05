# Qt installer

Installation tool for [Qt](https://www.qt.io/).

## Getting Started

These instruction will get you a copy of the project up and running on your local machine for development purposes.

### Prerequisites

Install dependencies
```bash
$ apt install python3 p7zip-full wget
```

Clone repo:
```bash
$ git clone https://github.com/g-konst/qt_installer && cd qt_installer
```

Make virtualenv and install python requirement
```bash
$ virtualenv --python=python3 --no-site-packages venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Allow script execution
```bash
$ chmod +x qt_installer.py
```

### Install Qt

To install Qt on your local machine, use the following command:
```bash
$ ./qt_installer.py -v 5.12.2 -m qtwebengine
```

Use `help` command to see available arguments:
```bash
$ ./qt_installer.py --help
usage: qt_installer.py [-h] -v VERSION [-m MODULES]

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION
                        Qt version <Required>
  -m MODULES, --modules MODULES
                        Modules to install
```
#### Notes:
- If the `VERSION` is without a patch value, it should be `0`, e.g.: `5.13.0`.
- `MODULES` value can be passed miltiple times to install additional modules:
  ```bash
  $ ./qt_installer.py -v 5.12.2 -m qtwebengine -m qtnetworkauth
  ```

Available modules for installation:
```
gcc_64 (default)              - Prebuilt Components for Desktop gcc 64-bit
debug_info                    - Desktop gcc 64-bit Debug Information Files
qtcharts          [LGPL v3]   - The Qt Charts API lets you easily create interactive and dynamic 2D charts
                                using C++ and/or Qt Quick.
qtdatavis3d       [LGPL v3]   - Qt Data Visualization is a module which provides a way to visualize data
                                in 3D. There are C++ classes and QML types for displaying bar graphs, 
                                scatter graphs, surface graphs and ways of manipulating the 3D scene. In 
                                addition, the graphs are fully customizable with different themes.
qtnetworkauth                 - Qt Network Authorization is an add-on library that enables Qt applications
                                to use different web authentication systems.
qtpurchasing                  - Qt Purchasing. Cross-platform APIs for handling in-app purchases on 
                                Android, iOS and macOS.
qtscript          [LGPL v2.0] - Qt Script (Deprecated) Prebuilt Components.
qtvirtualkeyboard [LGPL v3]   - The Qt Virtual Keyboard is a Qt Quick virtual keyboard that you can plug
                                in to your platform or application. You can extend it with your own 
                                layouts and styles.
qtwebengine       [LGPL v2.1] - The Qt WebEngine module integrates the fast moving Chromium web platform
                                into Qt and provides a convenient API for both Qt Widgets and Qt Quick to
                                utilize Chromium's web capabilities. Qt WebEngine takes full benefit of 
                                the whole Qt graphics stack integration allowing seamless mix and overlay
                                of native Qt controls with web content and OpenGL shaders.
qtwebplugin       [LGPL v3]   - The Qt WebGL Streaming Plugin is a Qt Platform Abstraction plugin which 
                                provides streaming of Qt Quick & Qt OpenGL applications over the network
                                to a WebGL capable browser.
```

### After installation
You also need to add `qt.conf` to your application folder.
```ini
[Paths]
Prefix = <PATH_TO_QT>
Documentation = doc
Headers = include
Libraries = lib
LibraryExecutables = libexec
Binaries = bin
Plugins = plugins
Imports = imports
Qml2Imports = qml
ArchData = .
Data = .
Translations = translations
Examples = examples
Tests = tests
Settings = .
```
