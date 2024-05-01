def compress(chars: list[str]) -> int:
    i = 0
    n = len(chars)
    ans_index = 0

    while(i<n):
        j = i+1
        while(j<n and chars[i] == chars[j]):
            j+=1
        
        print(ans_index,i)
        chars[ans_index] = chars[i]
        ans_index += 1
        
        count = j - i

        if count>1:
            for c in str(count):
                chars[ans_index]=c
                ans_index += 1
        # print(chars)
        i = j

    print(chars)
    print(ans_index)




chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(chars)
compress(chars)