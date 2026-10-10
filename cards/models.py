from django.db import models

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=140)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["box"]

    def __str__(self):
        return self.question

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]
        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self
