import nltk.corpus
import numpy as np
import docx2txt
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import utility.keyword as kw

punctuation = re.compile(r'[-.?!@,:;()|0-9]')
# creating files
resume = docx2txt.process("Resume2.docx")
cv = docx2txt.process("CV.docx")
job_description = docx2txt.process("Job_Description.docx")

# FIRST: get the cosine similarity between Resume and Job Description

# Create a list of text
text = [resume, job_description]

# Create a count vectorizer object and convert the text documents to a matrix of token counts
count_vec = CountVectorizer()
count_matrix = count_vec.fit_transform(text)

# Get and print the cosine similarity scores
print("Similarity Matrix Between Resume and Job Description:")
print(cosine_similarity(count_matrix))

# Get the match percentage
match_percentage = cosine_similarity(count_matrix)[0][1] * 100 # find the similarity of 2 elements in the matrix
match_percentage = round(match_percentage, 2) # round to 2 decimal
print("The resume matches about "+ str(match_percentage) + "% of the job description.\n\n")

# SECOND: compare Cover Letter to the keyword dictionary

# Create an object of keywords
key = kw.Keyword(["flexible", "creative", "great communication", "organized", "quick learner"])

keyword_dict = { 'flexible': ['adaptable', 'change'],
                'creative': ['imaginative', 'imagination', 'innovative'],
                'great communication': ['language', 'writing', 'oral', 'verbal', 'presentation'],
                'organized': ['calendar', 'organizer', 'notes', 'weekly', 'daily', 'every day', 'every week'],
                'quick learner': ['edx', 'coursera', 'udemy', 'lecture']
}

keywords_string = " "
keywords_string = keywords_string.join(key.get_keywords())
print(key.get_keywords()) # "flexible, creative, analytical, organized, quick learner"

cv_tokens = nltk.word_tokenize(cv)
# TODO: find keywords (synonyms) among tokens

# THIRD: calculate the candidate score based on the above criteria

# create an empty array for candidate score
candidate_score = np.zeros(key.get_keywords_number(), int)

if match_percentage < 50:
    pass
elif match_percentage < 60:
    candidate_score[0] += 5
elif match_percentage < 70:
    candidate_score[0] += 10
elif match_percentage < 80:
    candidate_score[0] += 20
elif match_percentage < 90:
    candidate_score[0] += 35
else:
    candidate_score[0] += 50

# TODO: add more evaluation criteria for the candidate
# the maximum value for each of the score values is considered to be 50
# for testing purposes, other values are hard-coded for now:
candidate_score[0] = 1
candidate_score[1] = 30
candidate_score[2] = 20
candidate_score[3] = 15
candidate_score[4] = 2

plt.bar([1,2,3,4,5], candidate_score, label = "Candidate Name")
plt.legend()
plt.xlabel('Category')
plt.ylabel('Score')
plt.title('Candidate Score')

plt.show()