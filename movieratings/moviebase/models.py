from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Avg, Count
from django.contrib.auth.models import User


def validating_rating(value):
    if value not in [1, 2, 3, 4, 5]:
        raise ValidationError

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

def delete_users():
    for users in User.objects.all():
        users.delete()


class Rater(models.Model):

    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)

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

    @property
    def num_reviews(self):
        return self.rating_set.count()

    @property
    def movies_seen(self):
        ratings = self.rating_set.all()
        return {rating.movie: rating.rating for rating in ratings}

    @property
    def average_rating(self):
        ratings = self.rating_set.all()
        total = 0
        if ratings:
            for rating in ratings:
                total += rating.rating
            return round(total/len(ratings), 2)
        else:
            return "No ratings"

    def __str__(self):
        return "User ID: {}, Job Type: {}, Age: {}"\
                .format(self.id, self.job, self.age)


class Movie(models.Model):
    title = models.CharField(max_length=255, null=True)

    genre = models.ManyToManyField("Genre")

    @property
    def average_rating(self):
        #returns a dictionary of {rating__avg: value}
        average_rating = self.rating_set.all().aggregate(Avg('rating'))
        if average_rating:
            #just want the value
            return average_rating['rating__avg']
        else:
            return "No ratings"

    @property
    def ratings_count(self):
        count_rating = self.rating_set.all().aggregate(Count('rating'))
        if count_rating:
            return (count_rating['rating__count'])
        else:
            return "No ratings"

    def __str__(self):
        return self.title

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
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, validators=[validating_rating])

    posted_at = models.DateTimeField(null=True)

    text_rating = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "Rater: {} rated movie {} a {}"\
                .format(self.rater.id, self.movie, self.rating)
    class Meta:
        unique_together = ('rater', 'movie')


class Genre(models.Model):

    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    ANIMATION = 'Animation'
    CHILDREN = '''Children's'''
    COMEDY = 'Comedy'
    CRIME = 'Crime'
    DOCUMENTARY = 'Documentary'
    DRAMA = 'Drama'
    FANTASY = 'Fantasy'
    FILM = 'Film-Noir'
    HORROR = 'Horror'
    MUSICAL = 'Musical'
    MYSTERY = 'Mystery'
    ROMANCE = 'Romance'
    SCIFI = 'Sci-Fi'
    THRILLER = 'Thriller'
    WAR = 'War'
    WESTERN = 'Western'

    GENRE_CHOICE = (
        (ACTION, 'Action'),
        (ADVENTURE, 'Adventure'),
        (ANIMATION, 'Animation'),
        (CHILDREN, '''Children's'''),
        (COMEDY, 'Comedy'),
        (CRIME, 'Crime'),
        (DOCUMENTARY, 'Documentary'),
        (DRAMA, 'Drama'),
        (FANTASY, 'Fantasy'),
        (FILM, 'Film-Noir'),
        (HORROR, 'Horror'),
        (MUSICAL, 'Musical'),
        (MYSTERY, 'Mystery'),
        (ROMANCE, 'Romance'),
        (SCIFI, 'Sci-Fi'),
        (THRILLER, 'Thriller'),
        (WAR, 'War'),
        (WESTERN, 'Western'),
    )
    genre = models.CharField(choices=GENRE_CHOICE, max_length=255, null=True)

    def __str__(self):
        return self.genre
