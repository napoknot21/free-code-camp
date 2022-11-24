function area (side1, side2, side3) {
	var somm = (side1, side2, side3)/2;
	var area = Math.sqrt(somm*((somm-side1)*(somm-side2)*(somm-side3)));
	return area
}

console.log(area(5, 6, 7))
