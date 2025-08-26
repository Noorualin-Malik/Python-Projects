numbers=[]
print("Welcome! You can enter number one by one and should type 'done' when you are finished")
while True:
    user=input("Enter a number or type 'done': ").strip().lower()
    if user=='done':
        break
    else:
        try:
            user_input= float(user)
            numbers.append(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
            continue

positive_numbers = [num for num in numbers if num > 0]
if positive_numbers==[]:
    print("No numbers were entered")
else :
    count = len(positive_numbers)
    total_sum = sum(positive_numbers)
    average = total_sum / count
    maximum = max(positive_numbers)
    minimum = min(positive_numbers)
    sorted_numbers = sorted(positive_numbers)

    if (count % 2) !=0:
        median = sorted_numbers[count // 2]
        print(f"Median of numbers is: {median}")
    else:
        num_1= sorted_numbers[(count // 2)-1]
        num_2= sorted_numbers[count // 2]
        print(f"Median of numbers is: {(num_1+num_2)/2}")
\
    # print(f"Count of numbers: {count}")
    # print(f"Sum of numbers: {total_sum}")
    # print(f"Average of numbers: {average}")
    # print(f"Maximum of numbers: {maximum}")
    # print(f"Minimum of numbers: {minimum}")

analysis_result={"Count": count, "sum": total_sum, "Average": average, "Maximum": maximum, "Minimum": minimum}
print(analysis_result)