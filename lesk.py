
import re
import sys
from nltk.corpus import wordnet

# Simplified Lesk algorithm
def lesk(word, sentence):

    senses = []
    overlaps = []

    #most frequent sense for word
    bestSense = wordnet.synsets(word)[0];
    #overlap count
    maxOverlap = 0;
    #set of words in sentence
    context = set(re.sub('\W+', ' ', sentence).lower().split());

    for sense in wordnet.synsets(word):
        #signature is: set of words in gloss+examples of the sense
        signature = set(re.sub('\W+', ' ', sense.definition()).lower().split())
        for example in sense.examples():
            signature.update(re.sub('\W+', ' ', example).lower().split());

        overlap = len(context.intersection(signature));

        if(overlap > maxOverlap):
            maxOverlap = overlap
            bestSense = sense

        #print current sense and overlap
        senses.append(sense.definition());
        overlaps.append(overlap);

    return bestSense, maxOverlap, senses, overlaps;

#Call simplified lesk
bestSense, maxOverlap, senses, overlaps = lesk(sys.argv[1], sys.argv[2]);

#Print to console
print('List of senses:')
for i in range(0, len(senses)):
    print("\nCurrent Sense: " + str(senses[i]) + "\nSense Overlap: " + str(overlaps[i]))
print("\n============================")
print("Best Sense: " + str(bestSense.definition()) + "\nBest Overlap: " + str(maxOverlap) + "\nExamples: ")
for count, example in enumerate(bestSense.examples(), start=1):
    print(str(count) + ". " + str(example));
print("============================\n")

#Print to file
myfile = open('output.txt', 'w+')
myfile.write('\nList of senses:\n')
for i in range(0, len(senses)):
    myfile.write("\nCurrent Sense: " + str(senses[i]) + "\nSense Overlap: " + str(overlaps[i]) + "\n")
myfile.write("\n============================\n")
myfile.write("Best Sense: " + str(bestSense.definition()) + "\nBest Overlap: " + str(maxOverlap) + "\nExamples:\n")
for count, example in enumerate(bestSense.examples(), start=1):
    myfile.write(str(count) + ". " + str(example)+"\n");
myfile.write("============================\n")

