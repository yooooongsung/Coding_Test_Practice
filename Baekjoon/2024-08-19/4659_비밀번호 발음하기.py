def is_acceptable(password):
    vowels = 'aeiou'
    vowel_count = 0
    consonant_count = 0
    prev_char = ''
    has_vowel = False  # 모음이 포함되었는지 확인하는 플래그

    for char in password:
        if char in vowels:
            has_vowel = True  # 모음 발견
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0
        
        # Check for three consecutive vowels or consonants
        if vowel_count == 3 or consonant_count == 3:
            return False
        
        # Check for repeated characters
        if char == prev_char:
            if char not in ['e', 'o']:  # Only allow 'ee' and 'oo'
                return False
        prev_char = char

    # Must contain at least one vowel
    return has_vowel

while True:
    password = input().strip()
    if password == 'end':
        break

    if is_acceptable(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
