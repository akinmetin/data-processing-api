
'''
This module includes the create_app() function that
returns the Flask API Server with predefined endpoints
to interact with data processing module
'''
import os


def create_app():
    '''
    Initializes Flask app and necessary class objects
    Defines API endpoints and allowed request types
    :return: Flask API server
    '''
    from flask import Flask, jsonify, request
    from api.data_processor import DataProcessor
    import api.utils as _utils

    app = Flask(__name__)
    data_processor = DataProcessor()

    @app.route("/latest", methods=['GET'])
    def get_latest_day():
        '''
        Returns the output of get_latest_day() from DataProcessor
        '''
        data = data_processor.get_latest_day()
        return jsonify(data)

    @app.route("/latest/average", methods=['GET'])
    def get_latest_day_avg():
        '''
        Returns the output of get_latest_day_average() from DataProcessor
        '''
        data = data_processor.get_latest_day_average()
        return jsonify(data)

    @app.route("/historical", methods=['GET'])
    def get_historical():
        '''
        Returns the output of get_historical_data() from DataProcessor
        '''
        dt_from = request.args.get('from')
        dt_to = request.args.get('to')
        validate = _utils.validate_date(dt_from, dt_to)

        if validate:
            data = data_processor.get_historical_data(dt_from, dt_to)
            return jsonify(data)
        response = jsonify({"error": "please check time range field(s)!"})
        return response, 400

    @app.route("/historical/average", methods=['GET'])
    def get_historical_avg():
        '''
        Returns the output of get_historical_data_average() from DataProcessor
        '''
        dt_from = request.args.get('from')
        dt_to = request.args.get('to')
        validate = _utils.validate_date(dt_from, dt_to)

        if validate:
            data = data_processor.get_historical_data_average(dt_from, dt_to)
            return jsonify(data)
        response = jsonify({"error": "please check time range field(s)!"})
        return response, 400

    @app.route("/average/highest", methods=['GET'])
    def get_avg_highest():
        '''
        Returns the output of get_average_highest() from DataProcessor
        '''
        data = data_processor.get_average_highest()
        return jsonify(data)

    @app.route("/average/lowest", methods=['GET'])
    def get_avg_lowest():
        '''
        Returns the output of get_average_lowest() from DataProcessor
        '''
        data = data_processor.get_average_lowest()
        return jsonify(data)

    return app


if __name__ == '__main__':
    app = create_app()

    if os.environ['DEBUG_MODE'] == '1':
        app.run(debug=True, host='0.0.0.0', port=5000)
    app.run()
