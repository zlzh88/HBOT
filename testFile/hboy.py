from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)

@app.router('/order', methods=(['POST']))

def order():

    req = request.get_jsoin()

    pizza_type = req['action']['detailParams']['피자종류']['value']
    address = req['action']['detailParams']['sys_text']['value']


    if len(pizza_type) <= 0 or len(address) <= 0:
        answer = ERROR_MESSAGE
    else:
        answer = pizza_type + "를 " + address + "(으)로 배달하겠습니다. 주문 감사합니다~"

        

    res = {
        "version": "2.0"
        "template": {
            "outputs": [
                {
                    "simpleText":{
                 	   "text": answer
                }
                }
            ]
        }
    }
