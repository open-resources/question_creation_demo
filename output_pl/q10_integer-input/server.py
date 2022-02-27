import random
import pandas as pd
import problem_bank_helpers as pbh
from collections import defaultdict
nested_dict = lambda: defaultdict(nested_dict)

def imports(data):
    import random
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)
    
def generate(data):
    # Start problem code
    
    data2 = nested_dict()
    
    # define or load names/items/objects
    names = pd.read_csv(data["options"]["client_files_course_path"]+"/data/names.csv")["Names"].tolist()
    manual_vehicles = pd.read_csv(data["options"]["client_files_course_path"]+"/data/manual_vehicles.csv")["Manual Vehicles"].tolist()
    
    # store phrases etc
    data2["params"]["vars"]["name"] = random.choice(names)
    data2["params"]["vars"]["vehicle"] = random.choice(manual_vehicles)
    data2["params"]["vars"]["title"] = "Integer Math"
    data2["params"]["vars"]["units"] = "m/s"
    
    # define bounds of the variables
    n = random.randint(2,100)
    
    # store the variables in the dictionary "params"
    data2["params"]["n"] = n
    
    # define correct answers
    data2["correct_answers"]["part1_ans"] = int(n*10)
    
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
