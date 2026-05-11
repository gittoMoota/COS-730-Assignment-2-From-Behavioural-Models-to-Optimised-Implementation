class NotificationService:
    def send_notification(self, outcome):
        global call_counter
        call_counter += 1
        return f"Notification sent: {outcome}"