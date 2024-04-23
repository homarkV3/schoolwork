// module_9A.rs: Fill in the 3 function bodies below.

fn squarelist(v: &Vec<i32>) -> Vec<i32> {

}

fn sqsum(v: &Vec<i32>) -> i32 {

}

fn compose_n<'a, T>(funs: &'a [fn(T) -> T]) -> impl Fn(T) -> T + 'a {

}

fn main() {
    let v = vec![1,2,3,4];
    println!("{:?}", squarelist(&v));
    println!("{:?}", sqsum(&v));

    // Test compose_n
    fn add1(n: i32) -> i32 {
        n+1
    }
    fn square(n: i32) -> i32 {
        n*n
    }
    fn div2(n: i32) -> i32 {
        n / 2
    }

    // Use an array
    let a: [fn(i32) -> i32; 3] = [add1, square, div2];
    let f = compose_n(&a);
    println!("{}", f(10)); // 26
    let a: [fn(i32) -> i32; 0] = [];
    let f = compose_n(&a);
    println!("{}", f(10)); //10

    // Use strings
    fn add_s(s: String) -> String {
        format!("{}s", s)
    }
    fn add_tick(s: String) -> String {
        format!("{}'", s)
    }

    // Use a vector
    let v: Vec<fn (String) -> String> = vec![add_s, add_tick];
    let f = compose_n(&v);
    println!("{}", f("John".to_string())); // John's
    let v: Vec<fn (String) -> String> = vec![];
    let f = compose_n(&v);
    println!("{}", f("John".to_string())); // John
}

/* Output:
[1, 4, 9, 16]
30
26
10
John's
John
*/
