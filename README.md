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

<!-- Update this image before its on pypi -->

<p align="center">
    <img 
        src="https://raw.githubusercontent.com/Bowley-Systems/PicoMats/refs/heads/main/media/logo.png" 
        alt="PicoMats logo" 
        style="width:100%; max-width:100%; display:block;"
    >
</p>
<p align="center">
    Use the material. Sustain the assumptions. <br>
    Reduce uncertainty by making every assumption explicit.
</p>

### Overview

![License](https://img.shields.io/badge/License-MIT-E14F4C?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-006D77?style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-N/A-E14F4C?style=flat-square)
[![PyPI Downloads](https://img.shields.io/pepy/dt/picomats?label=downloads\&style=flat-square\&color=006D77)](https://pepy.tech/projects/picomats)

PicoMats is an assumption-driven material ontology that sustains assumptions throughout your pipeline. It provides unit-informed material definitions with accompanying assumptions.  

```
- Follows a computational ontology called `Abstract-Fundamental Ontology`.
- Uses `UnitValues` and `PicoUnits` for encoding typed numerical definitions.
- Tracks assumptions alongside material definitions to reduce model uncertainty.
```

---

### What is the Abstract-Fundamental Ontology?

Abstract-Fundamental Ontology is a computational abstraction for both reductionist and pragmatist applications.

The model is based on two categories:

```
Abstract:       Defined by what it does     (measured properties).
Fundamental:    Defined by what it is       (atomic structure).
```

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

It's a mistake to assume it's impossible to model, but computational cost is prohibitive for most applications. Hence, you `abstract` it via empirical methods to measure friction, losing all but the necessary information.

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

When asking such a fundamental question, wouldn't it be best to derive the relations from what the material fundamentally is? Hence, you use `fundamental`, which describes what the material is, and build the necessary properties without measurement-implicit assumptions. 

> PicoMats does not calculate material properties from the fundamental characteristics of the elements. It is up to the user to compute them via custom modelling or external frameworks.

Both `abstract` and `fundamental` also make a good semantic boundary for model development. For example, `material.abstract.copper` and `material.fundamental.copper` explicitly denote the reality of their origin.

---

### Proposed workflow

PicoMats is still under development for `v0.1-alpha`. Implementation details and some abstractions may change.

```py
from picomats import mm
from picomats import Materials

# Pulls materials into the simulation
copper = Materials.abstract.pure.copper

density = copper.density
volume = 100 * mm ** 3

mass = volume * density
# > Output: 0.896 m(kg)

copper.assumptions.density
# > Output:
# >└── Method
# >    ├── Hydrostatic Balance (Archimedes' Principle)
# >    └── Media Type: Distilled Water
# >└── Assumptions
# >    ├── Lack of air bubbles within media
# >    └── Media temperature stability
```

---

### Installation 
 
Until release, this only installs the overview page and related files:
```bash
pip install PicoMats
```

#### Documentation

All internal documentation can be found within this repo's [issues](https://github.com/wgbowley/PicoMaterials/issues).

---