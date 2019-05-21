import UIKit

var array = [9, 1, 7, -1, 3, 2, 8, 5, 7, 6]

func bubbleSort(A: inout [Int]) {
    let indexStart = 0
    var indexEnd = A.count - 1
    
    while indexEnd > indexStart {
        for indexOfValueToCheck in (indexStart..<indexEnd) {
            if A[indexOfValueToCheck] > A[indexOfValueToCheck + 1] {
                swap(A: &A, i: indexOfValueToCheck, j: indexOfValueToCheck + 1)
                print(A)
            }
        }
        indexEnd -= 1
    }
}

func swap(A: inout [Int], i: Int, j: Int) {
    (A[i], A[j]) = (A[j], A[i])
}

bubbleSort(A: &array)
