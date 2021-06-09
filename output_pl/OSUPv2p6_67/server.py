import random, copy, math
import numpy as np
import pandas as pd
import problem_bank_helpers as pbh
from collections import defaultdict
nested_dict = lambda: defaultdict(nested_dict)

def generate(data):
    
    data2 = nested_dict()
    
    # Sample random numbers
    L = random.choice(np.linspace(7, 15, num = 9))
    q = random.choice(np.linspace(1, 9, num = 41))
    p = random.choice(np.linspace(-10, -6, num = 5))
    d = random.choice(np.linspace(0.5, 2.5, num = 21))
    
    # Put these numbers into data['params']
    data2["params"]["L"] = "{:.0f}".format(L)
    data2["params"]["q"] = "{:.1f}".format(q)
    data2["params"]["p"] = "{:.0f}".format(p)
    data2["params"]["d"] = "{:.1f}".format(d)
        
    # Compute the solutions
    e0 = 8.85e-12 # C^2/N m^2
    E = (q*10**p/(L/100)**2)/e0
    
    # Put the solutions into data['correct_answers']
    data2['correct_answers']['E'] = E
    
    # Write the solutions formatted using scientific notation while keeping 3 sig figs.
    data2['correct_answers']['Estr'] = "{:.2e}".format(E)
    
    # define possible answers
    
    data2["params"]["part2"]["ans1"]["value"] = 'points towards the negative plate'
    data2["params"]["part2"]["ans1"]["correct"] = True
    
    data2["params"]["part2"]["ans2"]["value"] = 'points towards the positive plate'
    data2["params"]["part2"]["ans2"]["correct"] = False
    
    data2["params"]["part2"]["ans3"]["value"] = 'points parallel to the plates'
    data2["params"]["part2"]["ans3"]["correct"] = False
    
    # Update the data object with a new dict
    data.update(data2)
    