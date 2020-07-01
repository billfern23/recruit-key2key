import PyPDF2
import nltk.corpus
import re
punctuation = re.compile(r'[-.?!@,:;()|0-9]')

resume_pdf = open('Resume.pdf', 'rb')
cv_pdf = open('CV.pdf', 'rb')

# creating a pdf reader object
resume_reader = PyPDF2.PdfFileReader(resume_pdf)
cv_reader = PyPDF2.PdfFileReader(cv_pdf)

# printing number of pages in pdf file
print(resume_reader.numPages)

# creating a page object
page_obj_r = resume_reader.getPage(0)
page_obj_cv = cv_reader.getPage(0)

# extracting text from page
resume_tokens = nltk.word_tokenize(page_obj_r.extractText())
cv_tokens = nltk.word_tokenize(page_obj_cv.extractText())

resume_no_punctuation = []
for words in resume_tokens:
    word = punctuation.sub("",words)
    if(len(word)>0):
        resume_no_punctuation.append(word)
print(resume_no_punctuation)

cv_no_punctuation = []
for words in cv_tokens:
    word = punctuation.sub("",words)
    if(len(word)>0):
        cv_no_punctuation.append(word)
print(cv_no_punctuation)

# closing the pdf file object
resume_pdf.close()
cv_pdf.close()