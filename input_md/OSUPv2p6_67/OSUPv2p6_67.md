---
title: Multi-part Question
topic: kinematics
author: Jake Bobowski
source:
- underfined
template_version: 0.5
attribution:
- underfined 
outcomes:
- underfined
difficulty:
- undefined
randomization:
- undefined
taxonomy:
- undefined
tags:
- unknown
assets:
- by.png
server: |
    import random, copy, math
    import numpy as np
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)

    # Start problem code

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
    
    data2["params"]["part2"]["ans1"] = 'points towards the negative plate'
    data2["params"]["part2"]["ans2"] = 'points towards the positive plate'
    data2["params"]["part2"]["ans3"] = 'points parallel to the plates'
    
    # define correct answers
    data2["params"]["part2"]["correct_answer"] = data2["params"]["part2"]["ans1"]

    # Update the data object with a new dict
    data.update(data2)
part1:
  type: number-input
  label: $E=$
  pl-customizations:
    allow-blank: false
    weight: 1
part2:
  type: dropdown  
  pl-options:
    weight: 1
    allow-blank: true
---
# {{ params.vars.title }}

## Part 1

### Question Text

Two parallel conducting plates ${{params.L}}\rm\ cm$ on a side are given equal and opposite charges of magnitude ${{params.q}}\times 10^{ {{params.p}} }\rm\ C$.  The plates are ${{params.d}}\rm\ mm$ apart.

What is the electric field at the centre of the region between the plates?

### Answer Section

Please enter in a numeric value

## Part 2

### Answer Section

- {{ params.part1.ans1}}
- {{ params.part1.ans2}}
- {{ params.part1.ans3}}

## Rubric

This should be hidden from students until after the deadline.

## Solution

This should never be revealed to students.

## Comments

These are random comments associated with this question.