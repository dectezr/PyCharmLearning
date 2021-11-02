args = sys.argv

# further code of the script "add_four_numbers.py"
number_list = [int(x) for x in args[1:4]]
print(sum(number_list))
