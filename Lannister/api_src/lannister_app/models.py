from django.db import models
from django.utils.translation import gettext_lazy as _
from Lannister.api_src.user_auth.models import UserModel


class BonusRequest(models.Model):
    class RequestStatus(models.TextChoices):
        CREATED = "Cr", _("Created")
        APPROVED = "Ap", _("Approved")
        REJECTED = "Rj", _("Rejected")
        DONE = "Dn", _("Done")

    creator = models.ForeignKey(UserModel, related_name="creators", on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        UserModel, related_name="reviewers", null=True, blank=True, on_delete=models.SET_NULL
    )
    bonus_type = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=RequestStatus.choices,
        default=RequestStatus.CREATED,
    )
    date_created = models.DateTimeField(auto_now=True)
    date_approved = models.DateTimeField(blank=True, null=True)
    date_rejected = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    date_changed = models.DateTimeField(blank=True, null=True)
    date_payment = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "bonus_request"

    def __repr__(self) -> str:
        return f"Creator id: {self.creator} - Bonus type: {self.bonus_type}"

    def __str__(self) -> str:
        return f"Creator id: {self.creator} - Bonus type: {self.bonus_type}"

