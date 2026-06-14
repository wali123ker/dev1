from django.db import models
from django.contrib.auth.models import User
import json

class Game(models.Model):
    STATE_CHOICES = [
        ('active', 'Activa'),
        ('won', 'Ganada'),
        ('tie', 'Empate'),
    ]
    room_name = models.SlugField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_games')
    player2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='joined_games')
    board = models.TextField(default=json.dumps(['']*9))
    active_player = models.IntegerField(default=1)
    state = models.CharField(max_length=6, choices=STATE_CHOICES, default='active')
    winner = models.CharField(max_length=50, blank=True, null=True)

    def get_board(self):
        return json.loads(self.board)

    def set_board(self, board_list):
        self.board = json.dumps(board_list)

    def __str__(self):
        return f"Sala: {self.room_name} — {self.owner}"