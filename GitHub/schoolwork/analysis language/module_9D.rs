// semimap.rs: Uses as_ref

use std::cmp::Eq;
use std::collections::HashMap;
use std::hash::Hash;

#[derive(Debug)]
struct Semimap<K: Eq + Hash, V> {
    pairs: HashMap<K, Option<V>>,
}

impl<K, V> Semimap<K, V>
where
    K: Eq + Hash,
{
    fn new() -> Self {
        todo!()
    }
    fn insert_1(&mut self, key: K) {
        todo!()
    }
    fn insert_2(&mut self, key: K, value: V) {
        todo!()
    }
    fn pair_count(&self) -> usize {
        todo!()
    }
    fn sing_count(&self) -> usize {
        todo!()
    }
    fn get(&self, key: &K) -> Option<&V> {
        todo!()
    }
    fn keys(&self) -> Vec<&K> {
        todo!()
    }
    fn values(&self) -> Vec<&V> {
        todo!()
    }
    fn remove(&mut self, key: &K) {
        todo!()
    }
    fn contains_key(&self, key: &K) -> bool {
        todo!()
    }
}

fn main() {
    let mut mymap = Semimap::new();
    mymap.insert_2(1, String::from("one"));
    mymap.insert_1(2);
    println!("{:?}", &mymap);
    println!("{}", mymap.pair_count());
    println!("{}", mymap.sing_count());
    println!("{:?}", mymap.get(&1));
    println!("{:?}", mymap.keys());
    println!("{:?}", mymap.values());
    mymap.remove(&1);
    println!("{:?}", &mymap);
    println!("{}", mymap.contains_key(&1));
}

/* Output:
Semimap { pairs: {2: None, 1: Some("one")} }
1
1
Some("one")
[2, 1]
["one"]
Semimap { pairs: {2: None} }
false
*/
