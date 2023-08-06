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

## Paper 
Right now the paper isn't it's own object but a dict which contains the following:

- ```paper_id```: the id of the paper
- ```metadata```: contains data about the paper such as the journal title, dates, and authors 
- ```abstract```: abstract of the paper 
- ```body_text```: text of the paper 
- ```bib_enteries```: bibliography
- ```ref_enteries```: references
- ```back_matter```: more meta data like funding, conflict of interest statements etc
