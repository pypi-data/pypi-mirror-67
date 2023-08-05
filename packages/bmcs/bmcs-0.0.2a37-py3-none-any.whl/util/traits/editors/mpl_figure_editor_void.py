
from traitsui.wx.basic_editor_factory import BasicEditorFactory
from traitsui.wx.editor import Editor


class _MPLFigureEditor(Editor):

    def init(self, parent):
        pass

    def update_editor(self):
        pass


class MPLFigureEditor(BasicEditorFactory):

    klass = _MPLFigureEditor
