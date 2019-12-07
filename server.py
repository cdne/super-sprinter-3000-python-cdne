from flask import Flask, render_template, request, redirect, url_for

from data_handler import *

app = Flask(__name__)

data = read_csv(DATA_FILE_PATH)

@app.route('/')
@app.route('/list')
def route_list():
    return render_template('list.html', title = "Super Sprinter 3000",
                                        data = data
                           )

@app.route('/story', methods=['GET', 'POST'])
def route_story():
    if request.method == 'POST':
        if len(data) < 1:
            id = 0
        else:
            id = len(data)
            story_logic()
            data.append(new_data)
            write_csv(DATA_FILE_PATH, data)
            return redirect('/')
    return render_template('story.html',
                               title='Add User Story | Super Sprinter 3000')


@app.route('/story/<int:id>', methods=['GET', 'POST'])
def route_update(id):
    try:
        current_data = data[id]
    except:
        return redirect(url_for('route_update', id=0))
    if request.method == 'POST':
        story_logic()
        del data[id]
        data.insert(id, new_data)
        write_csv(DATA_FILE_PATH, data)
        return redirect('/')
    return render_template('update.html',
                           title='Add User Story | Super Sprinter 3000',
                           current_data = current_data)

def story_logic():
    acceptance_criteria = request.form['acceptance_criteria']
    user_story = request.form['user_story']
    new_data = {'id': id + 1,
                'title': request.form['title'],
                'user_story': validate_newline(user_story),
                'acceptance_criteria': validate_newline(acceptance_criteria),
                'business_value': request.form['business_value'] + ' point',
                'estimation': request.form['estimation'] + 'h',
                'status': 'planning'
                }



def validate_newline(value):
    if '\n' in value or '<br>' in value:
        value = ''.join(value.split('<br>'))
        value = '<br>'.join(value.split('\n'))
    return value

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True
    )
