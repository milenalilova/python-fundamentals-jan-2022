word = input()
double_word = ""

while word != 'End':
    if word != 'SoftUni':
        for i in range(len(word)):
            double_word += 2 * word[i]
        print(double_word)
        double_word = ""

    word = input()
