from beam_col_elements import *

# --------------------------------------------------------------------------------
# Gravity loads
# --------------------------------------------------------------------------------
slab_thickness=4.0 * inch
Q_slab = gamma_conc * slab_thickness       # Self weight of Slab N per mm2
Q_floor_finish = 1.0e-3                    # Floor finish load N per mm2, floor finish load = 1 kN/m2
LL = 0.3 * 1.0e-3                         # Live load for all floors N per mm2, live load = 1 kN/m2, 30% considered for NLTHA

TL = Q_slab + Q_floor_finish + LL          # Total load for all floors N per mm2

P11 = (1/2) * 1600 * 800 * TL        # Triangular Load Distribution, N
P1 = P11 / (1600)                       # UDL for P11 N / mm
Beam_self_weight = Beam_mpul * g           # Total Self weight of Beam N / mm
Col_self_weight = Col_mpul * g             # Total Self weight of Column N / mm

wall_load = 115 * 2150 * gamma_masonry  # N / mm, wall thickness = 115 mm, height = 2150mm, apply on all beams

# --------------------------------------------------------------------------------
# Nodal Mass Distribution; mass(nodeTag, *massValues)
# --------------------------------------------------------------------------------
bay_width_X = 1600
bay_width_Y = 1600

NBayX = 2
NBayY = 4

def lumped_nodal_mass():

    TL_mass = TL * bay_width_X * bay_width_Y * NBayX * NBayY / g
    half_wall_mass = (wall_load / 2) * (bay_width_X * NBayX * (NBayY + 1) + bay_width_Y * NBayY * (NBayX + 1)) / g
    full_wall_mass = half_wall_mass * 2

    for node in master_nodes:
        if node == master_nodes[0] or node == master_nodes[-1]:
            ops.mass(node, TL_mass + half_wall_mass, TL_mass + half_wall_mass, 0.0, 0.0, 0.0, 0.0)
        else:
            ops.mass(node, TL_mass + full_wall_mass, TL_mass + full_wall_mass, 0.0, 0.0, 0.0, 0.0)

lumped_nodal_mass()

# --------------------------------------------------------------------------------
# Application Of UDL in local coordinate axes 
# --------------------------------------------------------------------------------
ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)

# eleLoad('-ele', *eleTags, '-range', eleTag1, eleTag2, '-type', '-beamUniform', Wy, <Wz>, Wx=0.0, '-beamPoint', Py, <Pz>, xL, Px=0.0, '-beamThermal', *tempPts)


def UDL_applier():
    # UDL Application on Beams
    ops.eleLoad('-ele', *beams_with_one_P1, '-type', '-beamUniform', -P1, 0.0, 0.0)


    ops.eleLoad('-ele', *beams_with_two_P1, '-type', '-beamUniform', -(2 * P1), 0.0, 0.0)

    ops.eleLoad('-ele', *all_beams, '-type', '-beamUniform', -(Beam_self_weight + wall_load), 0.0, 0.0)

    # UDL Application on Columns
    ops.eleLoad('-ele', *all_columns, '-type', '-beamUniform', 0.0, 0.0, -Col_self_weight)



   





    