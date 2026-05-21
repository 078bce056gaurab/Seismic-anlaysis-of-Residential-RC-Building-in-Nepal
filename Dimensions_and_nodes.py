import openseespy.opensees as ops
import numpy as np
import matplotlib.pyplot as plt
import opsvis as opsv

ops.wipe()
ops.model('BasicBuilder', '-ndm', 3, '-ndf', 6)

#----------------------------------------------------------------------------------
# Geometry, Dimensions And Units (mm, s, N) , Global axes X, Y, Z (vertical) 
#----------------------------------------------------------------------------------

inch = 25.4
ft = 12. * inch
rigidDiaphragm = 1

# --------------------------------------------------------------------------------
# Nodes # ops.node(nodeTag, x, y, z)
# --------------------------------------------------------------------------------

# Floor 1 nodes ------------------------------------------------------------
ops.node(101, 0 , 0, 0)     
ops.node(102, 1600, 0, 0)
ops.node(103, 3200, 0, 0)
ops.node(104, 0, 1600, 0)
ops.node(105, 1600, 1600, 0)
ops.node(106, 3200, 1600, 0)
ops.node(107, 0, 3200, 0)
ops.node(108, 1600, 3200, 0)
ops.node(109, 3200, 3200, 0)
ops.node(110, 0, 4800, 0)
ops.node(111, 1600, 4800, 0)
ops.node(112, 3200, 4800, 0)
ops.node(113, 0, 6400, 0)
ops.node(114, 1600, 6400, 0)
ops.node(115, 3200, 6400, 0)




ops.fix(101, 1, 1, 1, 1, 1, 1)
ops.fix(102, 1, 1, 1, 1, 1, 1)
ops.fix(103, 1, 1, 1, 1, 1, 1)
ops.fix(104, 1, 1, 1, 1, 1, 1)
ops.fix(105, 1, 1, 1, 1, 1, 1)
ops.fix(106, 1, 1, 1, 1, 1, 1)
ops.fix(107, 1, 1, 1, 1, 1, 1)
ops.fix(108, 1, 1, 1, 1, 1, 1)
ops.fix(109, 1, 1, 1, 1, 1, 1)
ops.fix(110, 1, 1, 1, 1, 1, 1)
ops.fix(111, 1, 1, 1, 1, 1, 1)
ops.fix(112, 1, 1, 1, 1, 1, 1)
ops.fix(113, 1, 1, 1, 1, 1, 1)
ops.fix(114, 1, 1, 1, 1, 1, 1)
ops.fix(115, 1, 1, 1, 1, 1, 1)

floor_1_nodes = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115]

# Floor 2 nodes ------------------------------------------------------------
ops.node(201, 0 , 0, 2150)     
ops.node(202, 1600, 0, 2150)
ops.node(203, 3200, 0, 2150)
ops.node(204, 0, 1600, 2150)
ops.node(205, 1600, 1600, 2150)
ops.node(206, 3200, 1600, 2150)
ops.node(207, 0, 3200, 2150)
ops.node(208, 1600, 3200, 2150)
ops.node(209, 3200, 3200, 2150)
ops.node(210, 0, 4800, 2150)
ops.node(211, 1600, 4800, 2150)
ops.node(212, 3200, 4800, 2150)
ops.node(213, 0, 6400, 2150)
ops.node(214, 1600, 6400, 2150)
ops.node(215, 3200, 6400, 2150)

floor_2_nodes = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215]

# Floor 3 nodes ------------------------------------------------------------
ops.node(301, 0 , 0, 4300)     
ops.node(302, 1600, 0, 4300)
ops.node(303, 3200, 0, 4300)
ops.node(304, 0, 1600, 4300)
ops.node(305, 1600, 1600, 4300)
ops.node(306, 3200, 1600, 4300)
ops.node(307, 0, 3200, 4300)
ops.node(308, 1600, 3200, 4300)
ops.node(309, 3200, 3200, 4300)
ops.node(310, 0, 4800, 4300)
ops.node(311, 1600, 4800, 4300)
ops.node(312, 3200, 4800, 4300)
ops.node(313, 0, 6400, 4300)
ops.node(314, 1600, 6400, 4300)
ops.node(315, 3200, 6400, 4300)
floor_3_nodes = [301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315]

# Floor 4 nodes ------------------------------------------------------------
ops.node(401, 0 , 0, 6450)     
ops.node(402, 1600, 0, 6450)
ops.node(403, 3200, 0, 6450)
ops.node(404, 0, 1600, 6450)
ops.node(405, 1600, 1600, 6450)
ops.node(406, 3200, 1600, 6450)
ops.node(407, 0, 3200, 6450)
ops.node(408, 1600, 3200, 6450)
ops.node(409, 3200, 3200, 6450)
ops.node(410, 0, 4800, 6450)
ops.node(411, 1600, 4800, 6450)
ops.node(412, 3200, 4800, 6450)
ops.node(413, 0, 6400, 6450)
ops.node(414, 1600, 6400, 6450)
ops.node(415, 3200, 6400, 6450)
floor_4_nodes = [401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415]

# Floor 5 nodes ------------------------------------------------------------
ops.node(501, 0 , 0, 8600)     
ops.node(502, 1600, 0, 8600)
ops.node(503, 3200, 0, 8600)
ops.node(504, 0, 1600, 8600)
ops.node(505, 1600, 1600, 8600)
ops.node(506, 3200, 1600, 8600)
ops.node(507, 0, 3200, 8600)
ops.node(508, 1600, 3200, 8600)
ops.node(509, 3200, 3200, 8600)
ops.node(510, 0, 4800, 8600)
ops.node(511, 1600, 4800, 8600)
ops.node(512, 3200, 4800, 8600)
ops.node(513, 0, 6400, 8600)
ops.node(514, 1600, 6400, 8600)
ops.node(515, 3200, 6400, 8600)
floor_5_nodes = [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515]

# Master Nodes ------------------------------------------------------------

print("Rigid Diaphragm ON....")
ops.constraints('Transformation')
perp_direction = 3 

master_nodes = [1, 2, 3, 4, 5]

ops.node(1, 1600, 3200, 0)     # Master node for floor 1
ops.node(2, 1600, 3200, 2150)     # Master node for floor 2
ops.node(3, 1600, 3200, 4300)     # Master node for floor 3
ops.node(4, 1600, 3200, 6450)     # Master node for floor 4
ops.node(5, 1600, 3200, 8600)     # Master node for floor 5

# ops.rigidDiaphragm(perp_direction, master_nodeTag, *slaveNodeTags)
ops.rigidDiaphragm(perp_direction, 1, *floor_1_nodes)      
ops.rigidDiaphragm(perp_direction, 2, *floor_2_nodes) 
ops.rigidDiaphragm(perp_direction, 3, *floor_3_nodes) 
ops.rigidDiaphragm(perp_direction, 4, *floor_4_nodes)
ops.rigidDiaphragm(perp_direction, 5, *floor_5_nodes) 

# ops.fix(master_nodeTag, x, y, z, Mx, My, Mz)
ops.fix(1, 1, 1, 1, 1, 1, 1)       
ops.fix(2, 0, 0, 1, 1, 1, 0)       
ops.fix(3, 0, 0, 1, 1, 1, 0)      
ops.fix(4, 0, 0, 1, 1, 1, 0)     
ops.fix(5, 0, 0, 1, 1, 1, 0)