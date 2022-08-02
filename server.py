from flask import Flask, render_template, request

app = Flask('app')

ADJECTIVES =   {"a": "Awesome",
                "b": "Beautiful",
                "c": "Charismatic",
                "d": "Delightful",
                "e": "Extraordinary",
                "f": "Friendly",
                "g": "Glamorous", 
                "h": "Hilarious",
                "i": "Impassioned", 
                "j": "Jaunty",
                "k": "Kind",
                "l": "Lovely",
                "k": "Knowledgeable",
                "m": "Mysterious", 
                "n": "Nice",
                "o": "Original",
                "p": "Powerful",
                "q": "Quirky",
                "r": "Radical",
                "s": "Splendid",
                "t": "Thoughtful",
                "u": "Unique",
                "v": "Vivacious",
                "w": "Witty",
                "x": "Xenophilic",
                "y": "Yummy",
                "z": "Zesty"
                } 

@app.route("/")
def home():
    name = request.args.get("name")
    return render_template("index.html", name=name)

@app.route("/poem")
def poem():
    context = {}
    name = request.args.get("name")
    context["name"] = name
    context["words"] = get_poem_words(name)
    return render_template("poem.html", context=context)


def get_poem_words(name):
    words = []
    for letter in name:
        words.append(ADJECTIVES[letter.lower()])
    return words


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8001)