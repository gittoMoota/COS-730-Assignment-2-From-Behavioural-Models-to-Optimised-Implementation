from metrics import call_counter
import metrics
class NotificationService:
    def send_notification(self, outcome):
        metrics.call_counter += 1
        return f"Notification sent: {outcome}"