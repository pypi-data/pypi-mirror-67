# Colabext : Some Extended convenient utilities 

## What is this about? 

This contains common style you can use for your notebook similar to Google CO-LABS

## How to use it

```
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

pip install colabexts
```
and load this in your browser


## In your notebook

```
%reload_ext autoreload
%autoreload 2
import colabexts
from colabexts.jcommon import *

jpath=os.path.dirname(colabexts.__file__)
jcom = f'{jpath}/jcommon.ipynb'
%run $jcom

```