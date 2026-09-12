use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();
    
    let t: usize = iter.next().unwrap().parse().unwrap();
    for _ in 0..t {
        let n: usize = iter.next().unwrap().parse().unwrap();
        let mut left_operations: Vec<(bool, usize)> = vec![];
        let mut right_operations: Vec<(bool, usize)> = vec![];
        
        for _ in 0..n {
            let left_operator = iter.next().unwrap();
            let left_a = iter.next().unwrap().parse().unwrap();
            
            let right_operator = iter.next().unwrap();
            let right_a = iter.next().unwrap().parse().unwrap();
            
            left_operations.push((left_operator == "x", left_a));
            right_operations.push((right_operator == "x", right_a));
        }
        
        let mut directions: Vec<bool> = vec![true; n];
        let mut current_direction: bool = true;
        let mut idx = n - 1;
        
        while idx > 0 {
            idx -= 1;
            let next = idx + 1;
            
            if left_operations[next].0 && right_operations[next].0 {
                directions[idx] = left_operations[next].1 > right_operations[next].1;
                
                if left_operations[next].1 == right_operations[next].1 {
                    directions[idx] = current_direction;
                }
            } else if left_operations[next].0 || right_operations[next].0 {
                directions[idx] = left_operations[next].0
            } else {
                directions[idx] = current_direction;
            }
            current_direction = directions[idx];
        }
        
        let mut left = 1;
        let mut right = 1;
        
        for i in 0..n {
            let mut addition = 0;
            
            if left_operations[i].0 {
                addition += left * (left_operations[i].1 - 1)
            } else {
                addition += left_operations[i].1
            }
            
            if right_operations[i].0 {
                addition += right * (right_operations[i].1 - 1)
            } else {
                addition += right_operations[i].1
            }
            
            if directions[i] {
                left += addition;
            } else {
                right += addition;
            }
        }
        let result = left + right;
        println!("{result}");
    }
}