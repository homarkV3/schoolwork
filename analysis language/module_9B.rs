// module_9B.rs: fill in the missing code below.
use std::f64::EPSILON;

#[derive(Debug)]
struct Sqrt {
    number: f64,
    guess: f64,
}

impl Sqrt {
    // Associated function to create a new instance of Sqrt
    fn new(number: f64, initial_guess: f64) -> Self {
        Sqrt {
            number,
            guess: initial_guess,
        }
    }
}

impl Iterator for Sqrt {
    type Item = f64;

    // Implementing the Newton's method for square root approximation
    fn next(&mut self) -> Option<Self::Item> {
        if self.guess == 0.0 {
            return None; // Avoid division by zero
        }

        let new_guess = (self.guess + self.number / self.guess) / 2.0;
        let result = Some(self.guess);
        self.guess = new_guess;
        result
    }
}

// Function to find the square root using an iterator, stopping when successive guesses are within std::f64::EPSILON
fn iterate(iter: &mut impl Iterator<Item = f64>) -> f64 {
    let mut prev_guess = if let Some(initial_guess) = iter.next() {
        initial_guess
    } else {
        return 0.0; // Return 0.0 if iterator is initially empty
    };

    for guess in iter {
        if (guess - prev_guess).abs() < std::f64::EPSILON {
            return guess;
        }
        prev_guess = guess;
    }

    prev_guess // In case the convergence condition is never met within the provided iterations
}
fn main() {
    let mut iter = Sqrt::new(2.0, 1.0);
    for _ in 0..5 {
        println!("{}", iter.next().unwrap());
    }
    println!("");
    println!("{}", iterate(&mut iter)); // 1.414213562373095 
    println!("{:?}", iter);  
}

/* Output:
1
1.5
1.4166666666666665
1.4142156862745097
1.4142135623746899

1.414213562373095
Sqrt { number: 2.0, guess: 1.414213562373095 }
*/
