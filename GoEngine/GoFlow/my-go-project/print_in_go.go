package main

import (
	"fmt"
)

func printFunc() {
	// Print messages to the console
	hello, world := "Hello", "World"

	fmt.Print(hello, world)
	fmt.Print(hello)
	fmt.Print(world)
	fmt.Print("\n--------default values---------------\n")
	fmt.Print(hello, "\n")
	fmt.Print(world, "\n")
	fmt.Print("---------added the next line values--------------\n")
	fmt.Print(hello, "\n", world)
	fmt.Print("\n--------White space---------------\n")
	fmt.Print(hello, " ", world)
}

func printlnFunc() {
	fmt.Println("\n", "--------println Function------------")
	message1, message2 := "Hello", "World"
	fmt.Println(message1, message2)
}

func printfFunc() {
	//%v is used to print the value of the arguments
	//%T is used to print the type of the arguments
	var i string = "Hello"
	var j int = 15
	fmt.Println("\n", "--------printf Function------------")
	fmt.Printf("i has value: %v and type: %T\n", i, i)
	fmt.Printf("j has value: %v and type: %T", j, j)
}

func printfFormat() {
	// %v	Prints the value in the default format
	// %#v	Prints the value in Go-syntax format
	// %T	Prints the type of the value
	// %%	Prints the % sign
	fmt.Println("\n", "--------printf Format Function------------")
	var i = 15.5
	var txt = "Hello World!"

	fmt.Printf("%v\n", i)
	fmt.Printf("%#v\n", i)
	fmt.Printf("%v%%\n", i)
	fmt.Printf("%T\n", i)

	fmt.Printf("%v\n", txt)
	fmt.Printf("%#v\n", txt)
	fmt.Printf("%T\n", txt)
}

// This function will print the Hello World message
func main() {
	//The Print() function prints its arguments with their default format.
	printFunc()
	//The Println() function is similar to Print() with the difference that a whitespace is added between the arguments, and a newline is added at the end:
	printlnFunc()
	//The Printf() function first formats its argument based on the given formatting verb and then prints them.
	printfFunc()
	//Some more formatting
	printfFormat()
}
