// Understanding the arguments parameter

function sayHi(){
	// arguments is dictionary object
	// where you can access whatever is passed into a function
	return arguments;
}
console.log(sayHi("Ty", "Lets Go", "This also shows"));

function shopping(){
	if (arguments.length >= 2) {
		console.log("You get a 20% discount");
	} else if (arguments.length <= 1) {
		console.log("Not eligible for any discount");
	}
}

shopping("Milk", "Bread");