def summation(num)
  (1..num).inject(0) { |sum, e| sum + e }
end

p summation(2)
p summation(8)
