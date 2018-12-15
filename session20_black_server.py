from flask import Flask, jsonify

server = Flask("todos")

tasks = {}

@server.route("/tasks")
def list_all_tasks():
    return jsonify(tasks)

@server.route("/view/<status>")
def view_tasks(status):
    result = []
    for task in tasks:
        if tasks[task] == status:
            result.append(task)
            
    return jsonify(result)
            

@server.route("/add_task/<task>", methods=["PUT"])
def add_task(task):
    tasks[task] = "open"
    
    return jsonify("[added]: {}".format(task))

@server.route("/complete_task/<task>", methods=["POST"])
def complete_task(task):
    if task in tasks:        
        tasks[task] = "complete"
    else:
        return jsonify("task doesn't exist")
    
    return jsonify("[completed]: {}".format(task))


server.run()
