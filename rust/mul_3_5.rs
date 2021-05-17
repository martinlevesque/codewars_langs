
fn solution(num: i32) -> i32 {
  (1..(num))
    .map(|x| if x % 3 == 0 || x % 5 == 0 { x } else { 0 })
    .sum()
}

fn main() {
    println!("{:?}", solution(6))
}