from flask import Flask, request, render_template

app = Flask(__name__)

import os
import vertexai
from vertexai import language_models

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable.

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/webapp1/mlproj1-403203-c24f2a45ebd5.json'

# Initialize Vertex AI.

vertexai.init(project="mlproj1-403203", location="us-central1")

# Load the CodeChatModel model from Vertex AI.

chat_model = language_models.CodeChatModel.from_pretrained("codechat-bison")

# Define a function to correct SQL queries.

def correct_sql_query(sql_query):
  """Corrects a SQL query using the Vertex AI CodeChatModel model.

  Args:
    sql_query: A string containing the SQL query to be corrected.

  Returns:
    A string containing the corrected SQL query.
  """

  chat = chat_model.start_chat()
  response = chat.send_message(sql_query)
  corrected_sql_query = response.text
  return corrected_sql_query

# Define a route to handle POST requests.

@app.route("/", methods=["POST"])
def handle_post_request():
  """Handles POST requests that contain SQL queries to be corrected.

  Returns:
    A plain text response containing the corrected SQL query.
  """

  sql_query = request.get_data().decode("utf-8")
  corrected_sql_query = correct_sql_query(sql_query)

  response = corrected_sql_query

  return response

# Define a route to handle GET requests.

@app.route("/")
def handle_get_request():
  """Handles GET requests that display the main page of the application.

  Returns:
    An HTML response containing the main page of the application.
  """

  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)
