# README

Write nice formatted report with good enough formating.

## Install

## Usage

Write your dataframe with sensible default. No question asked.

```python
from ecrivain import xlsx

xlsx.write_excel(df,'mytable.xlsx')
```

If you want to have more control use `autofit`

```python
writer = autofit(data,path,sheetname='data',factor=1.1,threshold=250)
writer.save()
```

