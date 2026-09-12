use std::io::{self, Read};

fn is_substring(arr1: &Vec<u8>, arr2: &Vec<u8>) -> bool {
    let length: usize = arr1.len().min(arr2.len());

    for idx in 0..length {
        if arr1[idx] != arr2[idx] {
            return false
        }
    }
    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();

    let mut strings: Vec<Vec<u8>> = vec![vec![]; 26];
    let mut used_chars: Vec<bool> = vec![false; 26];

    for _ in 0..n {
        let input_string: Vec<u8> = iter.next().unwrap().trim().as_bytes().to_vec();
        let alpha_to_num: usize = (input_string[0] - b'a') as usize;

        if !is_substring(&strings[alpha_to_num], &input_string) {
            println!("NO");
            return
        }
        
        if strings[alpha_to_num].len() < input_string.len() {
            strings[alpha_to_num] = input_string;
        }
    }

    let mut idx = 0;

    while idx < strings.len() {
        if strings[idx].len() == 0 || used_chars[idx] {
            idx += 1;
            continue
        }

        let mut string_idx: usize = 1;
        while string_idx < strings[idx].len() {
            let alpha_to_num: usize = (strings[idx][string_idx] - b'a') as usize;
            let current_string: Vec<u8> = strings[idx][string_idx..].to_vec();

            if used_chars[alpha_to_num] || !is_substring(&current_string, &strings[alpha_to_num]) {
                println!("NO");
                return
            }
            used_chars[alpha_to_num] = true;

            let current_length: usize = current_string.len();
            let compare_length: usize = strings[alpha_to_num].len();
            
            for i in current_length..compare_length {
                let value: u8 = strings[alpha_to_num][i];

                strings[idx].push(value);
            }
            
            if alpha_to_num < idx {
                string_idx += compare_length.max(1);
            } else {
                string_idx += 1;
            }
        }
        idx += 1;
    }

    for (idx, string) in strings.iter().enumerate() {
        if used_chars[idx] {
            continue
        }
        
        let origin_string = String::from_utf8(string.to_vec()).unwrap();

        print!("{origin_string}");
    }
    println!();
}