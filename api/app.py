
'''
This module includes the create_app() function that
returns the Flask API Server with predefined endpoints
to interact with data processing module
'''
import os
from flask import Flask, jsonify, request
from data_processor import DataProcessor
from utils import Utils


def create_app():
    '''
    Initializes Flask app and necessary class objects
    Defines API endpoints and allowed request types
    :return: Flask API server
    '''
    app = Flask(__name__)
    data_processor = DataProcessor()
    util = Utils()

    @app.route("/latest", methods=['GET'])
    def get_latest_day():
        '''
        Endpoint that returns the output of get_latest_day()
        from DataProcessor class as JSON
        '''
        data = data_processor.get_latest_day()
        response = jsonify(data)
        return response

    @app.route("/latest/average", methods=['GET'])
    def get_latest_day_avg():
        '''
        Endpoint that returns the output of get_latest_day_average()
        from DataProcessor class as JSON
        '''
        data = data_processor.get_latest_day_average()
        response = jsonify(data)
        return response

    @app.route("/historical", methods=['GET'])
    def get_historical():
        '''
        Endpoint that validates the parameters `from` and `to`,
        returns the output of get_historical_data()
        from DataProcessor class as JSON
        '''
        dt_from = request.args.get('from')
        dt_to = request.args.get('to')
        validate = util.validate_date(dt_from, dt_to)

        if validate:
            data = data_processor.get_historical_data(dt_from, dt_to)
            response = jsonify(data)
        else:
            response = jsonify({"error": "please check time range field(s)!"})
            return response, 400
        return response

    @app.route("/historical/average", methods=['GET'])
    def get_historical_avg():
        '''
        Endpoint that validates the parameters `from` and `to`,
        returns the output of get_historical_data_average()
        from DataProcessor class as JSON
        '''
        dt_from = request.args.get('from')
        dt_to = request.args.get('to')
        validate = util.validate_date(dt_from, dt_to)

        if validate:
            data = data_processor.get_historical_data_average(dt_from, dt_to)
            response = jsonify(data)
        else:
            response = jsonify({"error": "please check time range field(s)!"})
            return response, 400
        return response

    @app.route("/average/highest", methods=['GET'])
    def get_avg_highest():
        '''
        Endpoint that returns the output of get_average_highest()
        from DataProcessor class as JSON
        '''
        data = data_processor.get_average_highest()
        response = jsonify(data)
        return response

    @app.route("/average/lowest", methods=['GET'])
    def get_avg_lowest():
        '''
        Endpoint that returns the output of get_average_lowest()
        from DataProcessor class as JSON
        '''
        data = data_processor.get_average_lowest()
        response = jsonify(data)
        return response

    return app


if __name__ == '__main__':
    app = create_app()

    if os.environ['DEBUG_MODE'] == '1':
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        app.run()
