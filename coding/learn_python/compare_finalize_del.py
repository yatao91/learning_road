# -*- coding: utf-8 -*-
import tempfile
import shutil


# __del__形式
# class TempDir:
#     def __index__(self):
#         self.name = tempfile.mkdtemp()
#
#     def remove(self):
#         if self.name is not None:
#             shutil.rmtree(self.name)
#             self.name = None
#
#     @property
#     def removed(self):
#         return self.name is None
#
#     def __del__(self):
#         self.remove()

# finalize形式
import weakref


class TempDir:
    def __index__(self):
        self.name = tempfile.mkdtemp()
        self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

    def remove(self):
        self._finalizer()

    @property
    def removed(self):
        return not self._finalizer.alive
