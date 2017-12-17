from survey import AnonymousSurvey

question = "What langague did you first learn to speak? "
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' to leave at any time. ")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThanks everyone who participate in the survey! ")
my_survey.show_results()
