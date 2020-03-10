## phy211 grade calculator
## made by justin gluska
## all information taken from walterfreeman.github.io/phy211/syllabus.html

#####
# enter grades below
#####

#exam3 = (dropped lowest exam grade, don't include your lowest in the calcuation)

hwork = 100
exam1 = 100
exam2 = 100
final = 100
recit = 100
group = 100
paper = 100
prlec = 100

# homework is all homework grades combined
# exam1 & exam2 are your highest exam grades
# final is the exam taken on May 4th
# recitation grade is participation throughout the semester
# group exams are the average of all 3 group exams from recitation
# paper is the paper on the nature of science, taken from syllabus
# prelecture quizzes (pass [100] /fail [0]) grade

# grade calculation - do not edit
grade = (hwork*0.1923076923)+(exam1*0.1153846154)+(exam2*0.1153846154)+(final*0.2307692308)+(recit*0.07692307692)+(group*0.1153846154)+(paper*0.1153846154)+(prlec*0.03846153846)
chart = "\nA : >88\nA-: 80-88\nB+: 75-80\nB : 70-75\nB-: 65-70\nC+: 62-64\nC : 58-62\nC-: 55-58\nD : 50-55\nF : less than 50"
print("final grade: ", ((grade*1.3)/130)*100, "\n", chart)
# grade calculation - do not edit