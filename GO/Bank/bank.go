package main

import "fmt"

func main() {
	fmt.Println("What's your name ?")
	var name string
	fmt.Scan(&name)
	fmt.Printf("Welcome to my quiz game %v.", name)
}
