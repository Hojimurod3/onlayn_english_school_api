from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=255)
    location = models.URLField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.IntegerField()
    ielts = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Kurses(models.Model):
    title = models.CharField(max_length=255)
    level = models.ForeignKey("Level", on_delete=models.CASCADE, related_name='Kurses')
    max_students = models.IntegerField()

    def __str__(self):
        return self.title

class Level(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
class Students(models.Model):
    title = models.CharField(max_length=255)
    phone = models.IntegerField()
    time = models.ForeignKey("Lessons", on_delete=models.CASCADE, related_name="students")
    kurs = models.ForeignKey(Kurses, on_delete=models.CASCADE, related_name="students")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='students')
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='students')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.title


class Lessons(models.Model):
    id = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE, related_name='lessons')
    start_time = models.TimeField()
    end_time = models.TimeField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='lessons')


class Price(models.Model):
    kurs = models.ForeignKey(Kurses, on_delete=models.CASCADE, related_name='price')
    price = models.DecimalField(max_digits=10, decimal_places=2)



