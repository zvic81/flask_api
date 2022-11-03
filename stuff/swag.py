from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app,
  template= {
    "swagger": "3.0",
    "openapi": "3.0.0",
    "info": {
        "title": "TODO",
        "version": "0.0.1",
    },
    "components": {
      "schemas": {
        "Todo": {
          "properties": {
            "name": {
              "type": "string"
            },
            "task": {
              "type": "string"
            }
          }
        }
      }
    }
  }
)

todos = {}

@app.route("/todos")
def get_todos():
  """
  Get all todos
  ---
  description: Get all todos.
  tags:
    - todos
  responses:
    200:
      description: List of all todos.
      content:
        application/json:
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Todo'

  """
  return jsonify(list(todos.values())), 200

@app.route("/todos", methods=['POST'])
def post_todo():
  """
  Create a new todo
  ---
  description: Create a new todo.
  tags:
    - todos
  requestBody:
    description: The todo to create.
    required: true
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/Todo'
  responses:
    200:
      description: Empty.
  """
  data = request.get_json()
  if not data:
    return jsonify({'message': 'No input data provided'}), 400
  else:
    todos[data['name']] = data
    return '', 200

@app.route("/todos/<string:name>")
def get_todo(name):
  """
  Get the todo with the name provided.
  ---
  description: >
    Get the todo with the name provided by
    getting it using the **name** parameter provided!
  tags:
    - todos
  parameters:
    - name: name
      in: path
      description: Name of the todo
      required: true
      schema:
        type: string
  responses:
    200:
      description: A todo.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Todo'
  """
  if name in todos:
    return jsonify(todos[name]), 200
  else:
    return jsonify({ 'error': 'Todo not found.' }), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
