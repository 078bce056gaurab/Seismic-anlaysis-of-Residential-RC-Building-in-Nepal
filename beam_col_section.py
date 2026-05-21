import openseespy.opensees as ops
import opsvis as opsv
import matplotlib.pyplot as plt
import numpy as np

from Dimensions_and_nodes import *
from Materials import *

def area(diameter):
    return (np.pi * diameter ** 2) / 4.0

Beam_SecTag = 1
Col_SecTag = 2


matcolor = ['tab:orange', 'skyblue',  'w', 'w']

# Beam ------------------------------------------------------------

fiber_section_beam = [

['section', 'Fiber', Beam_SecTag, '-GJ', 1.0e6],
['patch', 'rect', confined_concrete_tag, 6, 6, *[-5.5 * inch, -3.5 * inch], *[5.5 * inch, 3.5 * inch]], # core

['patch', 'quad', unconfined_concrete_tag, 2, 6, *[5.5 * inch,-3.5 * inch], *[6.5 * inch,-4.5 * inch], *[6.5 * inch, 4.5 * inch], *[5.5 * inch,3.5 * inch]], # right side cover
['patch', 'quad', unconfined_concrete_tag, 2, 6, *[-6.5 * inch,-4.5 * inch], *[-5.5 * inch,-3.5 * inch], *[-5.5 * inch,3.5 * inch], *[-6.5 * inch, 4.5 * inch]], # left side cover

['patch', 'quad', unconfined_concrete_tag, 6, 2, *[-5.5 * inch,3.5 * inch], *[5.5 * inch,3.5 * inch], *[6.5 * inch, 4.5 * inch], *[-6.5 * inch,4.5 * inch]], # top side cover
['patch', 'quad', unconfined_concrete_tag, 6, 2, *[-6.5 * inch,-4.5 * inch], *[6.5 * inch,-4.5 * inch], *[5.5 * inch,-3.5 * inch], *[-5.5 * inch,-3.5 * inch]], # bottom side cover

['layer', 'straight', steel_tag, 3, area(16), *[5.5 * inch, 3.5 * inch], *[5.5 * inch, -3.5 * inch]], # right layer
['layer', 'straight', steel_tag, 3, area(16), *[-5.5 * inch, 3.5 * inch], *[-5.5 * inch, -3.5 * inch]] # left layer

]

opsv.fib_sec_list_to_cmds(fiber_section_beam)

# opsv.plot_fiber_section(fiber_section_beam, matcolor=matcolor)
# plt.title("Beam Section")

# Column for all floor  ------------------------------------------------------------

fiber_section_col = [

['section', 'Fiber', Col_SecTag, '-GJ', 1.0e6],
['patch', 'rect', confined_concrete_tag, 6, 6, *[-3.5 * inch, -3.5 * inch], *[3.5 * inch, 3.5 * inch]], # core

['patch', 'quad', unconfined_concrete_tag, 2, 6, *[3.5 * inch,-3.5 * inch], *[4.5 * inch,-4.5 * inch], *[4.5 * inch, 4.5 * inch], *[3.5 * inch,3.5 * inch]], # right side cover
['patch', 'quad', unconfined_concrete_tag, 2, 6, *[-4.5 * inch,-4.5 * inch], *[-3.5 * inch,-3.5 * inch], *[-3.5 * inch,3.5 * inch], *[-4.5 * inch, 4.5 * inch]], # left side cover

['patch', 'quad', unconfined_concrete_tag, 6, 2, *[-3.5 * inch,3.5 * inch], *[3.5 * inch,3.5 * inch], *[4.5 * inch, 4.5 * inch], *[-4.5 * inch,4.5 * inch]], # top side cover
['patch', 'quad', unconfined_concrete_tag, 6, 2, *[-4.5 * inch,-4.5 * inch], *[4.5 * inch,-4.5 * inch], *[3.5 * inch,-3.5 * inch], *[-3.5 * inch,-3.5 * inch]], # bottom side cover

['layer', 'straight', steel_tag, 2, area(16), *[3.5 * inch, 3.5 * inch], *[3.5 * inch, -3.5 * inch]], # right layer
['layer', 'straight', steel_tag, 2, area(16), *[-3.5 * inch, 3.5 * inch], *[-3.5 * inch, -3.5 * inch]], # left layer
['layer', 'straight', steel_tag, 2, area(12), *[0 * inch, 3.5 * inch], *[0 * inch, -3.5 * inch]],        # middle existing layer


]

opsv.fib_sec_list_to_cmds(fiber_section_col)

opsv.plot_fiber_section(fiber_section_col, matcolor=matcolor)
plt.title("Column Section for all floor ")



# Plotting of the sections ------------------------------------------------------------

plt.axis('equal')
plt.show()