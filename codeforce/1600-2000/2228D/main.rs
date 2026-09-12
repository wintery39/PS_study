use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let t: usize = iter.next().unwrap().parse().unwrap();
    
    for _ in 0..t {
        let n: usize = iter.next().unwrap().parse().unwrap();

        let mut input_coordinates: Vec<(usize, usize)> = vec![];

        for _ in 0..n {
            let x: usize = iter.next().unwrap().parse().unwrap();
            let y: usize = iter.next().unwrap().parse().unwrap();

            input_coordinates.push((x, y));
        }
        input_coordinates.sort();

        let mut ranked_x_coordinates: Vec<(usize, usize)> = vec![];
        let mut current_x = input_coordinates[0].0;
        let mut ranked_x = 0;

        for (x, y) in input_coordinates {
            if current_x != x {
                current_x = x;
                ranked_x += 1;
            }
            ranked_x_coordinates.push((ranked_x, y));
        }
        ranked_x_coordinates.sort_by_key(|coordinate| coordinate.1);

        let mut ranked_coordinates: Vec<(usize, usize)> = vec![];
        let mut current_y = ranked_x_coordinates[0].1;
        let mut ranked_y = 0;
        let mut right_ys: Vec<usize> = vec![];

        for (ranked_x, y) in ranked_x_coordinates {
            if current_y != y {
                current_y = y;
                ranked_y += 1;
            }
            if ranked_y == right_ys.len() {
                right_ys.push(0);
            }
            right_ys[ranked_y] += 1;
            ranked_coordinates.push((ranked_x, ranked_y));
        }

        ranked_coordinates.sort();

        let mut left_min: usize = ranked_coordinates[0].1;
        let mut left_max: usize = ranked_coordinates[0].1;

        let mut right_min: usize = 0;
        let mut right_max: usize = ranked_y;

        let mut current_x = ranked_coordinates[0].0;
        
        let mut result = 0;

        for (x, y) in ranked_coordinates {
            if current_x != x {
                while right_ys[right_min] == 0 {
                    right_min += 1;
                }

                while right_ys[right_max] == 0 {
                    right_max -= 1;
                }

                let bottom: usize = left_min.max(right_min);
                let top: usize = left_max.min(right_max);

                if top > bottom {
                    result += top - bottom;
                }

                current_x = x;
            }

            right_ys[y] -= 1;
            left_min = left_min.min(y);
            left_max = left_max.max(y);
        }

        println!("{result}");
    }
}