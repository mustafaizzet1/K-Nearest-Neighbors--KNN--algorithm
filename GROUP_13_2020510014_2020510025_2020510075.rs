fn euclidean_distance(point1: &[f64], point2: &[f64]) -> f64 {
    if point1.len() != point2.len() {
        panic!("Points must have the same dimension");
    }

    let squared_diff_sum: f64 = point1.iter()
        .zip(point2.iter())
        .map(|(a, b)| (a - b).powi(2))
        .sum();

    squared_diff_sum.sqrt()
}

fn main() {
    let point1 = vec![3.0, 1.0, 2.0];
    let point2 = vec![2.0, 4.0, 6.0];
    println!("Euclidean Distance: {}", euclidean_distance(&point1, &point2));
}
