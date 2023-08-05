from splipy.io import G2

from .hdf5 import Log, GeometryManager


class SimpleBasis:

    def __init__(self, patches):
        self.patches = patches
        self.name = 'Geometry'

    @property
    def npatches(self):
        return len(self.patches)

    def update_at(self, stepid):
        return stepid == 0

    def patch_at(self, stepid, patchid):
        return self.patches[patchid]


class Reader:

    def __init__(self, filename, **kwargs):
        self.basis = None
        self.filename = filename

    def __enter__(self):
        with G2(self.filename) as g2:
            patches = g2.read()
        self.basis = SimpleBasis(patches)
        return self

    def __exit__(self, type_, value, backtrace):
        pass

    def write(self, w):
        w.add_step(time=0.0)
        geometry = GeometryManager(self.basis, self)
        geometry.update(w, 0)
        w.finalize_step()
