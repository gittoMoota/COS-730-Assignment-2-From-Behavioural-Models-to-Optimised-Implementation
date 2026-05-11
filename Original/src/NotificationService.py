from metrics import call_counter
import metrics
class NotificationService:
    def notify_acceptance(self):
        metrics.call_counter += 1
        print("NotificationService: Acceptance notification sent.")

    def notify_rejection(self):
        metrics.call_counter += 1
        print("NotificationService: Rejection notification sent.")

    def notify_revision(self):
        metrics.call_counter += 1
        print("NotificationService: Revision notification sent.")

    def send_notification(self, message):
        metrics.call_counter += 1
        print(f"NotificationService: {message}")