from flask import Flask,request,Response
from flask_cors import CORS #, cross_origin
import base64,random,math


app=Flask(__name__)

# cors = CORS(app, resources={r"/YOURAPP/*": {"origins": "*"}})
cors = CORS(app, resources={r"/*": {"origins": "*"}})
auth_client_IP="127.0.0.1"  # needs to be tested 

@app.route("/",methods=['POST'])
def home():
    if request.method == 'POST' and request.access_route[-1] == auth_client_IP:
        try:
            img64 = request.get_json()['file'].split(',')[1]
            imgbytes = base64.b64decode(img64)
            filename='images/img_'+str(math.ceil(random.random()*10000))+'.jpg'
            with open(filename, 'wb') as f:
                f.write(imgbytes)
            # print(request.access_route[-1])
            # print(request.remote_addr)
            # print(img)
            print('File Received')
            return Response(status=200,response=img64)
        except Exception as error:
            print('File not Received')
            return Response(status=500,response=error)
    else:
        print("Unauthorized request")
        return Response(status=500,response="Unauthorized request")

if __name__ == '__main__':
    app.debug=True
    app.run(port=5000)  # ssl_context='adhoc'