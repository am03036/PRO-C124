from  flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [
    {
        'id':1,
        'name':'Amish',
        'contact':'9911008877',
        'done': False
    },
    {
        'id':2,
        'name':'Raj',
        'contact':'5566778899',
        'done': False
    }
]
@app.route('/get-contacts')
def get_tasks():
    return jsonify({
        'data':contacts
    })

@app.route('/add-contacts',methods=['POST'])
def post_tasks():
    if not request.json:
        return jsonify(
            {
                'status':'error',
                'message':'please provide the data'
            },400)
    contact = {
        'id':contacts[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'done': False
    }
    contacts.append(contact)
    return jsonify(
            {
                'status':'success',
                'message':'contact added successfully'
            },200)

if (__name__ == '__main__'):
    app.run(debug=True)