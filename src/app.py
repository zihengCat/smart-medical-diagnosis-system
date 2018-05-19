import flask as f

# Create App
app = f.Flask(__name__)


def read_data():
    f = open('records/input_data.txt', 'rt')
    data_list = list()
    for l in f.readlines():
        data_list.append(l.replace('\n', ''))
    return data_list

@app.route('/get/result', methods=['POST'])
def do_get_result():
    pass


## Index Page
@app.route('/', methods=['GET'])
def do_index():
    data = read_data()
    return f.render_template('index.html', data_list = data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333', debug=True)

