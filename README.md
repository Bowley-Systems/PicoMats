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

It is a computational abstraction for both reductionist and pragmatist applications.

The model is based on two categories:

```
Abstract:       Defined by what it does     (characteristics).
Fundamental:    Defined by what it is       (structure/state).
```

<br>

The ontology emerges from this simple series:

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

It's possible to model but computationally impractical for most applications. Hence, the `abstract` section exists for empirical measurements.

<br>

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

When asking a fundamental question, it's better to build from fundamental properties. 
Hence, use the `fundamental` section.

> PicoMats provides the structure for you to build characteristics through modelling, using fundamental properties as your foundation.

---

### Quick Start

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
```

> An introduction example is available in [`example/`](https://github.com/Bowley-Systems/PicoMats/tree/main/example).

---

### Installation 
 
To install:

```bash
pip install PicoMats
```

#### Documentation

Full documentation is available in the [`docs/`](https://github.com/Bowley-Systems/PicoMats/main/docs) folder, including API reference, changelog, and contributors.

---