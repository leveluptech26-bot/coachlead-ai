# Follow-Up Messages Service

class FollowUpService:
    def __init__(self):
        self.follow_ups = {}

    def add_follow_up(self, user_id, message):
        if user_id not in self.follow_ups:
            self.follow_ups[user_id] = []
        self.follow_ups[user_id].append(message)

    def get_follow_ups(self, user_id):
        return self.follow_ups.get(user_id, [])

    def clear_follow_ups(self, user_id):
        if user_id in self.follow_ups:
            del self.follow_ups[user_id]

    def send_follow_up(self, user_id):
        messages = self.get_follow_ups(user_id)
        for message in messages:
            # Logic to send message goes here
            print(f'Sending message to user {user_id}: {message}')

        self.clear_follow_ups(user_id)