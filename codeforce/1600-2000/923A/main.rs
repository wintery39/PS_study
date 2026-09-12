use std::io;

struct PrimeCalculator {
    primes_bool:Vec<bool>,
    primes: Vec<usize>
}

impl PrimeCalculator {
    fn new() -> Self {
        let mut primes_bool:Vec<bool> = vec![false; 1000001];
        let mut primes: Vec<usize> = vec![];
    
        for i in 2..=1000000 {
            if primes_bool[i] {
                continue
            }
            primes.push(i as usize);
            
            for j in ((i*2)..=1000000).step_by(i) {
                primes_bool[j] = true;
            }
        }
        
        Self { primes_bool, primes }
    }
    
    fn is_prime(&self, num: usize) -> bool {
        !self.primes_bool[num]
    }
    
    fn prime_factorization(&self, mut num: usize) -> Vec<usize> {
        let mut result: Vec<usize> = vec![];
        let mut idx: usize = 0;
        
        while num != 1 && self.primes[idx] * self.primes[idx] <= num{
            if num % self.primes[idx] == 0 {
                result.push(self.primes[idx]);
                num /= self.primes[idx]
            } else {
                idx += 1;
            }
        }
        
        if num != 1 {
            result.push(num);
        }
        result
    }    
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let x2: usize = input.trim().parse().unwrap();
    
    let calculator = PrimeCalculator::new();
    
    if calculator.is_prime(x2) {
        println!("{x2}");
        return
    }
    
    let x2_primes = calculator.prime_factorization(x2);
    let biggest_prime = x2_primes.last().unwrap();
    
    let x1s: Vec<usize> = ((x2-biggest_prime+1)..x2).collect();
    
    let mut result = x1s[0];
    
    for x1 in x1s {
        if calculator.is_prime(x1) {
            continue
        }
        
        let x1_primes = calculator.prime_factorization(x1);
        let biggest_prime = x1_primes.last().unwrap();
        result = result.min(x1-biggest_prime+1);
    }
    println!("{result}");
}