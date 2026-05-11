class NotificationService:
    def notify_acceptance(self):
        global call_counter
        call_counter += 1
        print("NotificationService: Acceptance notification sent.")

    def notify_rejection(self):
        global call_counter
        call_counter += 1
        print("NotificationService: Rejection notification sent.")

    def notify_revision(self):
        global call_counter
        call_counter += 1
        print("NotificationService: Revision notification sent.")

    def send_notification(self, message):
        global call_counter
        call_counter += 1
        print(f"NotificationService: {message}")