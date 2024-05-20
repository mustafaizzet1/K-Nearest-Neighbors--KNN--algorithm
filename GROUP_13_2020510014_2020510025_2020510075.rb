def euclidean_distance(point1, point2)
  if point1.length != point2.length
    raise "Points must have the same dimension"
  end

  squared_diff_sum = point1.zip(point2).map { |a, b| (a - b) ** 2 }.sum
  Math.sqrt(squared_diff_sum)
end

point1 = [3.0, 1.0, 2.0]
point2 = [2.0, 4.0, 6.0]
puts "Euclidean Distance: #{euclidean_distance(point1, point2)}"
