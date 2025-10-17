from bonus12_function import parse_input , convert

feet_inches = input("Enter feet and inches ")



f,i = parse_input(feet_inches)

print(f,i)
result_total = convert(f, i)

if result_total < 1:
    print("Less than a meter")
else:
    print(result_total)

