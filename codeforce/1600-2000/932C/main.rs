use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    let a: usize = iter.next().unwrap().parse().unwrap();
    let b: usize = iter.next().unwrap().parse().unwrap();

    let small: usize = a.min(b);
    let big: usize = b.max(a);

    let mut small_nums: usize = n / small + 1;
    let mut big_nums: usize = 0;
    
    let mut sum: usize = small * small_nums + big * big_nums;

    while sum != n { 
        if sum > n {
            if small_nums == 0 {
                break
            }
            
            small_nums -= 1;
        }

        if sum < n {
            big_nums += 1;
        }

        sum = small * small_nums + big * big_nums;
    }

    if sum != n {
        println!("-1");
    }
    else {
        let mut num: usize = 1;

        while num <= n {
            if small_nums != 0 {
                for extra_num in 1..=small {
                    let result = num + (extra_num % small);
                    print!("{result} ");
                }
                small_nums -= 1;
                num += small;
            }
            else {
                for extra_num in 1..=big {
                    let result = num + (extra_num % big);
                    print!("{result} ");
                }
                num += big;
            }
        }
        
    }
}