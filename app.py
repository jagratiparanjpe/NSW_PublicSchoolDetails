from flask import Flask, g, request, jsonify
from database import get_db

app = Flask(__name__)

@app.route('/details', methods=['GET'])
def get_details():
    db = get_db()
    details_cur = db.execute('select SCHOOL_NAME, STREET, SUBURB, POSTCODE, LEVEL_OF_SCHOOLING, SELECTIVE_SCHOOL, STUDENT_NUMBER from NSW_SCHOOL_DATA')
    details = details_cur.fetchall()
    return_values = []

    for detail in details:
        detail_dict = {}
        detail_dict['SCHOOL_NAME']      = detail['SCHOOL_NAME']
        detail_dict['STREET']  = detail['STREET']
        detail_dict['SUBURB']    = detail['SUBURB']
        detail_dict['POSTCODE']     = detail['POSTCODE']
        detail_dict['LEVEL_OF_SCHOOLING'] = detail['LEVEL_OF_SCHOOLING']
        detail_dict['SELECTIVE_SCHOOL'] = detail['SELECTIVE_SCHOOL']
        detail_dict['STUDENT_NUMBER'] = detail['STUDENT_NUMBER']

        return_values.append(detail_dict)

    return jsonify({'details' : return_values})

# get details for specific postcode
@app.route('/details/<string:POSTCODE>', methods=['GET'])
def get_detail(POSTCODE):
    db = get_db()
    details_cur = db.execute('select SCHOOL_NAME, STREET, SUBURB, LEVEL_OF_SCHOOLING, SELECTIVE_SCHOOL, STUDENT_NUMBER from NSW_SCHOOL_DATA where POSTCODE = ?', [POSTCODE])
    detail = details_cur.fetchall()

    return_values = []

    for detail in detail:
        detail_dict = {}
        detail_dict['SCHOOL_NAME'] = detail['SCHOOL_NAME']
        detail_dict['STREET'] = detail['STREET']
        detail_dict['SUBURB'] = detail['SUBURB']
        detail_dict['LEVEL_OF_SCHOOLING'] = detail['LEVEL_OF_SCHOOLING']
        detail_dict['SELECTIVE_SCHOOL'] = detail['SELECTIVE_SCHOOL']
        detail_dict['STUDENT_NUMBER'] = detail['STUDENT_NUMBER']

        return_values.append(detail_dict)

    return jsonify({'details' : return_values})


if __name__ == '__main__':
    app.run(debug=True)
