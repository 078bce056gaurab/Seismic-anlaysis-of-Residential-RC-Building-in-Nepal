import openseespy.opensees as ops
import opsvis as opsv
import matplotlib.pyplot as plt
import numpy as np

from Dimensions_and_nodes import *
from Materials_Retrofit_Concrete_Jacketing import *

def area(diameter):
    return (np.pi * diameter ** 2) / 4.0

Beam_SecTag = 1
Col_SecTag = 2


matcolor = ['orange', 'skyblue','gray',"tab:orange","tab:blue"]

# Beam ------------------------------------------------------------

fiber_section_beam = [

['section', 'Fiber', Beam_SecTag, '-GJ', 1.0e6],
['patch', 'rect', confined_concrete_tag, 6, 6, *[-5.5 * inch, -3.5 * inch], *[5.5 * inch, 3.5 * inch]], # core

['patch', 'quad', unconfined_concrete_tag, 2, 6, *[5.5 * inch,-3.5 * inch], *[6.5 * inch,-4.5 * inch], *[6.5 * inch, 4.5 * inch], *[5.5 * inch,3.5 * inch]], # right side cover
['patch', 'quad', unconfined_concrete_tag, 2, 6, *[-6.5 * inch,-4.5 * inch], *[-5.5 * inch,-3.5 * inch], *[-5.5 * inch,3.5 * inch], *[-6.5 * inch, 4.5 * inch]], # left side cover

['patch', 'quad', unconfined_concrete_tag, 6, 2, *[-5.5 * inch,3.5 * inch], *[5.5 * inch,3.5 * inch], *[6.5 * inch, 4.5 * inch], *[-6.5 * inch,4.5 * inch]], # top side cover
['patch', 'quad', unconfined_concrete_tag, 6, 2, *[-6.5 * inch,-4.5 * inch], *[6.5 * inch,-4.5 * inch], *[5.5 * inch,-3.5 * inch], *[-5.5 * inch,-3.5 * inch]], # bottom side cover

['layer', 'straight', steel_tag, 3, area(12), *[5.5 * inch, 3.5 * inch], *[5.5 * inch, -3.5 * inch]], # right layer
['layer', 'straight', steel_tag, 3, area(12), *[-5.5 * inch, 3.5 * inch], *[-5.5 * inch, -3.5 * inch]] # left layer

]

opsv.fib_sec_list_to_cmds(fiber_section_beam)

# opsv.plot_fiber_section(fiber_section_beam, matcolor=matcolor)
# plt.title("Beam Section")

# Column for all floor ------------------------------------------------------------

fiber_section_col = [

['section', 'Fiber', Col_SecTag, '-GJ', 1.0e6],
['patch', 'rect', confined_concrete_tag, 6, 6, *[-3.5 * inch, -3.5 * inch], *[3.5 * inch, 3.5 * inch]], # existing core

['patch', 'quad', confined_concrete_tag_retrofit, 4, 6, *[3.5*inch,-3.5*inch], *[8*inch,-8*inch], *[8*inch, 8*inch], *[3.5*inch,3.5*inch]], # right confined cover retrofit
['patch', 'quad', unconfined_concrete_tag_retrofit, 2, 6, *[8*inch,-8*inch], *[9*inch,-9*inch], *[9*inch, 9*inch], *[8*inch,8*inch]], # right unconfined cover retrofit

['patch', 'quad', confined_concrete_tag_retrofit, 4, 6, *[-8*inch,-8*inch], *[-3.5*inch,-3.5*inch], *[-3.5*inch,3.5*inch], *[-8*inch, 8*inch]], # left confined cover retrofit
['patch', 'quad', unconfined_concrete_tag_retrofit, 2, 6, *[-9*inch,-9*inch], *[-8*inch,-8*inch], *[-8*inch,8*inch], *[-9*inch, 9*inch]], # left unconfined cover retrofit

['patch', 'quad', confined_concrete_tag_retrofit, 6, 4, *[-3.5*inch,3.5*inch], *[3.5*inch,3.5*inch], *[8*inch, 8*inch], *[-8*inch,8*inch]], # top confined cover retrofit
['patch', 'quad', unconfined_concrete_tag_retrofit, 6, 2, *[-8*inch,8*inch], *[8*inch,8*inch], *[9*inch, 9*inch], *[-9*inch,9*inch]], # top unconfined cover retrofit

['patch', 'quad', confined_concrete_tag_retrofit, 6, 4, *[-8*inch,-8*inch], *[8*inch,-8*inch], *[3.5*inch,-3.5*inch], *[-3.5*inch,-3.5*inch]], # bottom confined cover retrofit
['patch', 'quad', unconfined_concrete_tag_retrofit, 6, 2, *[-9*inch,-9*inch], *[9*inch,-9*inch], *[8*inch,-8*inch], *[-8*inch,-8*inch]], # bottom unconfined cover retrofit

['layer', 'straight', steel_tag, 2, area(16), *[3.5 * inch, 3.5 * inch], *[3.5 * inch, -3.5 * inch]],   # right existin layer
['layer', 'straight', steel_tag, 2, area(16), *[-3.5 * inch, 3.5 * inch], *[-3.5 * inch, -3.5 * inch]], # left existing layer
['layer', 'straight', steel_tag, 2, area(12), *[0 * inch, 3.5 * inch], *[0 * inch, -3.5 * inch]],        # middle existing layer
      

['layer', 'straight', steel_tag_retrofit, 3, area(20), *[8*inch, 8*inch], *[8*inch, -8*inch]],   # right retrofit layer
['layer', 'straight', steel_tag_retrofit, 3, area(20), *[-8*inch, 8*inch], *[-8*inch, -8*inch]], # left retrofit layer
['layer', 'straight', steel_tag_retrofit, 2, area(20), *[0*inch, 8*inch], *[0*inch, -8*inch]]    # middle retrofit layer


]

opsv.fib_sec_list_to_cmds(fiber_section_col)

opsv.plot_fiber_section(fiber_section_col, matcolor=matcolor)
plt.title("Column Section for all floor ")





# Plotting of the sections ------------------------------------------------------------

plt.axis('equal')
plt.show()