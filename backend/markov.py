import MeCab
import random

from collections import deque


class Markov:
    def __init__(self, rcfile="", dicdir="", inputfile="input.txt", n_order=3):
        # read input file
        with open(inputfile) as f:
            lines = f.readlines()
            contents = [i.strip() for i in lines]

        # MeCab arguments settings
        tagger_args = "-Owakati"
        if rcfile != "":
            tagger_args += f" -r {rcfile} "
        if dicdir != "":
            tagger_args += f" -d {dicdir}"

        # separating words
        t = MeCab.Tagger(tagger_args)

        sentences = []
        for content in contents:
            sentence = t.parse(content).strip()
            sentences.append(sentence)
        sentences = [f"__BOS__ {sentence} __EOS__" for sentence in sentences]
        sentences = [sentence.split() for sentence in sentences]

        # data transform
        n_order -= 1
        self.markov_dict = {}
        self.bos_dict = {}
        for sentence in sentences:
            queue = deque(maxlen=n_order)
            for word in sentence:
                if len(queue) < n_order:
                    queue.append(word)
                    continue

                key = tuple(queue)
                if queue[0] == "__BOS__":
                    self.bos_dict.setdefault(key, []).append(word)
                self.markov_dict.setdefault(key, []).append(word)
                queue.append(word)
                # print(queue)

        print(f" - markov_dict len: {len(self.markov_dict)}")
        print(f" - bos_dict len: {len(self.bos_dict)}")

    def gen_sentence(self):
        word = random.choice(list(self.bos_dict))
        queue = deque(list(word), len(list(self.markov_dict.keys())[0]))
        sentence = "".join(word)

        while True:
            key = tuple(queue)
            next_word = random.choice(self.markov_dict[key])
            sentence += next_word
            queue.append(next_word)

            if next_word == "__EOS__":
                break

        return sentence.replace("__BOS__", "").replace("__EOS__", "")
