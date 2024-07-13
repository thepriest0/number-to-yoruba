from flask import Flask, render_template, request

app = Flask(__name__)

def translate_to_yoruba(number):
    yoruba_numbers = {
        1: "ọ̀kan",
        2: "ẹ̀jì",
        3: "ẹ̀ta",
        4: "ẹ̀rin",
        5: "àrún",
        6: "ẹ̀fà",
        7: "ẹ̀je",
        8: "ẹ̀jọ",
        9: "ẹ̀sán",
        10: "ẹ̀wá",
        20: "ogún",
        30: "ọgbọ̀n",
        40: "ogójì",
        50: "àádọ́ta",
        60: "ọgọ́ta",
        70: "àádọ́rin",
        80: "ọgọ́rin",
        90: "àádọ́rùn",
        100: "ọgọ́rùn",
        200: "igba",
        300: "ọ́ọ̀dúnrún",
        400: "irinwó",
        500: "ẹ̀ẹ́dẹ́gbẹ́ta",
        1000: "ẹgbẹ́rún",
        2000: "ẹgbàá",
        3000: "ẹgbẹ́ẹ́ẹdógún",
        4000: "ẹgbàájì",
        5000: "ẹ̀ẹ́dẹ́gbàta"
    }

    if number in yoruba_numbers:
        return yoruba_numbers[number]

    if number < 100:
        tens = (number // 10) * 10
        units = number % 10
        return yoruba_numbers[tens] + " àti " + yoruba_numbers[units] if units else yoruba_numbers[tens]
    elif number < 1000:
        hundreds = number // 100
        remainder = number % 100
        return yoruba_numbers[hundreds * 100] + " àti " + translate_to_yoruba(remainder) if remainder else yoruba_numbers[hundreds * 100]
    elif number <= 5000:
        thousands = number // 1000
        remainder = number % 1000
        return yoruba_numbers[thousands * 1000] + " àti " + translate_to_yoruba(remainder) if remainder else yoruba_numbers[thousands * 1000]
    else:
        return "Number out of range"

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = None
    error = None
    number = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            print(f"Received number: {number}")  # Debug print
            if number < 1 or number > 5000:
                error = "Please enter a number between 1 and 5000."
            else:
                translation = translate_to_yoruba(number)
                print(f"Translation: {translation}")  # Debug print
        except ValueError:
            error = "Please enter a valid number."
            print(f"Error: {error}")  # Debug print
    return render_template('index.html', translation=translation, error=error if not translation else None, number=number)

if __name__ == '__main__':
    app.run(debug=True)
