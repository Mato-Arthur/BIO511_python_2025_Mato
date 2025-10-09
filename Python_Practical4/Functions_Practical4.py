# Provided inputs (use these)
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Globals to observe name masking (same-name local variables hides the global variable so use different variable names inside the function). Do not rename these.
count = 999
summary = "unset"
result = "unset"

def count_above(nums, limit):
    count = 0
    for num in nums:
        if num > limit:
            count += 1
    return count

print (count) 

print (count_above(nums, limit))


def summarize_text(s):
    summary = results_dict = { "digits": 0, "letters": 0, "others": 0 }
    for char in s: 
        if char.isdigit():
            summary["digits"] += 1
        elif char.isalpha():
            summary["letters"] += 1
        else:
            summary["others"] += 1
    return summary

print (summary)
print (summarize_text(text))


def aggregate(seq, mode, threshold):
    if mode == "sum": result = 0
    elif mode == "count": result = 0
    elif mode == "max": result = None 
    for n in seq: 
        if n < 0:
            continue 
        elif n > threshold:
            if mode == "sum":
                result += n  
            elif mode == "count":
                result += 1
            elif mode == "max":
                if result is None or n > result:
                    result = n
    return result
      
# e) Outside the function:
#    - Print the GLOBAL result.
print (result)
#    - Call and print each of these:
#         aggregate(nums, "sum", limit)
print (aggregate(nums, "sum", limit))
#         aggregate(nums, "count", limit)
print (aggregate(nums, "count", limit))
#         aggregate(nums, "max", limit)
print (aggregate(nums, "max", limit))
#    - Print the GLOBAL result again.
print (result) 