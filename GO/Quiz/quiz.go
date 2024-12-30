package main

import "fmt"

func main() {
	var name string
	var age uint64
	var score int8

	fmt.Println("What's your name ?")
	fmt.Scan(&name)
	fmt.Println("What a funny name! \n")
	fmt.Println("How old are you ?")
	fmt.Scan(&age)

	if age <= 18 {
		fmt.Println("You are not old enough to play!")
		return

	} else if age >= 18 && age <= 127  {
		fmt.Printf("Welcome to my quiz %v. \n", name)
		question1(name, score)

	} else {
		fmt.Printf("You are too old to be alive %v...", name)
		return
	}
	
}

func question1(name string, score int8) {
	fmt.Printf("%v, what is better, Angular or React ? \n", name)
	var answer string
	fmt.Scan(&answer)

	if answer == "Angular" {
		fmt.Println("Incorrect")
		fmt.Printf("Score: %v \n", score)
		question2(name, score) 
	}
	if answer == "React" {
		fmt.Println("Correct")
		score := score + 1
		fmt.Printf("Score: %v \n", score) 
		question2(name, score)
	} else {
		fmt.Println("Please choose a valid answer")
		question1(name, score)
	}
}
func question2(name string, score int8) {
	fmt.Printf("%v, what is faster, Java or Python ? \n", name)
	var answer string
	fmt.Scan(&answer)

	if answer == "Python" {
		fmt.Println("Incorrect")
		fmt.Printf("Score: %v \n", score)
		question3(name, score) 
	}
	if answer == "Java" {
		fmt.Println("Correct")
		score := score + 1
		fmt.Printf("Score: %v \n", score) 
		question3(name, score)
	} else {
		fmt.Println("Please choose a valid answer")
		question2(name, score)
	}
}
func question3(name string, score int8) {
	fmt.Printf("%v, who have the cutest mascot, Go or Rust ? \n", name)
	var answer string
	fmt.Scan(&answer)

	if answer == "Rust" {
		fmt.Println("Incorrect")
		fmt.Printf("Score: %v \n", score)
	}
	if answer == "Go" {
		fmt.Println("Correct")
		score := score + 1
		fmt.Printf("Score: %v \n", score)
		fmt.Printf("You got %v/3", score) 
		var retry string
		
		if score == 3 {
			fmt.Println("You got the max score. Congratulations !!!")
			return 
		} else {
			fmt.Println("Do you want to retry ? (Y/N)")
			fmt.Scan(&retry)
			if retry == "Y" {
				main()
			} else {
				return
			}
		} 
		
	} else {
		fmt.Println("Please choose a valid answer")
		question3(name, score)
	}
}
