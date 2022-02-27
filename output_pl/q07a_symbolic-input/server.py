import random
import pandas as pd
import sympy as sp
import problem_bank_scripts.prairielearn as pl
import problem_bank_helpers as pbh
from collections import defaultdict
nested_dict = lambda: defaultdict(nested_dict)

def imports(data):
    import random
    import pandas as pd
    import sympy as sp
    import problem_bank_scripts.prairielearn as pl
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
    
def generate(data):
    # Start problem code
    
    data2 = nested_dict()
    
    # store phrases etc
    data2["params"]["vars"]["title"] = 'Centripetal Motion'
    
    # Declare math symbols to be used by sympy
    m, v, r = sp.symbols('m v r')
    
    # Describe the solution equation
    F = m*v**2/r
    
    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']['part1_ans'] = pl.to_json(F)
    
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
