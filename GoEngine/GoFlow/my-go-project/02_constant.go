package main

import (
	"fmt"
)

const PI = 3.14 // Untyped constant
const A int = 1 // Typed constant
const (
	D int = 1
	B     = 3.14
	C     = "Hi!"
)

func main() {
	fmt.Println(PI)
	fmt.Println(A)
	// Multiple constance declaration
	fmt.Println(D, B, C)
}
