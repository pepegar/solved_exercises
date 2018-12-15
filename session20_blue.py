from flask import Flask, jsonify

server = Flask("books")

list_of_books = []

@server.route("/books")
def get_books():
    return jsonify(list_of_books)

@server.route("/add/<title>", methods=["POST"])
def add_books(title):
    list_of_books.append(title)
    return jsonify("book added")

@server.route("/delete/<title>", methods=["DELETE"])
def whatever(title):
    if title in list_of_books:
        list_of_books.remove(title)
        return jsonify("book deleted")
    else:
        return jsonify("book not in the list")


server.run()
