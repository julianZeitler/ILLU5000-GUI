Developer Guide
================

Generating `.mat` Files
------------------------

In order to be capable of generating the needed MATLAB data files, it is crucial
to understand the underlying data structure.

Creating Additional Plot Types
-------------------------------

Additional plot types can be added in the `DataAnalyzer.PlotConfig.PlotTypes`
package. A plot type module must have the following syntax:

.. code-block::

    plt_YourCustomPlotType

And the class name must then be:

.. code-block::

    YourCustomPlotType

Typically each plot type inherits its `__init__` method from the `plot_Base` module,
which contains the :ref:`Base <plt_base>` class. The most basic configuration is taken there.