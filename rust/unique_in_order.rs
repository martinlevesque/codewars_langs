fn unique_in_order<T>(sequence: T) -> Vec<T::Item>
where
    T: std::iter::IntoIterator,
    T::Item: std::cmp::PartialEq + std::fmt::Debug,
{
    let mut result = vec![];

    for item in sequence {
        if result.last() != Some(&item) {
            result.push(item);
        }
    }

    return result;
}

fn main() {
    println!("{:?}", unique_in_order([1,2,2,3,3]))
}
