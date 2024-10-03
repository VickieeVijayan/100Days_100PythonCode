def calculate_love_score(name1, name2):
    
    combine = (name1+name2).lower()
    # print(combine)
    combine_list = list(combine)
    # print(combine_list)
    def calculate(word):
        total = 0
        for char in word:
            for letter in combine_list:
                if char == letter:
                    total += 1
                # print(total)
        return total
    True_Count = calculate("true")
    Love_Count = calculate("love")
    print(f"{True_Count}{Love_Count}")

calculate_love_score("Kanye West", "Kim Kardashian")