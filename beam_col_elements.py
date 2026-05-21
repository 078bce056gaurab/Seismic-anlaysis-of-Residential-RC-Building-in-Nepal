import openseespy.opensees as ops
import numpy as np
import matplotlib.pyplot as plt
import opsvis as opsv

from beam_col_section import *              # Import the section either Bare, Retrofit Concrete Jacketing or Retrofit Steel Jacketing

Beam_mpul = 13 * inch * 9 * inch * gamma_conc / g
Col_mpul = 9 * inch * 9* inch * gamma_conc / g

# --------------------------------------------------------------------------------
# Elements
# --------------------------------------------------------------------------------

# Geometry transformations -----------------------
Beam_X_TransfTag = 1
Beam_Y_TransfTag = 2
Col_TransfTag = 3

#geomTransf(transfType, transfTag, *transfArgs)
ops.geomTransf('Linear', Beam_X_TransfTag, 1, -1, 0)  
ops.geomTransf('Linear', Beam_Y_TransfTag, 1, 1, 0)   
ops.geomTransf('PDelta', Col_TransfTag, -1, 0, 1)   

#  Integration setup -----------------------------

#beamIntegration('Lobatto', tag, secTag, N)
Beam_IntTag = 1
Col_IntTag = 2


numIntPts_Beam = 5
numIntPts_Col = 5

ops.beamIntegration('Lobatto', Beam_IntTag, Beam_SecTag, numIntPts_Beam)
ops.beamIntegration('Lobatto', Col_IntTag, Col_SecTag, numIntPts_Col)


#  Elements setup -----------------------------

# --------------------------------------------------------------------------------
# Beam Elements ---- ops.element('forceBeamColumn', XBeamTag, startNode, endNode, Beam_X_TransfTag, Beam_1_IntTag, '-mass', Beam_1_mpul)
# --------------------------------------------------------------------------------

# Floor 2 Beams -----------------------------------
# Parallel to X axis
ops.element('forceBeamColumn', 201202, 201, 202, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 202203, 202, 203, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 204205, 204, 205, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 205206, 205, 206, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 207208, 207, 208, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 208209, 208, 209, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 210211, 210, 211, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 211212, 211, 212, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 213214, 213, 214, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 214215, 214, 215, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)


# Parallel to Y axis
ops.element('forceBeamColumn', 201204, 201, 204, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 204207, 204, 207, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 207210, 207, 210, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 210213, 210, 213, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 203206, 203, 206, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 206209, 206, 209, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 209212, 209, 212, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 212215, 212, 215, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 202205, 202, 205, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 205208, 205, 208, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 208211, 208, 211, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 211214, 211, 214, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)


# Floor 3 Beams -----------------------------------
# Parallel to X axis
ops.element('forceBeamColumn', 301302, 301, 302, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 302303, 302, 303, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 304305, 304, 305, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 305306, 305, 306, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 307308, 307, 308, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 308309, 308, 309, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 310311, 310, 311, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 311312, 311, 312, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 313314, 313, 314, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 314315, 314, 315, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)

# Parallel to Y axis
ops.element('forceBeamColumn', 301304, 301, 304, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 304307, 304, 307, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 307310, 307, 310, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 310313, 310, 313, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 302305, 302, 305, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 305308, 305, 308, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 308311, 308, 311, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 311314, 311, 314, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 303306, 303, 306, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 306309, 306, 309, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 309312, 309, 312, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 312315, 312, 315, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)

# Floor 4 Beams -----------------------------------
# Parallel to X axis
ops.element('forceBeamColumn', 401402, 401, 402, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 402403, 402, 403, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 404405, 404, 405, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 405406, 405, 406, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 407408, 407, 408, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 408409, 408, 409, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 410411, 410, 411, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 411412, 411, 412, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 413414, 413, 414, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 414415, 414, 415, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)

# Parallel to Y axis
ops.element('forceBeamColumn', 401404, 401, 404, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 404407, 404, 407, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 407410, 407, 410, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 410413, 410, 413, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 402405, 402, 405, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 405408, 405, 408, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 408411, 408, 411, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 411414, 411, 414, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 403406, 403, 406, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 406409, 406, 409, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 409412, 409, 412, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 412415, 412, 415, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)

# Floor 5 Beams -----------------------------------
# Parallel to X axis
ops.element('forceBeamColumn', 501502, 501, 502, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 502503, 502, 503, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 504505, 504, 505, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 505506, 505, 506, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 507508, 507, 508, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 508509, 508, 509, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 510511, 510, 511, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 511512, 511, 512, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 513514, 513, 514, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 514515, 514, 515, Beam_X_TransfTag, Beam_IntTag, '-mass', Beam_mpul)

