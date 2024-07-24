n = int(input())
animal_sounds = []
for _ in range(n):
    test = input().split()
    while True:
        line = input()
        if line == 'what does the fox say?':
            break
        animal, goes, sound = line.split()
        animal_sounds.append(sound)
    
    for sound in test:
        if sound not in animal_sounds:
            print(sound, end=' ')
    
