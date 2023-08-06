from itertools import cycle
from typing import Callable, Dict, Sequence, Tuple

from PyQt5.QtCore import pyqtSignal, QObject, QRectF, QTimer, QUrl
from PyQt5.QtGui import QPainter, QPicture, QTextCharFormat
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QLabel, QLineEdit, QSlider

from .widgets import HyperlinkTextBrowser, PictureWidget


class DisplayPageData:
    """ Data class that contains HTML formatted graphs, a caption, an SVG board, and a link reference. """

    def __init__(self, html_graphs:Sequence[str]=("", ""), board_caption="", board_xml=b"", link_ref="") -> None:
        self.html_graphs = html_graphs      # Sequence of 2 HTML text graphs for this rule: [normal, bright].
        self.board_caption = board_caption  # Text caption for this rule, drawn above the board.
        self.board_xml = board_xml          # XML byte string containing this rule's SVG board diagram.
        self.link_ref = link_ref            # Target ref for a link to find examples of this rule (empty if none).


class DisplayPageDict(Dict[str, DisplayPageData]):
    """ Contains HTML formatted graphs, captions, and SVG boards for each rule in an analysis. """

    DEFAULT_KEY = "_DEFAULT"  # Key for default page (nothing selected).


class SVGPictureRenderer:
    """ Renders SVG bytes data on QPictures. """

    def __init__(self, *, render_hints=QPainter.Antialiasing) -> None:
        self._renderer = QSvgRenderer()    # XML SVG renderer.
        self._render_hints = render_hints  # SVG rendering quality hints (such as anti-aliasing).

    def set_data(self, xml_data=b"") -> None:
        """ Load the renderer with raw XML data containing the SVG elements to draw. """
        self._renderer.load(xml_data)

    def render_fit(self, width:float, height:float) -> QPicture:
        """ Render the current SVG elements on a new picture of size <width, height> and return it. """
        gfx = QPicture()
        with QPainter(gfx) as p:
            p.setRenderHints(self._render_hints)
            bounds = self._fit_bounds(width, height)
            self._renderer.render(p, bounds)
        return gfx

    def _fit_bounds(self, width:float, height:float) -> QRectF:
        """ Return the bounding box needed to center everything in the picture at maximum scale. """
        _, _, vw, vh = self._renderer.viewBoxF().getRect()
        if vw and vh:
            scale = min(width / vw, height / vh)
            fw, fh = vw * scale, vh * scale
            ox = (width - fw) / 2
            oy = (height - fh) / 2
            return QRectF(ox, oy, fw, fh)
        else:
            # If no valid viewbox is defined, use the given size directly.
            return QRectF(0, 0, width, height)


class _TitleWrapper(QObject):
    """ Wrapper for title bar widget that displays translations as well as loading/status with simple text animations.
        Also allows manual lexer queries by editing translations directly. """

    _sig_user_translation = pyqtSignal([str, str])  # Sent on a user edit that produces a valid translation.

    def __init__(self, w_title:QLineEdit, *, tr_delim=" -> ") -> None:
        super().__init__()
        self._w_title = w_title
        self._tr_delim = tr_delim        # Delimiter between keys and letters of translations shown in title bar.
        self._anim_timer = QTimer(self)  # Animation timer for loading messages.
        self.call_on_translation = self._sig_user_translation.connect
        w_title.textEdited.connect(self._on_edit_text)

    def _on_edit_text(self, text:str) -> None:
        """ Parse the title bar text as a translation and send the signal if it is valid and non-empty. """
        parts = text.split(self._tr_delim)
        if len(parts) == 2:
            keys, letters = [p.strip() for p in parts]
            if keys and letters:
                self._sig_user_translation.emit(keys, letters)

    def set_enabled(self, enabled:bool) -> None:
        """ The title bar should be set read-only instead of disabled to continue showing status messages. """
        self._w_title.setReadOnly(not enabled)

    def show_status(self, text:str) -> None:
        """ Check if the status text ends in an ellipsis. If not, just show the text normally.
            Otherwise, animate the text with a • dot moving down the ellipsis until new text is shown:
            loading...  ->  loading•..  ->  loading.•.  ->  loading..• """
        if text.endswith("..."):
            body = text.rstrip(".")
            frames = [body + b for b in ("...", "•..", ".•.", "..•")]
            self._set_animated_text(frames, 200)
        else:
            self._set_static_text(text)

    def show_translation(self, keys:str, letters:str) -> None:
        """ Format a translation and show it in the title bar. """
        translation = [keys, letters]
        tr_text = self._tr_delim.join(translation)
        self._set_static_text(tr_text)

    def show_traceback_heading(self) -> None:
        """ Display a stack traceback heading. """
        self._set_static_text("Well, this is embarrassing...")

    def _set_static_text(self, text:str) -> None:
        """ Stop any animation and show normal text in the title bar. """
        self._anim_timer.stop()
        self._w_title.setText(text)

    def _set_animated_text(self, text_items:Sequence[str], delay_ms:int) -> None:
        """ Set the widget text to animate over <text_items> on a timed cycle.
            The first item is shown immediately, then a new one is shown every <delay_ms> milliseconds. """
        if text_items:
            show_next_item = map(self._w_title.setText, cycle(text_items)).__next__
            show_next_item()
            self._anim_timer.timeout.connect(show_next_item)
            self._anim_timer.start(delay_ms)


