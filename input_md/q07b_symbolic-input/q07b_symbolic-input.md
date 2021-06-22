---
title: Symbolic Input 2 - Trig
topic: Template
author: Michael Kudla
source: original
template_version: 1.0
attribution: standard
outcomes:
- 6.1.1.0
- 6.1.1.1
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets:
server: 
    imports: |
        import random
        import pandas as pd
        import sympy as sp
        import prairielearn as pl
        import problem_bank_helpers as pbh
        from collections import defaultdict
        nested_dict = lambda: defaultdict(nested_dict)
    generate: |
        # Start problem code

        data2 = nested_dict()

        # define or load names/items/objects
        names = pd.read_csv("data/names.csv")["Names"].tolist()
        vehicles = pd.read_csv("data/vehicles.csv")["Vehicles"].tolist()

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
        
        # Update the data object with a new dict
        data.update(data2)
    prepare: |
        pass
    parse: |
        pass
    grade: |
        pass
part1:
  type: symbolic-input
  label: $F_r =$
  pl-customizations:
    variables: "mu_s, g , theta"
    weight: 1
    allow-blank: true
---
# {{ params.vars.title }}

## Question Text

{{ params.vars.name }} is driving a {{ params.vars.vehicle }} up a slope of angle $\theta$. 

There is a wooden crate in the back of the {{ params.vars.vehicle }} and the coefficients of static and kinetic friction between the crate and the {{ params.vars.vehicle }} are $\mu_s$ and $\mu_k$ respectively. 

If the {{ params.vars.vehicle }} starts moving, what is the maximum acceleration the {{ params.vars.vehicle }} can have without the crate slipping? You should provide a symbolic answer in terms of the following variables: $\mu_s$, $\mu_k$, $g$, and $\theta$.

Note that it may not be necessary to use every variable. Use the following table as a reference for using each variable:

| $Variable$ | Use   |
|----------|-------|
| $\mu_s$  | mu_s  |
| $\mu_k$  | mu_k  |
| $g$      | g     |
| $\theta$ | theta |

### Answer Section

TODO: implement copying of the 'label' field to the substitutions.

## pl-submission-panel

Everything here will get inserted directly into the pl-submission-panel element at the end of the `question.html`.

## pl-answer-panel

Everything here will get inserted directly into an pl-answer-panel element at the end of the `question.html`.

## Rubric

This should be hidden from students until after the deadline.

## Solution

This should never be revealed to students.

## Comments

These are random comments associated with this question.