# Parallel to Y axis
ops.element('forceBeamColumn', 501504, 501, 504, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 504507, 504, 507, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 507510, 507, 510, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 510513, 510, 513, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 502505, 502, 505, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 505508, 505, 508, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 508511, 508, 511, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 511514, 511, 514, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 503506, 503, 506, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 506509, 506, 509, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 509512, 509, 512, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
ops.element('forceBeamColumn', 512515, 512, 515, Beam_Y_TransfTag, Beam_IntTag, '-mass', Beam_mpul)
# --------------------------------------------------------------------------------
# Beam Element Tag Lists
# --------------------------------------------------------------------------------

beams_with_one_P1 = [201204, 204207, 207210, 210213, 213214, 214215, 201202, 202203, 203206, 206209, 209212, 212215, 
                     301304, 304307, 307310, 310313, 313314, 314315, 301302, 302303, 303306, 306309, 309312, 312315,
                     401404, 404407, 407410, 410413, 413414, 414415, 401402, 402403, 403406, 406409, 409412, 412415,
                     501504, 504507, 507510, 510513, 513514, 514515, 501502, 502503, 503506, 506509, 509512, 512515]

beams_with_two_P1 = [204205, 205206, 207208, 208209, 210211, 211212, 202205, 205208, 208211, 211214, 
                     304305, 305306, 307308, 308309, 310311, 311312, 302305, 305308, 308311, 311314, 
                     404405, 405406, 407408, 408409, 410411, 411412, 402405, 405408, 408411, 411414, 
                     504505, 505506, 507508, 508509, 510511, 511512, 502505, 505508, 508511, 511514, ]




# All beam elements in X direction (Beam_X_TransfTag)
X_beams = [
    # Floor 2
    201202, 202203, 204205, 205206, 207208, 208209, 210211, 211212, 213214, 214215,
    # Floor 3
    301302, 302303, 304305, 305306, 307308, 308309, 310311, 311312, 313314, 314315,
    # Floor 4
    401402, 402403, 404405, 405406, 407408, 408409, 410411, 411412, 413414, 414415,
    # Floor 5
    501502, 502503, 504505, 505506, 507508, 508509, 510511, 511512, 513514, 514515
]

# All beam elements in Y direction (Beam_Y_TransfTag)
Y_beams = [
    # Floor 2
    201204, 204207, 207210, 210213, 213214, 202205, 205208, 208211, 211214, 203206, 206209, 209212, 212215,
    # Floor 3
    301304, 304307, 307310, 310313, 313314, 302305, 305308, 308311, 311314, 303306, 306309, 309312, 312315,
    # Floor 4
    401404, 404407, 407410, 410413, 413414, 402405, 405408, 408411, 411414, 403406, 406409, 409412, 412415,
    # Floor 5
    501504, 504507, 507510, 510513, 513514, 502505, 505508, 508511, 511514, 503506, 506509, 509512, 512515
]

# All beam elements combined
all_beams = X_beams + Y_beams

# --------------------------------------------------------------------------------
# Column Elements
# --------------------------------------------------------------------------------

# Floor 1 Columns -----------------------------------
ops.element('forceBeamColumn', 101201, 101, 201, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 102202, 102, 202, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 103203, 103, 203, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 104204, 104, 204, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 105205, 105, 205, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 106206, 106, 206, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 107207, 107, 207, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 108208, 108, 208, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 109209, 109, 209, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 110210, 110, 210, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 111211, 111, 211, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 112212, 112, 212, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 113213, 113, 213, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 114214, 114, 214, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 115215, 115, 215, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)

# Floor 2 Columns -----------------------------------
ops.element('forceBeamColumn', 201301, 201, 301, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 202302, 202, 302, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 203303, 203, 303, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 204304, 204, 304, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 205305, 205, 305, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 206306, 206, 306, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 207307, 207, 307, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 208308, 208, 308, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 209309, 209, 309, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 210310, 210, 310, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 211311, 211, 311, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 212312, 212, 312, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 213313, 213, 313, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 214314, 214, 314, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 215315, 215, 315, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)

# Floor 3 Columns -----------------------------------
ops.element('forceBeamColumn', 301401, 301, 401, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 302402, 302, 402, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 303403, 303, 403, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 304404, 304, 404, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 305405, 305, 405, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 306406, 306, 406, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 307407, 307, 407, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 308408, 308, 408, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 309409, 309, 409, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 310410, 310, 410, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 311411, 311, 411, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 312412, 312, 412, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 313413, 313, 413, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 314414, 314, 414, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 315415, 315, 415, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)

# Floor 4 Columns -----------------------------------
ops.element('forceBeamColumn', 401501, 401, 501, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 402502, 402, 502, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 403503, 403, 503, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 404504, 404, 504, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 405505, 405, 505, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 406506, 406, 506, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 407507, 407, 507, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 408508, 408, 508, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 409509, 409, 509, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 410510, 410, 510, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 411511, 411, 511, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 412512, 412, 512, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 413513, 413, 513, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 414514, 414, 514, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)
ops.element('forceBeamColumn', 415515, 415, 515, Col_TransfTag, Col_IntTag, '-mass', Col_mpul)


# --------------------------------------------------------------------------------
# Column Element Tag Lists
# --------------------------------------------------------------------------------

# Floor 1 Columns
floor1_cols = [101201, 102202, 103203, 104204, 105205, 106206, 107207, 108208, 109209, 110210, 111211, 112212, 113213, 114214, 115215]

# Floor 2 Columns
floor2_cols = [201301, 202302, 203303, 204304, 205305, 206306, 207307, 208308, 209309, 210310, 211311, 212312, 213313, 214314, 215315]

# Floor 3 Columns
floor3_cols = [301401, 302402, 303403, 304404, 305405, 306406, 307407, 308408, 309409, 310410, 311411, 312412, 313413, 314414, 315415]

# Floor 4 Columns
floor4_cols = [401501, 402502, 403503, 404504, 405505, 406506, 407507, 408508, 409509, 410510, 411511, 412512, 413513, 414514, 415515]

# All column elements
all_columns = floor1_cols + floor2_cols + floor3_cols + floor4_cols
