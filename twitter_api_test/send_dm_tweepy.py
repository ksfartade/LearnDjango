import tweepy

# Replace these with your actual credentials
client_id = "LXI0WVN2MS16SERzN09JTGtJVE46MTpjaQ"
consumer_secret = "fw2LL4FdI73mRtEXsPmx3yqQzFXTRz2vUOwVxsw2VDqITPrWJz"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAOxq%2FwAAAAAAmQO8HmXaM2DAuelqq4NBCmaPURk%3D45sqyAmcb3iVx3ZjwpAlM5O01O75qcVypRNYX28q3ZPNu22GJn"
access_token = "1025827801952407552-sVtseYNhx3heKzT4yaHsHZPtkg0E5O"
access_token_secret = "sDzKbrnpgt5Y5O2GhF4nYLeH82Pf3ufTkelWsfNJCSTox"

def get_user_id(username):
    # Initialize Tweepy Client
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=client_id,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        # Get user information by username
        user = client.get_user(username=username)
        return user.data.id
    except tweepy.TweepyException as e:
        print(f"Error: {e}")
        return None

def send_direct_message(recipient_id, message_text):
    # Initialize Tweepy Client
    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=client_id,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    try:
        # Send a direct message
        response = client.create_direct_message(
            participant_id=recipient_id,
            text=message_text
        )
        print("Message sent successfully!")
        print(response)
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

def main():
    username = "FamePilotReview"  # Replace with the actual Twitter username of the recipient
    message_text = "Hello, this is a test message from Tweepy!"  # The message text you want to send

    # Get the recipient's user ID
    # recipient_id = get_user_id(username)
    recipient_id = '1025827801952407552'
    if recipient_id:
        print(f"Recipient ID: {recipient_id}")
        # Send the direct message
        send_direct_message(recipient_id, message_text)
    else:
        print("Failed to get recipient ID.")

if __name__ == "__main__":
    main()
