from django.db import models


# Create your models here.
class Question(models.Model):
    '''
    Represents a poll question.

    Attributes:
        question_text (CharField): The text of the poll question.
        pub_date  (DateTimeField): The date and time the question was 
                                   published.

    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    

    def __str__(self):
        '''
        Returns the string representation of the Question object.
        '''
        return self.question_text


class Choice(models.Model):
    '''
    Represents an answer option for a specific question in a poll.

    Attributes:
        question (ForeignKey): The related Question object.
        choice_text (CharField): The text of the answer choice.
        votes (IntegerField): The number of votes this choice
                              has received.

    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        '''
        Returns the string representation of the Choice object.
        '''
        return self.choice_text
