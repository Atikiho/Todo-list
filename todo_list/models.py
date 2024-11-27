from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    state = models.BooleanField(default=False)
    tags = models.ManyToManyField(to="Tag", related_name="tasks")

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["state", "-created_at"]


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
