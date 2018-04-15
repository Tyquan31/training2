fun main(args: Array<String>) {
    // val is a constant that can not be changed (immutable)
    // read-only variable.
    // A val must be initialized when it is created, since it cannot be
    // changed later.
    // A read only variable does not mean the instance itself is automatically immutable. The
    // instance may still allow its member variables to be changed via functions or properties, but
    // the variable itself cannot change its value or be reassigned to another value.
    val name = "Kotlin"
    println(name)

    // Variables defined with var can be reassigned, since they are mutable:
    var newName = "New Kotlin"
    newName = "Not So Fast!"
    println(newName)

    /*

        Basic Types
        Numbers
        Booleans
        Chars
        Strings

    */
    // Numbers
    val int = 123
    val long = 123456L // requires L
    val double = 12.34 // used as the default for floating point numbers
    val float = 12.34F // requires F
    val hexadecimal = 0xAB
    val binary = 0b0101010101
    // Each number has a function that will convert the value to one of the other number types
    // toByte(), toShort(), toInt(), toLong(), toFloat(), toDouble(), toChar()
    val inty = 123
    val doubleInty = inty.toDouble()
    println(doubleInty)

    // Booleans
    val x = 1
    val y = 2
    val z = 2
    val isItTrue = x < y && x < z
    println(isItTrue)
    val alsoIsItTrue = x == y || y ==z
    println(alsoIsItTrue)

    // Strings (immutable)
    val string = "string with \nnew line"
    println(string)
    // strings can span many lines using the """
    val rawString = """
        raw string is useful for strings that span many lines."""
    println(rawString)

    /*

        Arrays

    */
    val myArray = arrayOf(1,2,3)
    println(myArray.size)
    for (k in myArray) {
        println(k)
    }
    // Alternative, create an Array from an initial size and a function, which is used
    // generate each element
    val perfectSquares = Array(10, { k -> k * k })
    for (k in perfectSquares) {
        println(k)
    }
    println(perfectSquares.size)
    println("\n")

    /*

        This
        When inside a class or function, we can refer to the enclosing instance
        This is the current receiver

    */
    class Person(private val name: String) {
        fun printMe() = println(this)
    }
    val person = Person("Tyquan")
    println(person.printMe())

    /*

        Scope
        In nested scopes, we may wish to refer to an outer instance. To do that, we must
        qualify the usage of this, and we do that using labels.

    */
    class Building(val address: String){
        inner class Reception(telephone: String) {
            //fun printAddress() = println(this.@Building.address)
        }
    }

}