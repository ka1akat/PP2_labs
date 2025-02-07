def spy_game(nums):
    found_zero = False
    for num in nums:
        if num == 0 and not found_zero:
            found_zero = True 
        elif num == 0 and found_zero:
            found_zero = "found_second_zero"  
        elif num == 7 and found_zero == "found_second_zero":
            return True  
    return False 


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False
