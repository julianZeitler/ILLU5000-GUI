from plt_base import Base


class LinLog(Base):
    def __init__(self,
                 foo='foo',
                 *args,
                 **kwargs):

        super().__init__(*args, **kwargs)
        self.foo = foo

    def plot(self, plots):
        pass
