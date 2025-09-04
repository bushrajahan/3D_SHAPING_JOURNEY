# Starship Mission: Earth → Mars

## Overview
This project is a **3D Manim animation** showcasing a SpaceX-style Starship mission. The animation covers the following phases:

1. **Launch from Starbase (Earth)** – Starship lifts off from a simplified launchpad with engine plume and countdown.  
2. **Orbital Refueling** – The Starship docks with a tanker in low Earth orbit and refuels using a visual fuel transfer animation.  
3. **Earth → Mars Transfer** – The rocket follows a stylized Hohmann-like transfer orbit while HUD labels display live velocity, altitude, and mission time.  
4. **Mars Arrival and Landing** – The Starship performs atmospheric entry, retro-burn, and a soft touchdown with dust effects on Mars’ surface.  

The animation emphasizes **advanced 3D techniques**, **camera choreography**, **smooth motion**, and **technical HUD overlays**.  

---

## Features

- **3D Modeling**
  - Starship built from cylinders, cones, and triangles.
  - Planets represented as spheres with gloss and rotation.
  - Starfield background for cinematic depth.

- **Motion & Updaters**
  - Smooth motion with `ValueTracker` and updaters.
  - Parametric Bezier paths for launch, docking, and transfer.
  - Realistic plume, retro-burn, and dust effects.

- **Camera & Cinematics**
  - Multi-phase camera movements (`phi`, `theta`, `zoom`).
  - Ambient camera rotation for dynamic shots.
  - Layered transitions: `FadeIn`, `LaggedStart`, `Transform`.

- **HUD & Telemetry**
  - Live-updating labels for time, velocity, altitude, and fuel.
  - Numeric displays using `DecimalNumber` and `MathTex`.

- **Modular & Reusable Code**
  - Functions: `make_starship()`, `make_planet()`, `make_starfield()`.
  - Scene builders: `build_launch()`, `build_orbit_refuel()`, `build_transfer_arc()`, `build_mars_landing()`.
  - Single-command master render: `MasterScene`.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone <YOUR_GITHUB_REPO>
   cd starship_mission
# Starship Mission: Earth → Mars

## Overview
This project is a **3D Manim animation** showcasing a SpaceX-style Starship mission. The animation covers the following phases:

1. **Launch from Starbase (Earth)** – Starship lifts off from a simplified launchpad with engine plume and countdown.  
2. **Orbital Refueling** – The Starship docks with a tanker in low Earth orbit and refuels using a visual fuel transfer animation.  
3. **Earth → Mars Transfer** – The rocket follows a stylized Hohmann-like transfer orbit while HUD labels display live velocity, altitude, and mission time.  
4. **Mars Arrival and Landing** – The Starship performs atmospheric entry, retro-burn, and a soft touchdown with dust effects on Mars’ surface.  

The animation emphasizes **advanced 3D techniques**, **camera choreography**, **smooth motion**, and **technical HUD overlays**.  

---

## Features

- **3D Modeling**
  - Starship built from cylinders, cones, and triangles.
  - Planets represented as spheres with gloss and rotation.
  - Starfield background for cinematic depth.

- **Motion & Updaters**
  - Smooth motion with `ValueTracker` and updaters.
  - Parametric Bezier paths for launch, docking, and transfer.
  - Realistic plume, retro-burn, and dust effects.

- **Camera & Cinematics**
  - Multi-phase camera movements (`phi`, `theta`, `zoom`).
  - Ambient camera rotation for dynamic shots.
  - Layered transitions: `FadeIn`, `LaggedStart`, `Transform`.

- **HUD & Telemetry**
  - Live-updating labels for time, velocity, altitude, and fuel.
  - Numeric displays using `DecimalNumber` and `MathTex`.

- **Modular & Reusable Code**
  - Functions: `make_starship()`, `make_planet()`, `make_starfield()`.
  - Scene builders: `build_launch()`, `build_orbit_refuel()`, `build_transfer_arc()`, `build_mars_landing()`.
  - Single-command master render: `MasterScene`.

---

## Installation

1. **Clone the repository**
   ```bash git clone https://github.com/bushrajahan/3D_SHAPING_JOURNEY
     cd 3D_STARSHIP_JOURNEY
     code . // For vs code
  
     OPEN TERMINAL THEN RUN python -m manim -pqh main.py MasterScene --renderer=opengl --write_to_movie

