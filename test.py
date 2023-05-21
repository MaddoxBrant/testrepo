import pymapdl

# Create a new Ansys instance
mapdl = pymapdl.launch_mapdl()

# Define the 3D model geometry using mapdl commands
mapdl.prep7()
mapdl.et(1, 'SOLID186')
# ... more commands here ...

# Solve the model
mapdl.solve()

# Save the results to an RST file
mapdl.finish('/path/to/results.rst', 'db')



# download the pontoon example
from ansys.mapdl.reader import examples

print("%%%%%%%%%%%%%%%%%&))")
pontoon = examples.download_pontoon()
print(pontoon)
print("!!!!!!!!!!!!!!!!")
pontoon.plot_nodal_solution(0, show_displacement=True, displacement_factor=100000)
# print("*****************")
# pontoon.plot()
# print("&&&&&&&&&&&&&&&&&&&&")
# pontoon.plot_nodal_elastic_strain(
#     0,
#     "eqv",
#     show_displacement=True,
#     displacement_factor=100000,
#     overlay_wireframe=True,
#     lighting=False,
#     add_text=False,
#     show_edges=True,
# )
# print("$$$$$$$$$")