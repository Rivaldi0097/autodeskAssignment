def reverse_words(s: str) -> str:
    result = []
    i = 0
    n = len(s)

    while i < n:
        if s[i].isalnum():  # start of a word (letters or digits)
            j = i
            while j < n and s[j].isalnum(): # to prevent out of range index and to check if s[j] is still a letter/number
                j += 1
            # reverse the word
            result.append(s[i:j][::-1])
            i = j
        else:
            # non-word character, keep as-is
            result.append(s[i])
            i += 1

    return "".join(result)

if __name__ == "__main__":
    #test case 1
    test_str = "String; 2be reversed..."
    result = reverse_words(test_str)
    assert result == "gnirtS; eb2 desrever..."

    #test case 2
    test_str2 = "Such @ beauiful d@y!!!"
    result2 = reverse_words(test_str2)
    assert result == "hcuS @ lufiuaeb d@y!!!"