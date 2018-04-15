/*
	Stack data structure implementation
*/
var Stack = (() => {
	// create a WeakMap() to store the stack items
	const sKey = {};
	const items = new WeakMap();

	// The Stack
	class Stack {
		constructor(){
			items.set(sKey, [])
		}
		// implement api methods
		push(element){
			let stack = items.get(sKey);
			stack.push(element);
		}
		pop(){
			let stack = items.get(sKey);
			return stack.pop();
		}
		peek(){
			let stack = items.get(sKey);
			return stack[stack.length - 1];
		}
		clear() {
			items.set(sKey, []);
		}
		size(){
			return items.get(sKey).length;
		}
	}
	return Stack;
})();