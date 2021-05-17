
fn spin_words(words: &str) -> String {
    let result: Vec<String> =
        words
            .split(" ")
            .map(|word|
                format!("{:}",
                    if word.len() >= 5 {
                        word.chars().rev().collect::<String>()
                    }
                    else {
                        word.to_string()
                    }
                )
            )
            .collect();

    result.join(" ") 
}

fn main() {
    //let ss: Vec<String> = "asfd fd".split(" ").map(|word| format!("{:}", word) ).collect();
    
    //println!("{:?}", ss);
    println!("{:?}", spin_words("Just kidding there is still one more"))
}
