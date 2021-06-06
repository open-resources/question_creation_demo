---
title: Centripetal Motion
topic: centripetal motion
author: Michael Kudla
source: original
template_version: 0.5
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
server: |
    import random    
    import prairielearn as pl
    import sympy
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)

    # Start problem code

    data2 = nested_dict()

    # store phrases etc
    data2["params"]["vars"]["title"] = 'Centripetal Motion'

    # Declare math symbols to be used by sympy
    m, v, r = sympy.symbols('m v r')

    # Describe the solution equation
    F = m*v**2/r
    
    # Answer to fill in the blank input stored as JSON.
    data2['correct_answers']['part1_ans'] = pl.to_json(F)
    
    # Update the data object with a new dict
    data.update(data2)    
part1:
  type: symbolic-input
  label: $F_r = $
  pl-customizations:
    variables: "m, v, r"
    weight: 1
    allow-blank: false
---
# {{ params.vars.title }}

## Question Text

Write the centripetal force $F_r$ in terms of the mass $m$, velocity $v$, and radius $r$.

Note that it may not be necessary to use every variable. Use the following table as a reference for each variable:

| $\LaTeX$ | Use   |
|----------|-------|
| $m$  | m  |
| $v$  | v  |
| $r$  | r  |


### Answer Section

{{ substitutions.part1.label }}

## Rubric

This should be hidden from students until after the deadline.

## Solution

This should never be revealed to students.

## Comments

These are random comments associated with this question.
