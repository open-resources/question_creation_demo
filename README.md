# Open Problem Bank - Physics

This repository is a bare-bones demo of how to create problems in PrairieLearn using a single markdown file (plus any images or assets that are needed).

## Installation 

1. It is recommended that you clone this repository locally first using the Terminal (For Windows, [GitBash](https://gitforwindows.org) is recommended):

```bash 
git clone https://github.com/open-resources/question_creation_demo.git
```

2. You will need to install the `problem_bank_scripts` and `problem_bank_helpers` python packages using `pip`:

```bash 
pip install problem_bank_scripts
pip install problem_bank_helpers
```

In case you had an older version of this package installed (it is being actively developed and things are changing FAST), you can upgrade it instead:

```bash
pip install problem_bank_scripts --upgrade
pip install problem_bank_helpers --upgrade

```

3. Download/copy the `problem_bank_helpers.py` file into the same directory you're running the notebook/python session from now. In the future, this will be integrated into `problem_bank_scripts`

4. To convert one of the sample markdown files to the PrairieLearn syntax, open a Jupyter notebook or Lab session (or just use the provided [`demo.ipynb`](demo.ipynb) file) and run this in a cell:

```bash
import problem_bank_scripts as pbs
import problem_bank_helpers as pbh
import pathlib

# Path to the input file (change for different questions)
pathstr = 'input_md/q01_multiple-choice/q01_multiple-choice.md'

# Set the input and output paths (no need to change)
input_path = pathlib.Path(pathstr)
output_path= pathlib.Path(pathstr.replace('input_md','output_pl')).parent

# Convert from markdown to PL
pbs.process_question_pl(input_path, output_path)
```
## Demo

There is a [`demo.ipynb`](demo.ipynb) provided to show you the expected usage of the package.
 
## Known Limitations

- Only the problem typess in the template are supported
- There are some weird LaTeX/Markdown rendering issues that we run into. Often using double `\` seems to resolve the issues. For e.g, use `\\frac{a}{b}` instead of `\frac{a}{b}`
 
## FAQ

#### Will there be more problem types supported soon?

Yes, I hope so! Contributions are welcome.

#### Will it be possible to add functionality to support the other functions (other than generate) in `server.py` ?

Yes absolutely, will be done in a mostly backward-compatible way.

## Acknowledgements

 - Support from BC Campus
 - UBC Okanagan Provost's office
  
