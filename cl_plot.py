import matplotlib.pyplot as plt


class Plot:
    def __init__(self, data, config, meta, plot):
        self.data = data        # dictionary
        self.config = config    # dictionary
        self.meta = meta        # object
        self.plot = plot        # string

    def create_figures(self):
        figs = [plt.figure(i) for i in range(len(self.config[self.plot]))]
        for fig in figs:
            self.create_subplots(fig)

    def create_subplots(self, fig):
        fi, ax = plt.subplots()

    def create_plots(self, plots):
        pass
