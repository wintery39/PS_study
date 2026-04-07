use std::io;

fn push_sort_vec(numbers: &mut Vec<usize>, new_number: usize, start: usize, end: usize) {
    if start >= end {
        numbers.push(new_number);
        return
    }
    
    let mid = (start + end) / 2;
    
    if numbers[mid] > new_number {
        if mid == 0 || numbers[mid-1] < new_number {
            numbers[mid] = new_number;
        } else {
            push_sort_vec(numbers, new_number, start, mid);
        }
    } else {
        push_sort_vec(numbers, new_number, mid + 1, end);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    
    let n: usize = input.trim().parse().unwrap();
    
    input.clear();
    
    let mut v: Vec<usize> = Vec::new();
    io::stdin().read_line(&mut input).unwrap();
    let iter = input.split_whitespace();
    
    
    for i in iter {
        let num: usize = i.parse().unwrap();
        let end: usize = v.len();
        push_sort_vec(&mut v, num, 0, end)
    }
    let result: usize = n - v.len();
    println!("{result}");
}