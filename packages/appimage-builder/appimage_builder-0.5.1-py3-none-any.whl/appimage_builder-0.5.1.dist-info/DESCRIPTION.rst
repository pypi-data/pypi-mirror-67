# appimage-builder

`appimage-builder` allows packing applications along with all of its dependencies. It uses
traditional GNU/Linux software package tools like `apt` or `yum` to obtain binaries and resolve
dependencies creating a self-sufficient bundle. The embedded binaries are configured to be
relocatable and to interact with the rest. Finally, the whole bundle is compressed as a
`squashfs` filesystem and attached to a launcher binary using `appimagetool` making a
nice AppImage.

**Features**:
 - Recipe based.
 - Self-sufficient bundles.
 - Backward and forwards compatibility.
 - Cross bundling (don't confuse it with cross-compilation, that's out of the tool scope).
 - Basic license compliance (package license files will be bundled).
 - `apt` package manager support.
 - `yum` package manager support (experimental).



