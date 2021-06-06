
# Open Problem Bank - Physics

This repository is a bare-bones demo of how to create problems in PrairieLearn using a single markdown file (plus any images or assets that are needed).

## Installation 

It is recommended that you clone this repository locally first using the Terminal (For Windows, [GitBash](https://gitforwindows.org) is recommended):

```bash 
git clone https://github.com/open-resources/question_creation_demo.git
```

Then you will need to install the `problem_bank_scripts` python package using `pip`:

```bash 
pip install problem_bank_scripts
```

In case you had an older version of this package installed (it is being actively developed and things are changing FAST), you can upgrade it instead:

```bash
pip install problem_bank_scripts --upgrade
```

To convert one of the sample markdown files to the PrairieLearn syntax, open a Jupyter notebook or Lab session (or just use the provided [`demo.ipynb`](demo.ipynb) file) and run this in a cell:

```bash
import problem_bank_scripts as pbs
import pathlib

# Path to the input file (change for different questions)
pathstr = 'input_md/q01_multiple-choice/q01_multiple-choice.md'

# Set the input and output paths (no need to change)
input_path = pathlib.Path(pathstr)
output_path= pathlib.Path(pathstr.replace('input_md','output_pl'))

# Convert from markdown to PL
pbs.process_question(input_path, output_path)
```
## Demo

There is a [`demo.ipynb`](demo.ipynb) provided to show you the expected usage of the package.
 
## Known Limitations

- Currently, images are not supported, is the top priority!
- Currently, only the generate function is handled, will be adding support for this soon.
 
## FAQ

#### Will there be more problem types supported soon?

Yes, I hope so! Contributions are welcome.

#### Will it be possible to add functionality to support the other functions (other than generate) in `server.py` ?

Yes absolutely, will be done in a mostly backward-compatible way.

## Acknowledgements

 - Support from BC Campus
 - UBC Okanagan Provost's office
  