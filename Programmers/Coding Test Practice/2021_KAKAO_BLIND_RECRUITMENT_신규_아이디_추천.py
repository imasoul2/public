import re
def solution(new_id):
    print(len(new_id))
    answer = ''
    # Step 1 : lower all cases
    temp_id = new_id.lower()
    # Step 2 : drop all invalid characters
    temp_id = re.sub('[^a-z._\-0-9]', '', temp_id)
    # Step 3 : replace .* to single .
    temp_id = re.sub('\.{2,}', '.', temp_id)
    # Step 4 : remove . at the start and end of string
    temp_id = re.sub('^\.', '', temp_id)
    temp_id = re.sub('\.$', '', temp_id)
    # Step 5 : check if temp_id is null
    if len(temp_id) == 0:
        temp_id += "a"
    # Step 6 : limit the chars to len of 15
    if len(temp_id) > 15:
        temp_id = temp_id[:15]
        temp_id = re.sub('\.$', '', temp_id)
    # Step 7 : if len() > 2, repeat 
    while len(temp_id) <= 2:
        temp_id += temp_id[-1]
        
    answer = temp_id
    return answer
