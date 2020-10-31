from django.db import models


class Content(models.Model):

    title = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        default="",
        help_text="Your title goes here",
    )

    content = models.TextField(
        blank=False,
        null=False,
        default="",
        help_text="Place here the content for your landing page",
    )

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title


class Collaborator(models.Model):

    avatar = models.ImageField(
        upload_to="avatars",
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        default="",
        help_text="Lirst name of collaborator",
    )
    last_name = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default="",
        help_text="Last name of collaborator",
    )
    email = models.EmailField(
        max_length=254,
        blank=True,
        null=True,
        default="",
    )
    nationality = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default="",
        help_text="Collaborator nationality",
    )
    profile = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        default="",
        help_text="Collaborator profile",
    )

    def __str__(self):
        if self.last_name is not None:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return "%s" % (self.first_name)


class SocialNetwork(models.Model):

    collaborator = models.ForeignKey(
        Collaborator, related_name="social_network", on_delete=models.CASCADE
    )
    network = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        default="",
        help_text="Social network name",
    )
    link = models.URLField(max_length=250, help_text="Social network link")

    def __str__(self):
        return "%s" % (self.network)
