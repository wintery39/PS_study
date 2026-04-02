use std::io;

fn pick_one(arr: &mut [bool; 9], idx: usize) {
    for i in 0..9 {
        if i == idx {
            continue;
        }

        arr[i] = false;
    }
}

fn has_first(arr: [bool; 9]) -> Option<usize> {
    let mut found: Option<usize> = None;

    for (idx, &val) in arr.iter().enumerate() {
        if val {
            if found.is_some() {
                return Some(10);
            }
            found = Some(idx);
        }
    }
    found
}


fn main() {
    let mut v: Vec<(usize, usize)> = Vec::new();

    for _ in 0..9 {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace();
        
        let a: usize = iter.next().unwrap().parse().unwrap();
        let b: usize = iter.next().unwrap().parse().unwrap();

        v.push((a, b-1));
    }

    let mut result: Option<usize> = None;
    
    for i in 0..9 {
        let mut arr = [true; 9];

        if v[i].0 == 0 {
            pick_one(&mut arr, v[i].1);
        } else {
            arr[v[i].1] = false;
        }

        
        for (idx, val) in v.iter().enumerate() {
            if idx == i {
                continue
            }
            
            if val.0 == 0 {
                arr[val.1] = false;
            } else if arr[val.1] {
                pick_one(&mut arr, val.1);
            } else {
                arr = [false; 9];
                break
            }
        }

        let found: Option<usize> = has_first(arr);

        if found.is_none() {
            continue
        }

        if found.unwrap() == 10 {
            result = None;
            break
        }

        if result.is_none() {
            result = found;
        } else {
            if result.unwrap() != found.unwrap() {
                result = None;
                break
            }
        }
    }

    if result.is_none() {
        println!("-1");
    } else {
        let p = result.unwrap() + 1;
        println!("{p}");
    }
}