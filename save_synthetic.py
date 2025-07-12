import pandas as pd
from datetime import datetime, timedelta
import random

categories = ["Complaints", "Bug Reports", "Feature Requests", "Compliments", "General Feedback"]
sources = ["App Store", "Email", "Google Play", "Web Form", "Twitter"]

feedback_data = {
    "feedback_text": [],
    "category": [],
    "source": [],
    "timestamp": []
}

sample_feedback = {
    "Complaints": [
        "The app crashes every time I try to upload a photo.",
        "Too many ads make the experience frustrating.",
        "Navigation is confusing and not user-friendly.",
        "The login process takes forever.",
        "It keeps asking me to verify my email again and again.",
        "The dark mode doesn't apply to all screens.",
        "Payment failed but the amount was deducted.",
        "Customer support is very slow to respond.",
        "The app freezes after the recent update.",
        "Settings options are very limited and unclear."
    ],
    "Bug Reports": [
        "When I tap the notification, the app opens a blank page.",
        "The calendar doesn't save any new events.",
        "Profile pictures are not loading.",
        "Voice input doesn't work on Android.",
        "I can’t delete old messages in the chat window.",
        "App randomly logs me out.",
        "Scrolling lags badly on the home feed.",
        "Push notifications don’t appear even when enabled.",
        "Fonts overlap on smaller screens.",
        "The share button crashes the app."
    ],
    "Feature Requests": [
        "Please add biometric login support.",
        "It would be great to have a dark theme toggle.",
        "Add a filter for unread messages.",
        "Can we get a desktop version too?",
        "Please include voice call functionality.",
        "Option to customize the dashboard would be helpful.",
        "An offline mode would be really useful.",
        "Need the ability to export data as CSV.",
        "A widget for the home screen would be nice.",
        "Add multi-language support, especially Hindi and Spanish."
    ],
    "Compliments": [
        "Amazing app! It’s super easy to use.",
        "I love the recent UI update.",
        "Great customer service!",
        "Very intuitive and fast — keep it up!",
        "Hands down the best productivity app I’ve tried.",
        "Love how clean and simple the design is.",
        "Thank you for listening to user feedback!",
        "Reliable and efficient, well done!",
        "Works seamlessly across my devices.",
        "Beautiful interface and flawless performance."
    ],
    "General Feedback": [
        "Good app, but could use some polish.",
        "Overall nice experience with a few hiccups.",
        "Hope you keep improving the update frequency.",
        "Useful features, though there’s room for growth.",
        "App works okay for basic needs.",
        "Can’t wait to see future enhancements.",
        "Decent app but has its flaws.",
        "Thanks for building something this useful.",
        "Sometimes it’s slow, but mostly fine.",
        "App does what it says, nothing more nothing less."
    ]
}

now = datetime.now()

for category in categories:
    for text in sample_feedback[category]:
        feedback_data["feedback_text"].append(text)
        feedback_data["category"].append(category)
        feedback_data["source"].append(random.choice(sources))
        random_days = random.randint(1, 60)
        feedback_data["timestamp"].append((now - timedelta(days=random_days)).strftime("%Y-%m-%d %H:%M:%S"))

# Create DataFrame
df = pd.DataFrame(feedback_data)
print(df.head())
df.to_csv("synthetic_feedback.csv", index=False)
print("✅ synthetic_feedback.csv created successfully!")
