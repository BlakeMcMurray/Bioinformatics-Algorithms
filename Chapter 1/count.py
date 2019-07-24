def count(text,sub_string):
    count = 0
    for i in range(len(text)-len(sub_string)+1):
        if(text[i:i+len(sub_string)] == sub_string):
            count = count + 1
    return(count)



