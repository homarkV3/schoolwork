use std::collections::HashMap;

fn slens(stuff: &Vec<String>) -> HashMap<String, usize> {
    todo!();
}

fn main() {
    let stuff = vec![
        String::from("A"),
        String::from("fine"),
        String::from("mess"),
    ];
    println!("{:?}", slens(&stuff));
    println!("{:?}", stuff);
}

/* Output:
{"fine": 4, "mess": 4, "A": 1}
["A", "fine", "mess"]
*/
