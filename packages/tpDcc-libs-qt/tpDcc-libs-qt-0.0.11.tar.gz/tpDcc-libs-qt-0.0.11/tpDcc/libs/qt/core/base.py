#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains base functionality for Qt widgets
"""

from __future__ import print_function, division, absolute_import

from Qt.QtCore import *
from Qt.QtWidgets import *

from tpDcc.libs.qt.core import qtutils, mixin, theme


@mixin.theme_mixin
@mixin.cursor_mixin
class BaseWidget(QWidget, object):
    """
    Base class for all QWidgets based items
    """

    def_use_scrollbar = False

    def __init__(self, parent=None, **kwargs):
        super(BaseWidget, self).__init__(parent=parent)

        self._size = self.theme_default_size()

        self._use_scrollbar = kwargs.get('use_scrollbar', self.def_use_scrollbar)

        self.ui()
        self.setup_signals()

    # =================================================================================================================
    # PROPERTIES
    # =================================================================================================================

    def _get_size(self):
        """
        Returns the spin box height size
        :return: float
        """

        return self._size

    def _set_size(self, value):
        """
        Sets spin box height size
        :param value: float
        """

        self._size = value
        self.style().polish(self)

    theme_size = Property(int, _get_size, _set_size)

    # =================================================================================================================
    # OVERRIDES
    # =================================================================================================================

    def keyPressEvent(self, event):
        return

    def mousePressEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.AltModifier:
            pos = self.mapToGlobal((self.rect().topLeft()))
            QWhatsThis.showText(pos, self.whatsThis())
        else:
            super(BaseWidget, self).mousePressEvent(event)

    # =================================================================================================================
    # BASE
    # =================================================================================================================

    def get_main_layout(self):
        """
        Function that generates the main layout used by the widget
        Override if necessary on new widgets
        :return: QLayout
        """

        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)
        layout.setAlignment(Qt.AlignTop)
        return layout

    def ui(self):
        """
        Function that sets up the ui of the widget
        Override it on new widgets (but always call super)
        """

        self.main_layout = self.get_main_layout()
        if self._use_scrollbar:
            layout = QVBoxLayout()
            self.setLayout(layout)
            central_widget = QWidget()
            central_widget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
            scroll = QScrollArea()
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scroll.setWidgetResizable(True)
            scroll.setFocusPolicy(Qt.NoFocus)
            layout.addWidget(scroll)
            scroll.setWidget(central_widget)
            central_widget.setLayout(self.main_layout)
            self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        else:
            self.setLayout(self.main_layout)

    def setup_signals(self):
        """
        Function that set up signals of the widget
        """

        pass

    def set_spacing(self, value):
        """
        Set the spacing used by widget's main layout
        :param value: float
        """

        self.main_layout.setSpacing(value)

    def tiny(self):
        """
        Sets spin box to tiny size
        """

        widget_theme = self.theme()
        self.theme_size = widget_theme.tiny if widget_theme else theme.Theme.Sizes.TINY

        return self

    def small(self):
        """
        Sets spin box to small size
        """

        widget_theme = self.theme()
        self.theme_size = widget_theme.small if widget_theme else theme.Theme.Sizes.SMALL

        return self

    def medium(self):
        """
        Sets spin box to medium size
        """

        widget_theme = self.theme()
        self.theme_size = widget_theme.medium if widget_theme else theme.Theme.Sizes.MEDIUM

        return self

    def large(self):
        """
        Sets spin box to large size
        """

        widget_theme = self.theme()
        self.theme_size = widget_theme.large if widget_theme else theme.Theme.Sizes.LARGE

        return self

    def huge(self):
        """
        Sets spin box to huge size
        """

        widget_theme = self.theme()
        self.theme_size = widget_theme.huge if widget_theme else theme.Theme.Sizes.HUGE

        return self


class BaseFrame(QFrame, object):
    mouseReleased = Signal(object)

    def __init__(self, *args, **kwargs):
        super(BaseFrame, self).__init__(*args, **kwargs)

    def mouseReleaseEvent(self, event):
        self.mouseReleased.emit(event)
        return super(BaseFrame, self).mouseReleaseEvent(event)


class ContainerWidget(QWidget, object):
    """
    Basic widget used a
    """

    def __init__(self, parent=None):
        super(ContainerWidget, self).__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        self.containedWidget = None

    def set_contained_widget(self, widget):
        """
        Sets the current contained widget for this container
        :param widget: QWidget
        """

        self.containedWidget = widget
        if widget:
            widget.setParent(self)
            self.layout().addWidget(widget)

    def clone_and_pass_contained_widget(self):
        """
        Returns a clone of this ContainerWidget
        :return: ContainerWidget
        """

        cloned = ContainerWidget(self.parent())
        cloned.set_contained_widget(self.containedWidget)
        self.set_contained_widget(None)
        return cloned


class BaseNumberWidget(BaseWidget, object):
    valueChanged = Signal(object)

    def __init__(self, name='', parent=None):
        self._name = name
        super(BaseNumberWidget, self).__init__(parent)

    def get_main_layout(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        return main_layout

    def ui(self):
        super(BaseNumberWidget, self).ui()

        self._number_widget = self.get_number_widget()
        self._number_label = QLabel(self._name, parent=self)
        if not self._name:
            self._number_label.hide()
        self._value_label = QLabel('value', parent=self)
        self._value_label.hide()

        self.main_layout.addWidget(self._number_label)
        self.main_layout.addSpacing(5)
        self.main_layout.addWidget(self._value_label, alignment=Qt.AlignRight)
        self.main_layout.addWidget(self._number_widget)

    def get_number_widget(self):
        """
        Returns the widget used to edit numeric value
        :return: QWidget
        """

        spin_box = QSpinBox(parent=self)
        spin_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return spin_box

    def get_value(self):
        """
        Returns the number value of the numeric widget
        :return: variant, int || float
        """

        return self._number_widget.value()

    def set_value(self, new_value):
        """
        Sets the value of the numeric widget
        :param new_value: variant, int || float
        """

        if new_value:
            self._number_widget.setValue(new_value)

    def get_label_text(self):
        return self._number_label.text()

    def set_label_text(self, new_text):
        self._number_label.setText(new_text)

    def set_value_label(self, new_value):
        self._value_label.show()
        self._value_label.setText(str(new_value))

    def _on_value_changed(self):
        self.valueChanged.emit(self.get_value())


class DirectoryWidget(BaseWidget, object):
    """
    Widget that contains variables to store current working directory
    """

    def __init__(self, parent=None, **kwargs):
        self.directory = None
        self.last_directory = None
        super(DirectoryWidget, self).__init__(parent=parent, **kwargs)

    def set_directory(self, directory):
        """
        Set the directory used by this widget
        :param directory: str, new directory of the widget
        """

        self.last_directory = self.directory
        self.directory = directory


class PlaceholderWidget(QWidget, object):
    """
    Basic widget that loads custom UI
    """

    def __init__(self, *args):
        super(PlaceholderWidget, self).__init__(*args)
        qtutils.load_widget_ui(self)
