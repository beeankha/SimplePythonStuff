from django.db import models

# Create your models here.
# A model tells Django how to work with the data that will be stored in the app.

# Whenever the models are modified, we need to call makemigrations on learning_logs,
# and then tell Django to migrate the project.


class Topic(models.Model):
    # We've created a class called Topic, which inherits from Model -- a parent
    # class included in Django that defines a model's basic functionality.
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # ^^ We add two attributes to the Topic class: text and date_added.
    # The "auto_now_add=True" argument tells Django to automatically set this
    # attribute to the current date and time whenever the user creates a new topic.

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# Model Field Reference
# https://docs.djangoproject.com/en/2.2/ref/models/fields/

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
    # The Meta class holds extra information for managing a model!
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
        # ^^ Only shows the first 50 characters of text!
