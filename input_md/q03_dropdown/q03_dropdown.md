---
title: Distance travelled
author: Firas Moosvi
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
    import pandas as pd
    import problem_bank_helpers as pbh
    from collections import defaultdict
    nested_dict = lambda: defaultdict(nested_dict)

    # Start problem code

    data2 = nested_dict()

    # define or load names/items/objects
    names = pd.read_csv("data/names.csv")["Names"].tolist()
    manual_vehicles = pd.read_csv("data/manual_vehicles.csv")["Manual Vehicles"].tolist()

    # store phrases etc
    data["params"]["vars"]["name"] = random.choice(names)
    data["params"]["vars"]["vehicle"] = random.choice(manual_vehicles)
    data["params"]["vars"]["title"] = "Distance travelled"
    data["params"]["vars"]["units"] = "m/s"

    # define bounds of the variables
    v = random.randint(2,7)
    t = random.randint(5,10)

    # store the variables in the dictionary "params"
    data["params"]["v"] = v
    data["params"]["t"] = t

    # define possible answers
    data["params"]["part1"]["ans1"] = pbh.roundp(v*t)
    data["params"]["part1"]["ans2"] = pbh.roundp(v+t)
    data["params"]["part1"]["ans3"] = pbh.roundp(v/t)
    data["params"]["part1"]["ans4"] = pbh.roundp(v-t)
    data["params"]["part1"]["ans5"] = pbh.roundp(1.3*(v-t))
    
    # define correct answers
    data["params"]["part1"]["correct_answer"] = data["params"]["part1"]["ans1"]
part1:
  type: dropdown
  pl-options:
    weight: 1
    allow-blank: true
---
# {{ params.vars.title }}

## Question Text

{{ params.vars.name }} is traveling on {{ params.vars.vehicle }} at {{ params.v }} {{ params.vars.units }}.
How far does {{ params.vars.name }} travel in {{ params.t }} seconds, assuming they continue at the same velocity?

## Answer Section

- {{ params.part1.ans1}} {{ params.vars.units}} 
- {{ params.part1.ans2}} {{ params.vars.units}} 
- {{ params.part1.ans3}} {{ params.vars.units}} 
- {{ params.part1.ans4}} {{ params.vars.units}} 
- {{ params.part1.ans5}} {{ params.vars.units}} 

## Rubric

This should be hidden from students until after the deadline.

## Solution

This should never be revealed to students.

## Comments

These are random comments associated with this question.