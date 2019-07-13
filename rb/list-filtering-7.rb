def filter_list(l)
  # return a new list with the strings filtered out
  l.select{ |item| ! item.is_a? String }
end

p filter_list([2,3,'234',4])
