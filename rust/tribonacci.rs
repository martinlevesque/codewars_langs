
fn tribonacci(signature: &[f64; 3], n: usize) -> Vec<f64> {
    let mut result: Vec<f64> = [].to_vec();
    let mut current_signature = signature.clone().to_vec();

    for _i in 0..n {
        result.push(current_signature[0]);

        let new_value = current_signature[0] + current_signature[1] + current_signature[2];

        current_signature.remove(0);
        current_signature.push(new_value);
    }
    
    result
}

fn main() {
    println!("{:?}", tribonacci(&[3., 2., 1.], 100))
}