import secrets

from django.db import models


class TimeStampedModel(models.Model):
    """Models with timestamps for time audit"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """Models that should not be physically deleted"""
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def soft_delete(self):
        if not self.is_deleted:
            self.is_deleted = True
            self.save()

    def restore_soft_deletion(self):
        if self.is_deleted:
            self.is_deleted = False
            self.save()


class PublicIDModel(models.Model):
    """Models exposed through the public API/URL"""
    BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    PREFIX = "xxx"
    public_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )

    @classmethod
    def generate_public_id(cls):
        if len(cls.PREFIX) not in (1,2,3):
            raise ValueError("PREFIX must be exactly 1, 2 or 3 characters")
        random_part = "".join(
            secrets.choice(cls.BASE62_ALPHABET) for _ in range(12)
        )
        return f"{cls.PREFIX.lower()}_{random_part}"

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = self.generate_public_id()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class BaseModel(PublicIDModel, SoftDeleteModel, TimeStampedModel):
    class Meta:
        abstract = True
