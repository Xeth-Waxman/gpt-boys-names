import nltk

# Set the NLTK data path to the directory where the data is installed
nltk.data.path.append('/workspace/gpt-boys-names/nltk_data')

# Download the names resource
nltk.download('names', download_dir='/workspace/gpt-boys-names/nltk_data')
nltk.download('cmudict', download_dir='/workspace/gpt-boys-names/nltk_data')

# Get a list of male names from the NLTK corpus
male_names = nltk.corpus.names.words('male.txt')

# Initialize a list to store tuples of names and their phonetical pronunciations
name_phonetics = []

# Use the CMU Pronouncing Dictionary from the NLTK library to get the phonetic pronunciations
cmu_dict = nltk.corpus.cmudict.dict()

# Iterate over each name and get its phonetic pronunciation
for name in male_names:
    phonetics = cmu_dict.get(name.lower(), [])
    if phonetics:
        name_phonetics.append((name, ' '.join(phonetics[0])))

# Select the first 100 names and their phonetic pronunciations
selected_names = name_phonetics[:100]

# Write the names and their phonetic pronunciations to a text file
with open('boys_names.txt', 'w', encoding='utf-8') as f:
    for name, phonetic in selected_names:
        f.write(f"{name}\t{phonetic}\n")
