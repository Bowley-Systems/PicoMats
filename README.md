<!-- 
Color palette: 
#006d77ff -> deep, muted teal-green 
#d92c2aff -> bold, warm crimson-red 

It might seem risky to define a new ontology for materials,
but imagine for a second you're trying to do work across
electromagnetic, mechanical, and chemical systems.

And imagine your goal is to have a material backend that
has the same routing from v0.1 to vn.n. It needs to be
made general-purpose.

— William Bowley, 12th of August, 2026
-->

<p align="center"><img src="media/logo.png" alt="PicoMaterials logo" style="width:100%; max-width:100%; display:block;"></p>
<h4 align="center">A unit-informed, assumption-driven material ontology.</h4>
<p align="center">
    Use the material. Sustain the assumptions. <br>
    Reduce uncertainty by making every assumption explicit.
</p>

# Overview

![License](https://img.shields.io/badge/License-MIT-E14F4C?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-006D77?style=flat-square)

PicoMats is an assumption-driven material ontology that sustains assumptions throughout your pipeline. It provides unit-informed material definitions with accompanying assumptions.  

> [!important]
> ### Features:
> - Follows a computational ontology called `Element–Abstract Ontology`.
> - Uses `UnitValues` and `PicoUnits` for encoding typed numerical definitions.

## What is the Element–Abstract Ontology?

Element-Abstract Ontology is a computational abstraction for both reductionist and pragmatist applications.

The model is based on two categories:

```
Element:    Defined by what it is       (atomic structure).
Abstract:   Defined by what it does     (measured properties).
```

---

The ontology emerges from this simple thought experiment:

```
Let's model a ball rolling down a ramp.
        ↓   
What forces act on the ball?
        ↓
Gravity, electromagnetic repulsion, and friction.
        ↓
How do we model friction?
        ↓
A coefficient? Isn't that arbitrary?
        ↓
Why not just model it?
        ↓
What exactly is friction?
        ↓
Oh, random microscopic interactions...
```

It's a mistake to assume it's impossible to model, but computational cost is ridiculous for most applications. Hence, you `abstract` it via empirical methods to measure friction, losing all but the necessary information.

But `abstract` isn't always the right model...

```
I want to research superconductors.
        ↓
Oh, my temperature range is 0 K to 200 K.
        ↓
Where do I get material definitions for that range?
        ↓
I'll just interpolate the standard Niobium definition.
        ↓
Actually, how were these measurements obtained?
```

When asking such a fundamental question, wouldn't it be best to derive the relations from what the `element` fundamentally is? Hence, you use `element`, which describes what the material is, and build the necessary properties without measurement-implicit assumptions. 

## Quick Start
 
```py
from picomats import
# Work In Progress
```

## Installation 
 
To install:
```bash
pip install PicoMats
```

### Documentation

All internal documentation can be found within this repo's [issues](https://github.com/wgbowley/PicoMaterials/issues).
