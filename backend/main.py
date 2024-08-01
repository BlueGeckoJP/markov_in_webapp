import markov

from flask import Flask

app = Flask(__name__)


@app.route("/api")
def root():
    return mkv.gen_sentence()


if __name__ == "__main__":
    mkv = markov.Markov(
        rcfile="/etc/mecabrc",
        dicdir="/usr/lib/mecab/dic/mecab-ipadic-neologd/",
    )

    app.run(debug=True)
