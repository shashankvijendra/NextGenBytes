package main

import "fmt"

var zz int

func multiple_variable_declare() {
	var a, b, c, d int = 1, 3, 5, 7

	fmt.Println("--multiple variable declare--")
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
}

func variables_declared_in_block() {
	fmt.Println("--variables declared in block--")
	var (
		a int
		b int    = 1
		c string = "hello"
	)

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}

// main is the entry point for the program
func main() {
	// Declare variable with string type
	var student1 string = "John"
	// Declare variable with type inferred
	var student2 = "Jane"
	// Declare variable with short variable declaration
	x := "Bob"
	// Declare variable with type inferred
	y := 1
	// Update global variable
	zz = 25
	// Declare variable without initialization
	var a int
	fmt.Println(student1, student2, x, y, a)
	// Value assignment
	var b, c int
	// Assign value to variable
	b = 100
	c = 1
	fmt.Println(b, c)
	fmt.Println("--global variables--")
	fmt.Println(zz)
	// Call functions
	multiple_variable_declare()
	variables_declared_in_block()

}
