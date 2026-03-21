use std::io;

fn main() {
    const Q: u64 = 1000000000;

    let mut input: String  = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let mut iter: std::str::SplitWhitespace<'_>     = input.split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    let k: usize = iter.next().unwrap().parse().unwrap();
 
    let mut prev: Vec<u64> = vec![1; n+1];
    let mut next: Vec<u64> = vec![0; n+1];


    for _ in 1..k {
        for norm_number in 0..n+1 {
            for target_number in norm_number..n+1 {
                next[target_number] = (next[target_number] + prev[norm_number]) % Q;
            }
        }

        std::mem::swap(&mut prev, &mut next);
        next.fill(0);
    }

    let result = prev[n];
    println!("{result}");
}
