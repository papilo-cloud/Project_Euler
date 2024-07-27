def letters(number):
    ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
            17: "seventeen", 18: "eighteen", 19: "nineteen",
    }
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }
    
    if number in ones:
        return ones[number]
    if number >= 20 and number < 100:
        return tens[number // 10] + ('' if number%10 == 0 else ones[number%10])
    
    if number >= 100 and number < 1000:
        suffix = ''
        if number % 100 > 19:
            suffix = ' and ' + tens[number%100//10] + ('' if number%100%10 == 0 else ones[number%100%10])
        elif number % 100 < 20 and number%100 != 0:
            suffix = ' and ' + ones[number%100]
        
        return ones[number // 100] + ' hundred' + suffix
    if number  == 1000:
        return ones[number // 1000] + ' thousand'
    
    

def letter_count(num):
    num_list = [''.join(letters(index).strip().split(' ')) for (index) in range(1, num)]
    return len(''.join(num_list))

print(letter_count(1001))