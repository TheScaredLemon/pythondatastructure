def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    vowels_in_s = [char for char in s if char in vowels]
    reversed_vowels = vowels_in_s[::-1]
    result = []
    vowel_index = 0
    
    for char in s:
        if char in vowels:
            result.append(reversed_vowels[vowel_index])
            vowel_index += 1
        else:
            result.append(char)
    
    return ''.join(result)
