Developer Guide
================

Generating `.mat` Files
------------------------

In order to be capable of generating the needed MATLAB data files, it is crucial
to understand the underlying data structure.

Creating Additional Plot Types
-------------------------------

Additional plot types can be added in the :ref:`DataAnalyzer.PlotConfig.PlotTypes <plottypes>`
package. A plot type module must have the following syntax:

.. code-block:: python

    plt_YourCustomPlotType.py

And the contained class's name must then be:

.. code-block:: python

    YourCustomPlotType

Typically each plot type inherits its `__init__` method from the `plot_Base` module,
which contains the :ref:`Base <plt_base>` class. The most basic configuration is taken there.

Additionally plot types that have a very basic configuration can inherit the `plot` method from the
:ref:`DataAnalyzer.PlotConfig.TwoD.plt_TwoD <plt_twod>` module.

You can however define the constructor and `plot` methods yourself. You have to minimally include these two methods,
because they get called by the program.

.. warning::
    Watch out that you take all possible configuration arguments in
    the `__init__` method, or else an error will be thrown

The `plot` method is required. If you define it yourself, make sure it takes two additional arguments,
because the program will call it that way.
The first argument gets assigned a Matplotlib axes object, which can be understood as a subplot. By changing it's
properties, the subplot can be customized. The second argument will be an object of
`DataAnalyzer.Data.cl_data.FileData.plot_data.Data`
which contains the actual plotting data (:ref:`reference <cl_data>`). You will have to index it with the correct
name. The following is the `plot` method from :ref:`DataAnalyzer.PlotConfig.TwoD.plt_TwoD <plt_twod>` module.

.. code-block:: python

    def plot(self, ax, data):
        if not isinstance(self.plots[0], list):
            self.plots = [self.plots]

        for plot in self.plots:
            ax.plot(asarray(data[plot[0].strip()].values),
                    asarray(data[plot[1].strip()].values),
                    label=data[plot[1].strip()].name)

        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.set_title(self.title)
        ax.legend(loc=self.legend)
        ax.grid(self.grid)

        try:
            self.plot_specific(ax)
        except AttributeError:
            pass

The `plot` method is responsible for plotting the data onto the axes object that was created before.
As you can see, `plot` tries to call the function `self.plot_specific`, which can be defined by the child class of it.
That way you would not need to define the whole `plot` method, but could just add the parameters you were missing.