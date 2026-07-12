# Write your solution here

def anagrams(string, string2):

    if sorted(string) == sorted(string2):

        return True
    
    else:

        return False

if __name__ == "__main__":

    anagrams('tame', 'mate')