# From http://mrjob.readthedocs.org/en/latest/guides/quickstart.html#writing-your-first-job

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRWordFrequencyCount(MRJob):
    def steps(self):
        return [
            # Step 1: Count bigrams
            MRStep(mapper=self.mapper_counts,
                   reducer=self.reducer_counts),
            # Step 2: Calculate probabilities
            MRStep(reducer=self.reducer_prob)
        ]

    # Step 1a: Split out all bigrams
    def mapper_counts(self, _, line):
        words = re.findall('([a-zA-Z]+[\'][a-zA-Z]+|[a-zA-Z]+)', line)
        num_words = len(words)
        if num_words>1:
            words[0] = words[0].upper()
            for i in range(num_words-1):
                words[i+1] = words[i+1].upper()
                yield (words[i], words[i+1]), 1

    # Step 1b: Reduce bigram counts
    def reducer_counts(self, words, count):
        word1, word2 = words
        yield word1, (sum(count),word2)

    
    # Step 2: Calculate probablities for each bigram
    #         and get top words that come after 'my'
    def reducer_prob(self, word1, bigrams_gen):
        yield word1, bigrams_gen

if __name__ == '__main__':
    MRWordFrequencyCount.run()
