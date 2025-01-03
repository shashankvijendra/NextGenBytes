package main

import "fmt"

func add_number() {
	fmt.Println("\033[34m Add number \033[0m")
	var a int = 10 + 20
	fmt.Println(a)

	fmt.Println("\033[34m add number with another variable \033[0m")
	var (
		sum1 = 100 + 50    // 150 (100 + 50)
		sum2 = sum1 + 250  // 400 (150 + 250)
		sum3 = sum2 + sum2 // 800 (400 + 400)
	)

	fmt.Println(sum1, sum2, sum3)
}

func subtract_number() {
	fmt.Println("\033[34m Subtract number \033[0m")
	var a int = 10 - 20
	fmt.Println(a)
	fmt.Println(a - 1)
}

func multiply_number() {
	fmt.Println("\033[34m Multiply number \033[0m")
	var a int = 10 * 20
	fmt.Println(a)
	var b int = a * 3
	fmt.Println(b)
}

func divide_number() {
	fmt.Println("\033[34m Divide number \033[0m")
	var a int = 100 / 20
	fmt.Println(a)
	var b int = a / 3
	fmt.Println(b)
	fmt.Println("\033[34m Moduus number \033[0m")
	var c int = 100 % 21
	fmt.Println(c)
}

func increment_number() {
	fmt.Println("\033[34m Increment number \033[0m")
	a := 10
	fmt.Println(a)
	a++
	fmt.Println(a)
}

func decrement_number() {
	fmt.Println("\033[34m Decrement number \033[0m")
	b := 10
	fmt.Println(b)
	b--
	fmt.Println(b)
}

func arithmetic_operations() {
	fmt.Println("\033[32m Arithmetic operations \033[0m")
	// add Numbers
	add_number()
	// subtract Number
	subtract_number()
	// multiply Number
	multiply_number()
	// divide Number
	divide_number()
	// increment Number
	increment_number()
	// decrement Number
	decrement_number()

}

func assignment_operator() {
	fmt.Println("\033[32m Assignment operations \033[0m")
	var x = 10
	fmt.Printf("x initial value : %d\n", x)
	x += 5
	fmt.Printf("x after increment : %d\n", x)
	var v = 5
	fmt.Printf("v initial value : %b \n", v) // 101

	v >>= 3

	fmt.Printf("v now is %03b \n", v) // 000

}

func main() {
	// arithmetic operations
	arithmetic_operations()
	// assignment operator
	assignment_operator()
}
