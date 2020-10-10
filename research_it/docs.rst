Reading one column of data for a specified time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function ``pp.get_data_by_time(path, columns, dates, start_time="00:00", end_time="23:59")`` extracts data from a ProCoDA data log based on the `path` (folder in your computer) the file is located in, the `columns` you wish to extract, the `dates` of the experiment (a single date or a list of consecutive dates), and the optional `start_time` and `end_date`. The `columns` input can be a single integer if you want to extract one column, or it can be a list of integers if you want to extract multiple columns. Note: the 0<sup>th</sup> column of a ProCoDA datalog is the time column.

The output is either

1. a list of numbers (for a single column of data), or
2. a list of lists of numbers (for multiple columns of data, in the order specified in the `columns` input)

.. Therefore, if we want to graph it, we can pass it directly to the ``plot()`` function from ``matplotlib.pyplot`` (see sections [III](#plotting-with-matplotlib-one-y-axis) and [IV](#plotting-with-matplotlib-two-y-axes)).

Here is an example that uses `get_data_by_time` to extract data from one column, for one day, and for specified start and end times.

.. code-block:: python

    import aguaclara.research.procoda_parser as pp

    data_path = "Data"
    column = pp.get_data_by_time(path=data_path, columns=4,
                                 dates="6-14-2018", start_time="15:40",
                                 end_time="23:30")
    print(column)


Reading multiple columns of data for a specified time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here is another example that uses `get_data_by_time()` again to extract three columns (which happen to represent time, influent turbidity, and effluent turbidity) of data over the entirety of two days (since no start or end times are specified).

.. code-block:: python

    import aguaclara.research.procoda_parser as pp

    data_path = "Data"
    columns = pp.get_data_by_time(path=data_path, columns=[0, 3, 4],
                                  dates=["6-14-2018", "6-15-2018"])
    # columns is now a list of 3 elements, each of which is also a list:

    # 1. a list of times (from the 0th column)
    time = columns[0]
    # 2. a list of influent turbidity values (from the 3rd column)
    influent_turbidity = columns[1]
    # 3. a list of effluent turbidity values (from the 4th column)
    effluent_turbidity = columns[2]

Reading one column of data for a specified STATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The function ``pp.get_data_by_state(path, dates, state, column)`` extracts data from a ProCoDA datalog based on the `path` (folder in your computer) the file is located in, the `dates` of the experiment (input as a list of one or more dates), the `state` of ProCoDA during which you collected your data of interest (this is an integer), and the `column` of the data that you want to extract. *Note that the 0<sup>th</sup> column of a ProCoDA datalog is the time column.*

The output of the function is a 3-dimension list (list of lists of lists), where the "smallest" lists are lists of time and data (from your desired column) from the ProCoDA datalog, the next level of lists contains contains time and data column pairs (one for each  iteration of your state), and the top level of lists contains these lists for each iteration.

Here is an example that uses `get_data_by_time` to extract and make simple calculations on data from a particular ProCoDA state.

.. code-block:: python

    import aguaclara.research.procoda_parser as pp

    data_path = "Data"
    data = pp.get_data_by_state(data_path, dates="6-19-2013", state=1, column=1)

    # This empty list will be used later to hold the average pH reading from
    # each iteration of the 1st state
    pH_averages = []

    for iteration in data:
      # Here's how to extract time from the output:
      time = iteration[:,0]
      elapsed_time = time - iteration[0,0]

      # Here's a way to extract and work with data from the output:
      pH_readings = iteration[:,1]
      pH_averages.append(sum(pH_readings)/len(pH_readings))

    print(pH_averages)
