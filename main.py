from manim import *
import numpy as np

# -----------------------------
# Helper functions to create objects
# -----------------------------

def make_starship() -> VGroup:
    """Create a simple Starship (cylinder body + cone nose)."""
    body = Cylinder(radius=0.5, height=3, direction=UP, color=BLUE)
    nose = Cone(radius=0.5, height=1, direction=UP, color=RED).next_to(body, UP, buff=0)
    return VGroup(body, nose)

def make_planet(radius: float, color: str) -> Sphere:
    """Create a planet sphere."""
    return Sphere(radius=radius, color=color, checkerboard_colors=[color, color])

# -----------------------------
# Scene Builders
# -----------------------------

def build_launch(scene: ThreeDScene):
    """Starbase launch scene."""
    starship = make_starship()
    launchpad = Cube(side_length=2, color=GRAY)
    launchpad.stretch_to_fit_height(0.5)
    launchpad.move_to(ORIGIN)
    starship.move_to(launchpad.get_top() + UP*1.5)

    # Plume that follows rocket
    plume = Dot3D(color=ORANGE).move_to(starship.get_bottom())
    plume.add_updater(lambda m: m.move_to(starship.get_bottom()))

    scene.add(launchpad, starship, plume)

    # Animate launch using .move_to loop for OpenGL safety
    n_steps = 60
    for i in range(n_steps):
        starship.shift(UP*0.1)
        scene.wait(0.05)

    scene.wait(1)

def build_orbit_refuel(scene: ThreeDScene):
    """Orbital refueling scene."""
    rocket = make_starship().scale(0.5)
    tanker = make_starship().scale(0.6).shift(UP*3 + RIGHT*3)
    scene.add(rocket, tanker)

    # Docking path using Line3D
    path = Line3D(rocket.get_center(), tanker.get_center(), color=YELLOW)
    path.add_updater(lambda m: m.put_start_and_end_on(rocket.get_center(), tanker.get_center()))
    scene.add(path)

    # Fuel tracker (placeholder animation)
    fuel_tracker = ValueTracker(0)
    fuel_label = DecimalNumber(0, num_decimal_places=2).add_updater(
        lambda d: d.set_value(fuel_tracker.get_value())
    ).to_corner(UR)
    scene.add(fuel_label)

    # Animate fuel transfer safely
    for i in range(50):
        fuel_tracker.set_value(i/50)
        scene.wait(0.04)

    scene.wait(1)

def build_transfer_arc(scene: ThreeDScene):
    """Earth to Mars transfer scene."""
    earth = make_planet(1, BLUE).shift(LEFT*4)
    mars = make_planet(0.8, RED).shift(RIGHT*4)
    rocket = make_starship().scale(0.4).move_to(earth.get_center())
    scene.add(earth, mars, rocket)

    # Parametric 3D curve for rocket
    def transfer_path(t):
     pos = (1-t)*earth.get_center() + t*mars.get_center() + np.array([0.0, 0.5*np.sin(t*PI), 0.0])
     return np.array(pos, dtype=float)

    transfer_curve = ParametricFunction(transfer_path, t_range=(0,1), color=YELLOW, fill_opacity=0)
    scene.add(transfer_curve)

    # Animate rocket along curve safely
    n_steps = 100
    for i in range(n_steps+1):
        t = i / n_steps
        rocket.move_to(transfer_path(t))
        scene.wait(0.04)

    scene.wait(1)

def build_mars_landing(scene: ThreeDScene):
    """Mars landing scene."""
    mars_surface = Plane(width=6, height=6, color=RED).shift(DOWN*0.5)
    rocket = make_starship().scale(0.4).shift(UP*3)
    scene.add(mars_surface, rocket)

    # Dust puffs
    dust = [Dot3D(radius=0.05, color=ORANGE).move_to(rocket.get_bottom()) for _ in range(5)]
    for d in dust:
        d.add_updater(lambda m, r=rocket: m.move_to(r.get_bottom()))
    scene.add(*dust)

    # Animate landing safely
    n_steps = 60
    for i in range(n_steps):
        rocket.shift(DOWN*0.05)
        scene.wait(0.05)

    scene.wait(1)

# -----------------------------
# Master Scene
# -----------------------------

class MasterScene(ThreeDScene):
    """Full 3D Starship Journey."""
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES)
        build_launch(self)
        build_orbit_refuel(self)
        build_transfer_arc(self)
        build_mars_landing(self)
