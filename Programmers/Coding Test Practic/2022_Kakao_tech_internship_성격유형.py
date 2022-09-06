# 2022 KAKAO TECH INTERNSHIP
# 성격 유형 검사하기
def solution(survey, choices):
    
    # Init dict to store the value of personality trait
    personality_dict = {"R":0,"T":0,"C":0,"F":0, "J":0,"M":0, "A":0, "N":0}
    # Default personality trait
    personality_result = "RCJA"
    
    # For each element on the survey
    for i in range(0,len(survey)):
        personality= survey[i]
        score = choices[i]
        # Update the score of each personality trait according to the (choice - 4)
        if score > 4:
            personality_dict[personality[1]]+=abs(score-4)
        elif score < 4:
            personality_dict[personality[0]]+=abs(score-4)
            
    # Based on the dictionary, build the final personality trait
    if personality_dict["T"] > personality_dict["R"]:
        personality_result=personality_result.replace("R","T")
    if personality_dict["F"] > personality_dict["C"]:
        personality_result=personality_result.replace("C","F")        
    if personality_dict["M"] > personality_dict["J"]:
        personality_result=personality_result.replace("J","M")       
    if personality_dict["N"] > personality_dict["A"]:
        personality_result=personality_result.replace("A","N")      
        
    answer = personality_result
    print(answer)
    return answer
