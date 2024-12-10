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

func main() {
	var student1 string = "John"
	var student2 = "Jane"
	x := "Bob"
	y := 1
	zz = 25
	// Variable without initialization
	var a int
	fmt.Println(student1, student2, x, y, a)
	// Valus assignment
	var b, c int
	b = 100
	c = 1
	fmt.Println(b, c)
	fmt.Println("--global variables--")
	fmt.Println(zz)
	multiple_variable_declare()

}
