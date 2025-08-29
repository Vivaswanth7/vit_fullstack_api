from flask import Flask, request, jsonify

app = Flask(__name__)

# -------- CONFIG (Edit with your details) --------
FULL_NAME = "vivaswanth_sadasivuni"   # lowercase only
DOB = "15022005"         # ddmmyyyy format
EMAIL = "vivaswanth9@gmail.com"
ROLL_NUMBER = "22BCE7760"
# -------------------------------------------------


def process_data(data):
    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0

    for item in data:
        # Handle numbers
        if item.isdigit():
            num = int(item)
            if num % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
            total_sum += num
        # Handle alphabets
        elif item.isalpha():
            alphabets.append(item.upper())
        # Handle special chars
        else:
            special_characters.append(item)

    # Build concat string: reverse + alternating caps
    concat_string = ""
    letters_only = "".join([c for c in "".join(data) if c.isalpha()])
    letters_only = letters_only[::-1]  # reverse
    for i, ch in enumerate(letters_only):
        concat_string += ch.upper() if i % 2 == 0 else ch.lower()

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME}_{DOB}",
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }


@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])
        response = process_data(data)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({
            "is_success": False,
            "message": str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True)