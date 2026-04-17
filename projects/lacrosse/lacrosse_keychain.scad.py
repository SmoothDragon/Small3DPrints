from solid import *
from solid.utils import *

# Load the STL file
stick = import_stl('lego_lacrosse_stick.stl')

# Manipulate it (e.g., move it 10 units on the X-axis)
# moved_object = translate([10, 0, 0])(my_object)
stick -= rotate([0,90,0])(translate([0,-4,-5])(rotate(22.5)(cylinder(r=1,h=10))))

# Render to an OpenSCAD (.scad) file
# scad_render_to_file(moved_object, 'output.scad')
print("$fn=8;")
print(scad_render(stick))

