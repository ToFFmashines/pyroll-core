from pyroll.core import Profile, BoxGroove, Roll, RollPass, PassSequence, Transport

in_profile = Profile.square(
    side=180e-3,
    corner_radius=2e-3,
    temperature=1200 + 273.15,
    strain=0,
    material=["C45", "steel"],
    flow_stress=100e6,
    length=1,
)

sequence = PassSequence([
    RollPass(
    label = "BOX B0",
    roll = Roll(
        groove = BoxGroove(
            depth = 82e-3,
            r1 = 6e-3,
            r2 = 12e-3,
            ground_width = 130e-3,
            usable_width = 145e-3
        ),
    nominal_radius = 270e-3,
    rotational_frequency = 1
    ),
    gap = 40e-3,
    ),
])

sequence.solve(in_profile)