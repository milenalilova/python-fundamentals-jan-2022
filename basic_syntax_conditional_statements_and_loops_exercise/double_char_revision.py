string = input()
double_string = ''

while string != "End":
    if string == "SoftUni":
        string = input()

    for ch in range(len(string)):
        double_string += 2 * string[ch]

    print(double_string)
    double_string = ''

    string = input()
