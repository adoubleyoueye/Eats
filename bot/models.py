from django.db import models


class Order(models.Model):
    user_id = models.CharField(null=False, max_length=32)
    team_id = models.CharField(null=False, max_length=32)
    item = models.CharField(null=False, max_length=32)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    restaurant = models.TextField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}: {self.item}"


# TODO : Write methods
# def get_recent_orders(user_id, limit=5, timespan_days=14):
#     """
#     Fetch user's recent orders
    #     :param user: user
#     :param limit: limit
#     :param timespan_days: definition of recent in days
#     :return: recent orders
#     """
#     timespan_recent = datetime.now().astimezone() - timedelta(days=timespan_days)
#     orders_recent = (
#         Order.objects.filter(order_date=timespan_recent)
#         .filter(user=user_id)
#         .annotate(count=Count("interactions"))
#         .order_by("-count")[:limit]
#     )
#     return list(orders_recent)

# def get_remaining_budget(user):
#     total = monthly_budget - spent
#     return total

# def delete_order():
#     pass
