README
======

Write nice formatted report with good enough formating.

Install
-------

Usage
-----

Write your dataframe with sensible default. No question asked.

.. code:: python

   from ecrivain import xlsx

   xlsx.write(df,'mytable.xlsx')

If you want to have more control use ``autofit``

.. code:: python

   writer = autofit(data,path,sheetname='data',factor=1.1,threshold=250)
   writer.save()
