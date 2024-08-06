from django.db import models
from django.db.models import Q, Index, Max
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class FYStudent(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN , "Freshman"),
        (SOPHOMORE , "Sophomore"),
        (JUNIOR , "Junior"),
        (SENIOR , "Senior"),
        (GRADUATE , "Graduate"),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    class Role(models.TextChoices):
        MANAGER = 'MGR', 'Manager'
        DEVELOPER = 'DEV', 'Developer'
        INTERN = 'INT', 'Intern'

    role = models.CharField(
        max_length=3,
        choices=Role.choices,
        default=Role.INTERN,
    )

    class Status(models.IntegerChoices):
        TODO = 1, 'To Do'
        IN_PROGRESS = 2, 'In Progress'
        DONE = 3, 'Done'

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.TODO,
    )

    name = models.CharField(max_length=100)

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
    
    def __str__(self) -> str:
        return self.name + " " + self.year_in_school

class Elective(models.Model):
    subject = models.CharField(max_length=50, unique=True)
    marks   = models.IntegerField(default=0)


class Department(models.Model):
    class Names(models.TextChoices):
        ENTC    = 'ENTC', 'Electronics and telecommunications'
        CIVIL   = 'CIVIL', 'Cement and Intelligent'
        CS      = 'CS', "Computer science"
        IT      = 'IT', "Information Technology"

    name = models.CharField(max_length=10, choices=Names, default=Names.CIVIL)

class SY(models.Model):
    class DivisionChoice(models.TextChoices):
        A = 'A', 'Devision A'
        B = 'B', "Devision B"
        C = 'C', 'Devision C'
        D = 'D', "Devision D"

    name        = models.CharField(max_length=100)
    roll_no     = models.IntegerField(primary_key=True)
    division    = models.CharField(max_length=1, choices=DivisionChoice.choices)
    marks       = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True)
    # slug        = models.SlugField(unique=True)
    elective    = models.OneToOneField(Elective, related_name='student', on_delete=models.SET_NULL, null=True)
    department  = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ['division', '-name']
        verbose_name = 'SY Student Data'
        verbose_name_plural = "SY Student Records"
        indexes = [
            Index(
                name='division_A_index',
                fields=['name'],
                condition=Q(division='A')
            )
        ]
    
    def save(self, *args, **kwargs):
        if not self.roll_no:
            current_max = SY.objects.filter(division=self.division).aggregate(Max('roll_no', default=0))
            self.roll_no = current_max['roll_no__max'] + 1
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.division + " " + self.name
