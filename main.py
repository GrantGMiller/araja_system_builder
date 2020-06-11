from flask import Flask, request, jsonify

app = Flask('System Builder')


@app.route('/', methods=['GET', 'POST'])
def Index():
    print('request.form=', request.form)
    if request.form:
        # the user submitted the form
        d = dict()
        d['procAlias'] = request.form.get('procAlias')
        d['uidAlias'] = request.form.get('uidAlias')
        return jsonify(d)
    else:
        # user needs to fill out the form

        resp = '''
        <html>
            <body>
                <form method="POST">
                    ProcessorDevice Alias: <input name='procAlias' type='text'/>
                    <br>
                    UIDevice Alias: <input name='uidAlias' type='text'/>
                    <br>
                    <input type='submit' value='Save'/>
                </form>
            </body>
        </html>
        '''
        return resp


if __name__ == '__main__':
    app.run(debug=True)
