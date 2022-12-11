text = "C:/Users/vigne/Downloads/wordle.txt"
f= open(text)
f = f.readlines()
f = [x.strip('\n') for x in f]
def permutations_generator(s: str) -> int:

    unique_words = set()


    def generate_permutations(s: str, prefix: str):
        if len(prefix) == 5:
            unique_words.add(prefix)
            return

        for i, c in enumerate(s):
            generate_permutations(s[:i] + s[i+1:], prefix + c)

    generate_permutations(s, '')
    return unique_words
def exercise8(input_string):
    counter = 0
    anagrams = []
    flag = 0
    perms = permutations_generator(input_string)
    subset = set(f) & set(perms)
    return len(subset)
print(exercise8("caarto"))