from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game
import json

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

@login_required(login_url='/users/login/')
def game_list(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name', '').strip()
        if room_name and not Game.objects.filter(room_name=room_name).exists():
            Game.objects.create(room_name=room_name, owner=request.user)
        return redirect('games:game_list')
    games = Game.objects.all().order_by('-id')
    return render(request, 'games/game_list.html', {'games': games})

@login_required(login_url='/users/login/')
def game_play(request, room_name):
    game = get_object_or_404(Game, room_name=room_name)
    board = game.get_board()

    if request.method == 'POST' and game.state == 'active' and game.owner == request.user:
        square_id = request.POST.get('square')
        if square_id is not None:
            idx = int(square_id)
            if board[idx] == '':
                token = '❌' if game.active_player == 1 else '⭕'
                board[idx] = token
                game.set_board(board)
                winner = check_winner(board)
                if winner:
                    game.state = 'won'
                    game.winner = str(game.owner)
                elif '' not in board:
                    game.state = 'tie'
                else:
                    game.active_player = 2 if game.active_player == 1 else 1
                game.save()
        return redirect('games:game_play', room_name=room_name)

    return render(request, 'games/game_play.html', {'game': game, 'board': board})

@login_required(login_url='/users/login/')
def game_delete(request, room_name):
    game = get_object_or_404(Game, room_name=room_name)
    if request.method == 'POST' and game.owner == request.user:
        game.delete()
    return redirect('games:game_list')