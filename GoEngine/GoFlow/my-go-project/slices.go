package main

import "fmt"

func declare_slice_with_datatype() {
	// Declare a slice without values
	fmt.Println("\033[34m Declare a slice with datatype \033[0m")
	myslice1 := []int{}

	fmt.Println(len(myslice1))
	fmt.Println(cap(myslice1))
	fmt.Println(myslice1)

	// Declare a slice with values
	myslice2 := []string{"Go", "Slices", "Are", "Powerful"}
	fmt.Println(len(myslice2))
	fmt.Println(cap(myslice2))
	fmt.Println(myslice2)

	start := 1
	end := 3
	myslice := myslice2[start:end]
	fmt.Println(myslice)

}

func declare_slice_with_array() {

	fmt.Println("\033[34m Declare a slice with ayrray \033[0m")
	arr1 := [6]int{10, 11, 12, 13, 14, 15}
	myslice := arr1[2:4]

	fmt.Printf("myslice = %v\n", myslice)
	fmt.Printf("length = %d\n", len(myslice))
	fmt.Printf("capacity = %d\n", cap(myslice))

}

func create_slice_from_func() {

	fmt.Println("\033[34m Create slice from func \033[0m")
	myslice1 := make([]int, 5, 10)
	fmt.Printf("myslice1 = %v\n", myslice1)
	fmt.Printf("length = %d\n", len(myslice1))
	fmt.Printf("capacity = %d\n", cap(myslice1))

	// with omitted capacity
	myslice2 := make([]int, 5)
	fmt.Printf("myslice2 = %v\n", myslice2)
	fmt.Printf("length = %d\n", len(myslice2))
	fmt.Printf("capacity = %d\n", cap(myslice2))
}

// main is the entry point of the program
func main() {
	// declare slice with datatype
	declare_slice_with_datatype()
	// declare slice with array
	declare_slice_with_array()
	// Create slice from func
	create_slice_from_func()
}
