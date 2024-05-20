package main

import (
	"fmt"
	"math"
)

func euclideanDistance(point1, point2 []float64) float64 {
	if len(point1) != len(point2) {
		panic("Points must have the same dimension")
	}

	squaredDiffSum := 0.0
	for i := range point1 {
		squaredDiffSum += math.Pow(point1[i]-point2[i], 2)
	}

	return math.Sqrt(squaredDiffSum)
}

func main() {
	point1 := []float64{3.0, 1.0, 2.0}
	point2 := []float64{2.0, 4.0, 6.0}
	fmt.Println("Euclidean Distance:", euclideanDistance(point1, point2))
}
