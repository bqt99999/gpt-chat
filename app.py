from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set up the OpenAI API with API key
openai.api_key = "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"
# The "creativity" of the generated response (0-1)
creativity=1
# Maximum words of response
maxWord=500
# Model of GPT
modelGPT='gpt-3.5-turbo'

# Input questions
#prompt = input("Input your question: ")

@app.route("/")
def index():
    return render_template("index.html", response="")
@app.route('/submit-message', methods=['POST'])
def submit_message():
    input_message = request.form.get('inputMessage')
    # Do something with the input message, e.g. call OpenAI API and get response
    # Return the response to the client as a JSON object
    response = {"response": "Hello, you said: " + input_message}
    return response

def askGPT(prompt):
    response_ai = openai.ChatCompletion.create(
        model=modelGPT,
        messages=[
            {"role": "user", "content": prompt}],
        max_tokens=maxWord,
        temperature=creativity,
    )
    return response_ai['choices'][0]['message']['content']

@app.route("/api/message")
def get_response():
    prompt = request.args.get("message")
    response = askGPT(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
