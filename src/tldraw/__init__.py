import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("tldraw")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class TldrawWidget(anywidget.AnyWidget):
    width = traitlets.Int(600).tag(sync=True)
    height = traitlets.Int(300).tag(sync=True)

    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    _css = pathlib.Path(__file__).parent / "static" / "widget.css"
    value = traitlets.Int(0).tag(sync=True)




class TldrawImage(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "image.js"
    _css = pathlib.Path(__file__).parent / "static" / "image.css"
    value = traitlets.Int(0).tag(sync=True)
