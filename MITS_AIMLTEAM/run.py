from similarity.hamming import hamming_distance
from similarity.jaccard import jaccard_coefficient
from similarity.overlap import overlap_coefficient

str1 = "Data Science"
str2 = "Data Analyst"  # Modified to be of the same length

try:
    print(f"The Hamming distance between '{str1}' and '{str2}' is {hamming_distance(str1, str2)}")
except ValueError as e:
    print(f"Error: {e}")

print(f"The Jaccard coefficient between '{str1}' and '{str2}' is {jaccard_coefficient(str1, str2)}")
print(f"The Overlap coefficient between '{str1}' and '{str2}' is {overlap_coefficient(str1, str2)}")
