# Example data for five tests
test1 = ["12345:80", "67890:70"]
test2 = ["12345:85", "67890:75"]
test3 = ["12345:90", "67890:80"]
test4 = ["12345:95", "67890:85"]
test5 = ["12345:100", "67890:90"]

# Create a dictionary to store the student numbers and their test scores
student_scores = {}

# Iterate over the data for each test
for test_data in [test1, test2, test3, test4, test5]:
    # Iterate over the data for this test
    for item in test_data:
        # Split the item into its components
        student_number, score = item.split(":")
        
        # Convert the score to an integer
        score = int(score)
        
        # Add the score to the list of scores for this student
        if student_number not in student_scores:
            student_scores[student_number] = []
        student_scores[student_number].append(score)

# Calculate the average score for each student
for student_number, scores in student_scores.items():
    average_score = sum(scores) / len(scores)
    print(f"Student {student_number} has an average score of {average_score}")