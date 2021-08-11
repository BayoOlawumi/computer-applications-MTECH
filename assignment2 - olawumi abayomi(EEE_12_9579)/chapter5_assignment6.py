# Function created
def grade_maker(score):
    if score>75:
        return 'First'
    elif score<=75 and score >=70:
        return 'Upper Second'
    elif score>=60 and score <=70:
        return 'Second'
    elif score>=50 and score <=60:
        return 'Third'
    elif score>=45 and score <=50:
        return 'F1 Supp'
    elif score>=40 and score <=45:
        return 'F2'
    elif score<40:
        return 'F3'

xs = [83,75,74.9,70,69.9,65,60,59.9,55,50,49.9,45,44.9,40,39.9,2,0]
for each_score in xs:
        print("Score: {0}  - Grade: {1}".format(each_score, grade_maker(each_score)))


