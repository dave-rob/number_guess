from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)
# print(random_number)
@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTd2ODRieGlsODViNDE1aGwyNGUxcTVrdm9sNnNqaWR5b2xpcWQ1ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/abHQ4aDqRqlyBTdAP0/giphy.gif />'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return '<h1 style="color: red">Too low, try again!</h1>' \
            '<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemJteDg0Ym5nc2I5YWpsbzViMXo4bWRjNG9zbnVxY2dxZnNpOHdvcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SDi3kPcN4mILsLKgQc/giphy.gif />'
    elif guess > random_number:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
            '<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWo2YXNubGgzNjVpdDI3ZXJpc3RlOGc2dWZxdXAyeHFlejN2NW11bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ky9vnG678kzD91TO3N/giphy.gif />'
    else:
        return '<h1 style="color: green">You found me!</h1>' \
            '<img src=https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3c5azF6cjJhcGd5bm50Z2hpZGZuYWlrb2NxeWlmMDdjNzE3cndsNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/naiba7cRbSjgrzJ9wa/giphy.gif />'
    
if __name__ == '__main__':
    app.run(debug=True)