package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var a int
	var b string
	fmt.Scanf("%d%d%d", &a)
	b = strconv.Itoa(a)
	fmt.Println(strings.Count(b, "1"))
}
