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
    
    # define or load names/items/objects
    names = pd.read_csv(data["options"]["client_files_course_path"]+"/data/names.csv")["Names"].tolist()
    vehicles = pd.read_csv(data["options"]["client_files_course_path"]+"/data/vehicles.csv")["Vehicles"].tolist()
    
    # store phrases etc
    data2["params"]["vars"]["title"] = 'Symbolic Input 2 - Trig'
    data2["params"]["vars"]["name"] = random.choice(names)
    data2["params"]["vars"]["vehicle"] = random.choice(vehicles)
    
    # Declare math symbols to be used by sympy
    mu_s, g , theta = sp.symbols('mu_s g theta')
    
    # Describe the solution equation
    amax = g*(mu_s*sp.cos(theta) - sp.sin(theta))
    
    # Answer to fill in the blank input -- must be stored as JSON.
    data2['correct_answers']['part1_ans'] = pl.to_json(amax)
    
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
