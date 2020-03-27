# 665. Non-decreasing nums
nums = [1,2,3]

prev_value = -1
count = 0
nums.each_with_index do |num, index|
  p "prev num #{prev_value}"
  p "current number #{num}"
  p "next number #{nums[index + 1]}"
  p "index #{index}"

  if nums[index + 1] == nil
    "We're at at last numbber!"
    p count > 1 ? false : true
    return
  end

  # If next number is greater than current number, count++ and change current number
  if nums[index + 1] < num || (nums[index + 1] < num && num < prev_value)
    p "next number is less than current number"
    count += 1
  end

  if count > 1
    p "count greater than 1"
    p "false"
    return false
  end
  p "count #{count}"
  puts
  prev_value = num
end
p "true"
return true