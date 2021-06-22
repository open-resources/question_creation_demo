---
title: Distance travelled
topic: Template
author: Firas Moosvi
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
        import problem_bank_helpers as pbh
        from collections import defaultdict
        nested_dict = lambda: defaultdict(nested_dict)
    generate: |
        # Start problem code

        data2 = nested_dict()

        # define or load names/items/objects
        names = pd.read_csv("data/names.csv")["Names"].tolist()
        manual_vehicles = pd.read_csv("data/manual_vehicles.csv")["Manual Vehicles"].tolist()

        # store phrases etc
        data2["params"]["vars"]["name"] = random.choice(names)
        data2["params"]["vars"]["vehicle"] = random.choice(manual_vehicles)
        data2["params"]["vars"]["title"] = "Distance travelled"
        data2["params"]["vars"]["units"] = "m/s"

        # define bounds of the variables
        v = random.randint(2,7)
        t = random.randint(5,10)

        # store the variables in the dictionary "params"
        data2["params"]["v"] = v
        data2["params"]["t"] = t

        # define correct answers
        data2["correct_answers"]["part1_ans"] = v*t
        
        # Update the data object with a new dict
        data.update(data2)
    prepare: |
        pass
    parse: |
        pass
    grade: |
        pass
part1:
  type: number-input
  pl-customizations:
    weight: 1
    allow-blank: true
    label: $d= $
    suffix: m
    comparison: sigfig
    digits: 2
---
# {{ params.vars.title }}

{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.

## Question Text

How far does {{ params.vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

### Answer Section

Please enter in a numeric value in {{ params.vars.units }}.

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
