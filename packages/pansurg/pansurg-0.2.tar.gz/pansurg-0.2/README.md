# Pansurg
Open source pip module that enables the user to access coronavirus resources. 

## Installation 

```
pip install pansurg 
```

# Papers 
All coronavirus papers from the Alan institute can be streamed using the ```Papers``` object which 
itself is a list. To get the papers run the following code"

```python
from pansurg import Papers


papers = Papers()

for paper in papers:
    # do something 
```

Initially, the papers are directly streamed from the Alan institute so this initializing the 
```Papers``` object might take a while. Once the first initialization is done, the papers are 
then saved onto your computer and are accessed locally from there onwards. This still takes 
some time to load as of the time of reading this there's over 2500 papers, but it's a lot 
shorter than directly streaming them from the Alan institute every time. The Alan institute 
updates the papers every friday, so it's advised that you refresh the cache once a week to 
get the latest papers. This can be done by setting the ```force_refresh``` parameter to ```True```:

```python
from pansurg import Papers


papers = Papers(force_refresh=True)
```

## Paper 
Right now the paper isn't it's own object but a dict which contains the following:

- ```paper_id```: the id of the paper
- ```metadata```: contains data about the paper such as the journal title, dates, and authors 
- ```abstract```: abstract of the paper 
- ```body_text```: text of the paper 
- ```bib_entries```: bibliography
- ```ref_entries```: references
- ```back_matter```: more meta data like funding, conflict of interest statements etc