class _GraphWrapper(QObject):
    """ Formatted text widget for displaying a monospaced HTML graph of the breakdown of text by steno rules.
        May also display plaintext output such as error messages and exceptions when necessary. """

    _sig_mouse_over = pyqtSignal([str])   # Sent with a node reference when the mouse moves over a new one.
    _sig_mouse_click = pyqtSignal([str])  # Sent with a node reference when the mouse clicks one.

    def __init__(self, w_graph:HyperlinkTextBrowser) -> None:
        super().__init__()
        self._w_graph = w_graph
        self._mouse_enabled = False  # If True, all graph mouse actions are disabled.
        self._has_focus = False      # If True, freeze focus on the current page and do not allow mouseover signals.
        self.call_on_mouse_over = self._sig_mouse_over.connect
        self.call_on_mouse_click = self._sig_mouse_click.connect
        w_graph.linkOver.connect(self._on_link_over)
        w_graph.linkClicked.connect(self._on_link_click)

    def _on_link_over(self, url:QUrl) -> None:
        """ If the graph is enabled, send a signal with the fragment string of the URL under the cursor.
            When we move off of a link, this will be sent with an empty string.
            Do not allow mouseover signals if focus is active. """
        if self._mouse_enabled and not self._has_focus:
            self._sig_mouse_over.emit(url.fragment())

    def _on_link_click(self, url:QUrl) -> None:
        """ If the graph is enabled, send a signal with the fragment string of the clicked URL.
            When we click something that isn't a link, this will be sent with an empty string. """
        if self._mouse_enabled:
            self._sig_mouse_click.emit(url.fragment())

    def set_enabled(self, enabled:bool) -> None:
        self._w_graph.setEnabled(enabled)

    def set_focus(self, enabled=False) -> None:
        """ Set the focus state of the graph. Mouseover signals will be suppressed when focus is active. """
        self._has_focus = enabled

    def set_graph_text(self, text:str) -> None:
        """ Enable graph interaction and replace the current text with new HTML formatted graph text. """
        self._mouse_enabled = True
        self._w_graph.setHtml(text, no_scroll=True)

    def set_plaintext(self, text:str) -> None:
        """ Disable graph interaction and replace the current text with new plaintext. """
        self._mouse_enabled = False
        self._w_graph.clear()
        self._w_graph.setCurrentCharFormat(QTextCharFormat())
        self._w_graph.append(text)


class _BoardWrapper(QObject):
    """ Displays all of the keys that make up one or more steno strokes pictorally. """

    _LINK_HTML = "<a href='dummy'>More Examples</a>"

    _sig_new_ratio = pyqtSignal([float])  # Sent with the width / height aspect ratio of the board widget.

    def __init__(self, w_board:PictureWidget, w_link:QLabel, renderer:SVGPictureRenderer) -> None:
        super().__init__()
        self._w_board = w_board    # Board diagram container widget.
        self._w_link = w_link      # Rule example hyperlink.
        self._renderer = renderer  # XML SVG renderer.
        self.call_on_link_click = self._w_link.linkActivated.connect
        self.call_on_ratio_change = self._sig_new_ratio.connect
        w_link.setText(self._LINK_HTML)
        w_link.setVisible(False)
        w_board.resized.connect(self._on_resize)

    def _on_resize(self) -> None:
        """ Reposition the link and redraw the board on any size change. """
        width, height = self._get_size()
        self._w_link.move(width - 75, height - 18)
        self._draw_board()
        self._sig_new_ratio.emit(width / height)

    def set_link_visible(self, visible=True) -> None:
        """ Show the link in the bottom-right corner of the diagram if examples exist. """
        self._w_link.setVisible(visible)

    def set_data(self, xml_data=b"") -> None:
        """ Load the renderer with new SVG data and redraw the board. """
        self._renderer.set_data(xml_data)
        self._draw_board()

    def get_ratio(self) -> float:
        """ Return the width / height aspect ratio of the board widget. """
        width, height = self._get_size()
        return width / height

    def _get_size(self) -> Tuple[float, float]:
        """ Return the size of the board widget. """
        return self._w_board.width(), self._w_board.height()

    def _draw_board(self) -> None:
        """ Render the diagram on a new picture and immediately repaint the board. """
        width, height = self._get_size()
        gfx = self._renderer.render_fit(width, height)
        self._w_board.setPicture(gfx)


class _CaptionWrapper:

    def __init__(self, w_caption:QLabel) -> None:
        self._w_caption = w_caption  # Label with caption containing rule keys/letters/description.

    def set_caption(self, caption="") -> None:
        """ Show a caption above the board diagram. """
        self._w_caption.setText(caption)


