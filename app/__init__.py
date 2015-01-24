from flask import Flask, jsonify, make_response, abort, request

app = Flask(__name__)

motor_state = [
    {
        'id': 1,
        'name': u'velocity',
        'value': 0,
        'units': u'm/s',
        'flags': u'r'
    },
    {
        'id': 2,
        'name': u'distance',
        'value': 0,
        'units': u'm',
        'flags': u'r'
    },
    {
        'id': 3,
        'name': u'temperature',
        'value': 0,
        'units': u'C',
        'flags': u'r'
    },
    {
        'id': 4,
        'name': u'current',
        'value': 0,
        'units': 'amps',
        'flags': u'r'
    },
    {
        'id': 5,
        'name': u'velocityDesired',
        'value': 0,
        'units': u'm/s',
        'flags': u'rw'
    },
    {
        'id': 6,
        'name': u'distanceDesired',
        'value': 0,
        'units': u'm',
        'flags': u'rw'
    }
]


@app.route("/", methods = ['GET'])
def get_motor():
    return jsonify({'motor_state': motor_state})


@app.route('/<string:resource_name>', methods = ['GET'])
def get_resource(resource_name):
    resource = [res for res in motor_state if res['name'] == resource_name]
    if len(resource) == 0:
        abort(404)
    return jsonify({resource_name: resource[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error','Not found'}),404)

@app.route('/<string:resource_name>', methods = ['PUT'])
def put_vel_des():
    if not request.json or not 'value' in request.json:
        abort(400)   
    #in the future make a regex that looks for w
    if motor_state['name'==resource_name]['flags'] == 'rw':
        motor_state['name'==resource_name]['value'] = request.json['value']
    else:
        abort(400)
    return jsonify({resource_name: resource[0]}), 201

if __name__ == "__main__":
    app.run()
