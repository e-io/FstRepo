//this is game "Guess number"

package main

import(
  "fmt"
  "math/rand"
  "time"
)

func main() {
  rand.Seed(time.Now().UnixNano())
  counter, guess, number := 0, -1, rand.Intn(1000)

  fmt.Print("Guess the number between 1 and 1000\n")
  for  counter <= 1000 && guess != number{
    fmt.Print("_")
    fmt.Scanln(&guess)
    if guess != number {
      if guess < number {
        fmt.Println("Try >")
      } else {
        fmt.Println("Try <")
      }
      counter++
    }
    if guess == number {
      fmt.Println("You Won. steps:")
      fmt.Println(counter)
    }
  }
}
