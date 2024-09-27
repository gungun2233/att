from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

# List of motivational quotes
motivational_quotes = [
    "It does not matter how slowly you go as long as you do not stop.",
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Strive not to be a success, but rather to be of value.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "The way to get started is to quit talking and begin doing.",
    "Don't watch the clock; do what it does. Keep going.",
    "Everything you've ever wanted is on the other side of fear.",
    "Hard work beats talent when talent doesn't work hard.",
    "If you're going through hell, keep going.",
    "Your talent determines what you can do. Your motivation determines how much you're willing to do.",
    "The secret of getting ahead is getting started.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream big and dare to fail.",
    "You don't have to be great to start, but you have to start to be great.",
    "The only place where success comes before work is in the dictionary.",
    "Push yourself, because no one else is going to do it for you.",
    "The expert in anything was once a beginner.",
    "Success usually comes to those who are too busy to be looking for it.",
    "The best way to predict the future is to invent it.",
    "You are never too old to set another goal or to dream a new dream.",
    "Act as if what you do makes a difference. It does.",
    "Opportunities don't happen, you create them.",
    "You miss 100% of the shots you don’t take.",
    "Success is walking from failure to failure with no loss of enthusiasm.",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "The harder you work, the luckier you get.",
    "Your only limit is your mind.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream it. Believe it. Build it.",
    "Motivation is what gets you started. Habit is what keeps you going.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do what you can, with what you have, where you are.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Don’t wait. The time will never be just right.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up, start fresh, see the bright opportunity in each new day.",
    "Little by little, one travels far.",
    "It always seems impossible until it’s done.",
    "The best revenge is massive success.",
    "Don’t watch the clock; do what it does. Keep going.",
    "You are not your failures. You are not your mistakes. You are what you choose to become.",
    "Don’t be afraid to give up the good to go for the great.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "The way to get started is to quit talking and begin doing.",
    "In the end, we will remember not the words of our enemies, but the silence of our friends.",
    "A journey of a thousand miles begins with a single step.",
    "To be the best, you must be able to handle the worst.",
    "There are no limits to what you can accomplish, except the limits you place on your own thinking.",
    "You don’t have to be perfect to be amazing.",
    "Start where you are. Use what you have. Do what you can.",
    "Success is not in what you have, but who you are.",
    "You are never too old to set another goal or to dream a new dream.",
    "The best way to get started is to quit talking and begin doing.",
    "You are capable of more than you know.",
    "Don’t limit your challenges. Challenge your limits.",
    "Great things never come from comfort zones.",
    "Dream it. Believe it. Work for it.",
    "Your only limit is your mind.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things take time. Be patient.",
    "Dream bigger. Do bigger.",
    "Focus on your goal. Don’t look in any direction but ahead.",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
    "Do what you love, love what you do.",
    "Success doesn’t come from what you do occasionally. It comes from what you do consistently.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Hard work beats talent when talent doesn’t work hard.",
    "You are capable of achieving greatness.",
    "Chase your dreams, work hard, and never give up.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don’t let yesterday take up too much of today.",
    "The only limit to your impact is your imagination and commitment.",
    "Your dreams are valid.",
    "Don’t be afraid to start over. It’s a chance to build something better this time.",
    "You are stronger than you think.",
    "Every day is a new beginning. Take a deep breath, smile, and start again.",
    "Don’t wait for opportunity. Create it.",
    "Make each day your masterpiece.",
    "Stay positive, work hard, make it happen.",
    "Be not afraid of life. Believe that life is worth living, and your belief will help create the fact.",
    "Your attitude, not your aptitude, will determine your altitude.",
    "The only way to achieve the impossible is to believe it is possible."
]

# Get all images in the static folder
def get_images():
    image_folder = 'static'
    images = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png'))]
    print("Available images:", images)  # Debug print statement
    return images

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    quote = random.choice(motivational_quotes)
    images = get_images()  # Get the list of images
    if not images:
        return jsonify({'quote': "No images available.", 'image_url': ""})  # Handle case with no images
    image_url = f"/static/{random.choice(images)}"  # Select a random image
    print("Selected image:", image_url)  # Debug print statement
    return jsonify({'quote': quote, 'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
