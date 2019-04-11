# qt_installer

Install dependencies
```bash
$ apt install python3 p7zip-full wget
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

Install Qt
```bash
$ ./qt_installer.py -v 5.12.2 -m qtwebengine
```

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
