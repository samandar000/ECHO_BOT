from flask import Flask,request,jsonify
import os
import telegram
TOKEN = os.environ.get('TOKEN')
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)
token = os.environ()
@app.route('/')
def home():
    html = '''
    <h1> This is a home page </h1>
    <p> This is a paragraph </p>
    '''
    print(TOKEN)
    return html


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json(force=True)
    print(data)
    chat_id = 5325797385
    bot.send_message(chat_id=chat_id,text="Hello,this is a message from the bot")
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True) 