class _OptionSliderWrapper:

    def __init__(self, w_slider:QLabel) -> None:
        self._w_slider = w_slider  # Slider to control board rendering options.
        self.set_enabled = w_slider.setEnabled
        self.call_on_change = w_slider.valueChanged.connect

    def is_mode_compound(self) -> bool:
        """ The board is compound if not in keys mode (left value, 0). """
        return self._w_slider.value() > 0

    def is_mode_letters(self) -> bool:
        """ The board uses letters only if in letters mode (right value, 2). """
        return self._w_slider.value() > 1


class DisplayController:

    def __init__(self, title:_TitleWrapper, graph:_GraphWrapper, board:_BoardWrapper,
                 caption:_CaptionWrapper, slider:_OptionSliderWrapper) -> None:
        self._title = title
        self._graph = graph
        self._board = board
        self._caption = caption
        self._slider = slider
        self._page_dict = DisplayPageDict()
        self._last_link_ref = ""
        self._last_translation = None
        self._on_example_search = lambda *_: None
        self._on_query = lambda *_: None
        graph.call_on_mouse_over(self._graph_over)
        graph.call_on_mouse_click(self._graph_clicked)
        title.call_on_translation(self._send_query)
        board.call_on_link_click(self._send_example_search)
        slider.call_on_change(self._slider_action)
        self.get_board_ratio = board.get_ratio
        self.get_board_compound = slider.is_mode_compound
        self.get_board_letters = slider.is_mode_letters
        self.set_status = title.show_status

    def call_on_query(self, fn:Callable[[Tuple[str, str]], None]) -> None:
        self._on_query = fn

    def call_on_example_search(self, fn:Callable[[str], None]) -> None:
        self._on_example_search = fn

    def _send_query(self, keys:str, letters:str) -> None:
        self._on_query([keys, letters])

    def _send_example_search(self, *_) -> None:
        self._on_example_search(self._last_link_ref)

    def _slider_action(self, *_) -> None:
        """ On slider actions, resend the last query to get pages rendered with the new options. """
        translation = self._last_translation
        if translation is not None:
            self._on_query(translation)

    def _graph_over(self, node_ref:str) -> None:
        self._graph_action(node_ref, False)

    def _graph_clicked(self, node_ref:str) -> None:
        self._graph_action(node_ref, True)

    def _graph_action(self, node_ref:str, focused:bool) -> None:
        """ On mouse actions, change the current analysis page to the one under <node_ref>.
            If <node_ref> is an empty string, show the default page with nothing focused. """
        if not node_ref:
            focused = False
            node_ref = DisplayPageDict.DEFAULT_KEY
        page = self._page_dict.get(node_ref)
        if page is not None:
            self._set_page_active(page, focused)

    def _set_page_active(self, page=DisplayPageData(), focused=False) -> None:
        """ Change the currently displayed analysis page and set its focus state. Call with no args to clear it. """
        self._graph.set_graph_text(page.html_graphs[focused])
        self._graph.set_focus(focused)
        self._caption.set_caption(page.board_caption)
        self._board.set_data(page.board_xml)
        self._board.set_link_visible(bool(page.link_ref))
        self._last_link_ref = page.link_ref

    def set_translation(self, keys:str, letters:str) -> None:
        self._last_translation = [keys, letters]
        self._title.show_translation(keys, letters)

    def set_pages(self, page_dict:DisplayPageDict) -> None:
        """ Replace the current dict of analysis pages and attempt to select the last link target. """
        self._page_dict = page_dict
        last_link = self._last_link_ref
        start_ref = ""
        if last_link:
            for node_ref, page in page_dict.items():
                if page.link_ref == last_link:
                    start_ref = node_ref
                    break
        self._graph_action(start_ref, True)

    def set_enabled(self, enabled:bool) -> None:
        """ Enable/disable all display widgets. Invalidate the current graph and board on disable. """
        if not enabled:
            self._set_page_active()
            self._graph.set_plaintext("")
        self._title.set_enabled(enabled)
        self._graph.set_enabled(enabled)
        self._slider.set_enabled(enabled)

    def show_traceback(self, tb_text:str) -> None:
        """ Display a stack trace. """
        self._title.show_traceback_heading()
        self._graph.set_plaintext(tb_text)

    @classmethod
    def from_widgets(cls, w_title:QLineEdit, w_graph:HyperlinkTextBrowser, w_board:PictureWidget,
                     w_caption:QLabel, w_slider:QSlider) -> "DisplayController":
        title = _TitleWrapper(w_title)
        graph = _GraphWrapper(w_graph)
        w_link = QLabel(w_board)
        board_renderer = SVGPictureRenderer()
        board = _BoardWrapper(w_board, w_link, board_renderer)
        caption = _CaptionWrapper(w_caption)
        slider = _OptionSliderWrapper(w_slider)
        return cls(title, graph, board, caption, slider)
