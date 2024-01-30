#Write a function that interleaves 2 strings. 
	#e.g.  string_1=AAAA,  string_2=1234567 -> output (interleaved_string) = A1A2A3A4567



def interleave_strings(string_1, string_2):
    interleaved_string = ''
    len_1, len_2 = len(string_1), len(string_2)
    min_len = min(len_1, len_2)

    for i in range(min_len):
        interleaved_string += string_1[i] + string_2[i]

    if len_1 > len_2:
        interleaved_string += string_1[min_len:]
    else:
        interleaved_string += string_2[min_len:]

    return interleaved_string


string_1 = "AAAA"
string_2 = "1234567"
result = interleave_strings(string_1, string_2)
print(result)
