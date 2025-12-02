try:
    with open("input.txt", 'r') as file:
        count_zero = 0
        number = 50
        for line in file:
            if line != "":
                value = line[1::]
                letter = line[0]
                if letter == "R":
                    number += int(value)
                else:
                    number -= int(value)
                number = number % 100
                if number == 0:
                    count_zero += 1
                print(letter, value, number)
        print(count_zero)


except FileNotFoundError:
    print("File not found error")
except Exception as e:
    print(f"Exception:  {e}")
