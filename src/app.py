from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pickle
import pandas as pd
# import numpy

app = Flask(__name__)
api = Api(app)

model = pickle.load(open('../notebooks/model_v1.p', 'rb'))

# create endpoint
class Approval(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        res = model.predict(df)

        return res.tolist()

# assign endpoint
api.add_resource(Approval, '/approval')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)