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

func arrayIndex() {
	prices := [3]int{10, 20, 30}
	fmt.Println("Array index")
	fmt.Println(prices[0])
	fmt.Println(prices[2])
}

func arrayInitialization() {
	arr1 := [5]int{}              //not initialized
	arr2 := [5]int{1, 2}          //partially initialized
	arr3 := [5]int{1, 2, 3, 4, 5} //fully initialized

	fmt.Println("Array initialization")
	fmt.Println(arr1)
	fmt.Println(arr2)
	fmt.Println(arr3)
}

func arrayInitializeOnlySpecificElements() {
	arr1 := [5]int{1: 10, 2: 40, 4: 1}

	fmt.Println("Array initialization only specific elements")
	fmt.Println(arr1)
}

func arrayLength() {
	arr1 := [4]string{"Volvo", "BMW", "Ford", "Mazda"}
	arr2 := [...]int{1, 2, 3, 4, 5, 6}
	fmt.Println("Array length")
	fmt.Println(len(arr1))
	fmt.Println(len(arr2))
}

// main is the entry point of the program
func main() {
	// Demonstrate array with fixed length
	arrayWithFixedLength()
	// Demonstrate array with dynamic length
	defineDynamicLengthArrays()
	// Demonstrate array with string elements
	arrayWithString()
	//Array with index
	arrayIndex()
	//Array initialization
	arrayInitialization()
	//Array initialize only specific elements
	arrayInitializeOnlySpecificElements()
	// Find the len of the array
	arrayLength()
}
