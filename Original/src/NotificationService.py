class NotificationService:
    def notify_acceptance(self):
        print("NotificationService: Acceptance notification sent.")

    def notify_rejection(self):
        print("NotificationService: Rejection notification sent.")

    def notify_revision(self):
        print("NotificationService: Revision notification sent.")

    def send_notification(self, message):
        print(f"NotificationService: {message}")