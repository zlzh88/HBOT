from flask import Flask, request, jsonify, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def hellow() :
	return 'Server On!' 
                                
@app.route('/message', methods=['POST'])
def Message(): 
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']
    

    with open("data.json") as json_file:
        json_data = json.load(json_file)
        
    dataSend = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "코로나 관련 뉴스입니다!",
            "imageUrl": "https://proxy.goorm.io//service/5edf4a94cfcc8f3ea83d67ff_dp9Hbo59aZ4kbCsRvUr.run.goorm.io/9080//file/load/corona.jpg?path=d29ya3NwYWNlJTJGSEJPVF9mbGFzayUyRmNvcm9uYS5qcGc=&docker_id=dp9Hbo59aZ4kbCsRvUr&secure_session_id=cLVVoywMLcGY7mTcJfIqJcZMOYySkqMn"
          },
          "items": json_data["items"][:5]}}]}}
    
    return jsonify(dataSend)

@app.route('/status', methods=['POST'])
def push_statusImg() :    
	content = request.get_json()
	content = content['userRequest']
	content = content['utterance']
    
	imgSend = {
    "version": "2.0",
    "template": {
        "outputs": [
            {
                "simpleImage": {
                    "imageUrl": "https://proxy.goorm.io//service/5edf4a94cfcc8f3ea83d67ff_dp9Hbo59aZ4kbCsRvUr.run.goorm.io/9080//file/load/status.png?path=d29ya3NwYWNlJTJGSEJPVF9mbGFzayUyRmltYWdlcyUyRnN0YXR1cy5wbmc=&docker_id=dp9Hbo59aZ4kbCsRvUr&secure_session_id=QarWNYacpOHDZEtYoMO4YOefW1qJ_V0I",
                    "altText": "확진자 현황 입니다."
                }
            }
        ]
    }
}

	return jsonify(imgSend)

if __name__ == "__main__" :
    app.run(host='0.0.0.0', port=5000)
    