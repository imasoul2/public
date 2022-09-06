def solution(id_list, report, k):
    
    # init as lists of zeroes
    reported_list = [0 for i in id_list]
    email_list = [0 for i in id_list]
    
    # remove duplicates
    report = list(set(report))
    
    # build reported_list
    for element in report:
        find_index = id_list.index(element.split(" ")[1])
        reported_list[find_index] +=1

    # re-visit the report
    for element in report:
        # find the number of reported   
        find_index = id_list.index(element.split(" ")[1])
        if reported_list[find_index] >= k:
            set_index = id_list.index(element.split(" ")[0])
            email_list[set_index] +=1
            
    answer = email_list

    return answer
