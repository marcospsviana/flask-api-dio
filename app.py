from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)

    desenvolvedores = {'desenvolvedores':
        [
            {
                'nome': 'marcos paulo',
                'skills': ['python', 'django', 'flask'],

            },
            {
                'nome': 'tiago tardelli',
                'skills': ['python', 'django', 'flask', 'kotlin', 'C#', 'Java', 'html', 'css', 'react', 'vuejs'],

            },
        ]
    }

    @app.route('/desenvolvedores', methods=['POST', 'GET'])
    def index():
        return jsonify(desenvolvedores)

    @app.route('/desenvolvedores/<int:id>', methods=['POST', 'GET', 'PUT'])
    def desenvolvedor(id):
        if request.method == 'GET':
            dado_dev = desenvolvedores['desenvolvedores'][id]
        else:
            dado_dev = desenvolvedores['desenvolvedores'][id]
        return jsonify(dado_dev)


    return app


if __name__ == '__main__':
    create_app().run(debug=True)
