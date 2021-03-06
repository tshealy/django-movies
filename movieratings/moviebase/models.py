from django.db import models
from django.contrib.auth.models import User


def create_users():
    for rater in Rater.objects.all():
        user = User.objects.create_user(
            "User{}".format(rater.id), "user{}@example.com".format(rater.id), "password")
        rater.user = user
        rater.save()

def change_passwords():
   for user in User.objects.all():
       password = "password"
       user.set_password(password)
       user.save()

class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    ONE = 1
    EIGHTTEEN = 18
    TWENTYFIVE = 25
    THIRTYFIVE = 35
    FORTYFIVE = 45
    FIFTY = 50
    FIFTYSIX = 56

    AGE_CHOICES = (
        (ONE, "Under 18"),
        (EIGHTTEEN, "18-24"),
        (TWENTYFIVE, "25-34"),
        (THIRTYFIVE, "35-44"),
        (FORTYFIVE, "45-49"),
        (FIFTY, "50-55"),
        (FIFTYSIX, "56+"),
    )

    age = models.IntegerField(choices=AGE_CHOICES)

    OTHER = 0
    ACADEMIC = 1
    ARTIST = 2
    ADMIN = 3
    COLLEGE = 4
    SERVICE = 5
    DOCTOR = 6
    EXEC = 7
    FARMER = 8
    HOMEMAKER = 9
    STUDENT = 10
    LAWYER = 11
    PROGRAMMER = 12
    RETIRED = 13
    SALES = 14
    SCEINTIST = 15
    SELF = 16
    TECH = 17
    TRADE = 18
    UNEMPLOYED = 19
    WRITER = 20

    JOB_CHOICE = (
       (OTHER, "other"),
       (ACADEMIC, "academic/educator"),
       (ARTIST, "artist"),
       (ADMIN, "clerical/admin"),
       (COLLEGE, "college/grad student"),
       (SERVICE, "customer service"),
       (DOCTOR, "doctor/health care"),
       (EXEC, "executive/managerial"),
       (FARMER, "farmer"),
       (HOMEMAKER, "homemaker"),
       (STUDENT, "K-12 student"),
       (LAWYER, "lawyer"),
       (PROGRAMMER, "programmer"),
       (RETIRED, "retired"),
       (SALES, "sales/marketing"),
       (SCEINTIST, "scientist"),
       (SELF, "self-employed"),
       (TECH, "technician/engineer"),
       (TRADE, "tradesman/craftsman"),
       (UNEMPLOYED, "unemployed"),
       (WRITER, "writer"),
   )
    job = models.IntegerField(choices=JOB_CHOICE, default=0)

    postal_code = models.CharField(max_length=10, null=True)

    user = models.OneToOneField(User, null=True)


    def __str__(self):
        return "User ID: {}, Job Type: {}, Age: {}"\
                .format(self.id, self.job, self.age)

class Movie(models.Model):
    title = models.CharField(max_length=255, null=True)
    #
    # ACTION = 'Action'
    # ADVENTURE = 'Adventure'
    # ANIMATION = 'Animation'
    # CHILDREN = '''Children's'''
    # COMEDY = 'Comedy'
    # CRIME = 'Crime'
    # DOCUMENTARY = 'Documentary'
    # DRAMA = 'Drama'
    # FANTASY = 'Fantasy'
    # FILM = 'Film-Noir'
    # HORROR = 'Horror'
    # MUSICAL = 'Musical'
    # MYSTERY = 'Mystery'
    # ROMANCE = 'Romance'
    # SCIFI = 'Sci-Fi'
    # THRILLER = 'Thriller'
    # WAR = 'War'
    # WESTERN = 'Western'
    #
    # GENRE_CHOICE = (
    #     (ACTION, 'Action'),
    #     (ADVENTURE, 'Adventure'),
    #     (ANIMATION, 'Animation'),
    #     (CHILDREN, '''Children's'''),
    #     (COMEDY, 'Comedy'),
    #     (CRIME, 'Crime'),
    #     (DOCUMENTARY, 'Documentary'),
    #     (DRAMA, 'Drama'),
    #     (FANTASY, 'Fantasy'),
    #     (FILM, 'Film-Noir'),
    #     (HORROR, 'Horror'),
    #     (MUSICAL, 'Musical'),
    #     (MYSTERY, 'Mystery'),
    #     (ROMANCE, 'Romance'),
    #     (SCIFI, 'Sci-Fi'),
    #     (THRILLER, 'Thriller'),
    #     (WAR, 'War'),
    #     (WESTERN, 'Western'),
    # )
    # genre = models.CharField(choices=GENRE_CHOICE, max_length=20, null=True)
    @property
    def average_rating(self):
        return round(self.rating_set.all().aggregate(models.Avg('rating'))['rating__avg'], 2)

    @property
    def ratings_count(self):
        return self.rating_set.all().aggregate(models.Count('rating'))['rating__count']

    def __str__(self):
        return "Title: {}".format(self.title)

class Rating(models.Model):
    rater = models.ForeignKey(Rater, null=True)
    movie = models.ForeignKey(Movie, null=True)

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    RATING_CHOICES = (
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)

    # timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return "Rater: {} rated movie {} a {}"\
                .format(self.rater.id, self.movie, self.rating)