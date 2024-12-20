package main

import (
	"fmt"
)

// arrayWithFixedLength demonstrates the declaration of arrays with fixed lengths
func arrayWithFixedLength() {
	// Declare an array of integers with a fixed length of 3
	var arr1 = [3]int{1, 2, 3}

	// Declare an array of integers with a fixed length of 5
	arr2 := [5]int{4, 5, 6, 7, 8}

	// Print the arrays
	fmt.Println(arr1)
	fmt.Println(arr2)
}

func defineDynamicLengthArrays() {
	numbers1 := [...]int{1, 2, 3}
	numbers2 := [...]int{4, 5, 6, 7, 8}

	fmt.Println(numbers1)
	fmt.Println(numbers2)
}

func arrayWithString() {
	cars := [4]string{"Volvo", "BMW", "Ford", "Mazda"}
	fmt.Println(cars)
}

// main is the entry point of the program
func main() {
	// Demonstrate array with fixed length
	arrayWithFixedLength()
	// Demonstrate array with dynamic length
	defineDynamicLengthArrays()
	// Demonstrate array with string elements
	arrayWithString()
}
