// called when page loads;sets up event handlers
window.onload = function () {
	var computeButton = document.getElementById("calcula").onclick = intlag;
};

// Calculate the Lagrange interpolationtyped into input boxes on the
//and displays the result in a span on the page
function intlag() {
	var inputcx = document.getElementById("coordx").value;
	var inputcy = document.getElementById("coordy").value;
	var x = document.getElementById("xint").value;
	var answer = document.getElementById("answer");

	var cx = inputcx.split(" ");
	var cy = inputcy.split(" ");

	var result = lagrange(cx, cy, x);
	answer.innerHTML = result;
}

function lagrange(cx, cy, x) {
	var suma = 0
	var prod;

	for (var j=0; j < cx.length ; j++)
	{
		prod=1;
		for (var i=0; i < cx.length ; i++)
		   if (i!=j)
			prod *= (x - cx[i])/(cx[j]-cx[i]);
		suma += prod * cy[j];
	}
	return suma;
	//Retorna el grado del polinomio.
}