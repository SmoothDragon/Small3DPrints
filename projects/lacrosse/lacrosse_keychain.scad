$fn=8;


difference() {
	import(file = "lego_lacrosse_stick.stl", origin = [0, 0]);
	rotate(a = [0, 90, 0]) {
		translate(v = [0, -4, -5]) {
			rotate(a = 22.5000000000) {
				cylinder(h = 10, r = 1);
			}
		}
	}
}
