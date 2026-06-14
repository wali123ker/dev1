import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Game

def check_winner(board):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in wins:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'game_{self.room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get('action')

        if action == 'move':
            idx = int(data.get('square'))
            user = self.scope['user']
            game = await self.get_game()
            board = game.get_board()

            if game.state != 'active' or board[idx] != '':
                return

            owner = await self.get_owner(game)
            if user != owner:
                return

            token = '❌' if game.active_player == 1 else '⭕'
            board[idx] = token
            game.set_board(board)

            winner = check_winner(board)
            if winner:
                game.state = 'won'
                game.winner = str(owner)
            elif '' not in board:
                game.state = 'tie'
            else:
                game.active_player = 2 if game.active_player == 1 else 1

            await self.save_game(game)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'game.update',
                    'board': board,
                    'active_player': game.active_player,
                    'state': game.state,
                    'winner': game.winner or '',
                }
            )

        elif action == 'delete':
            user = self.scope['user']
            game = await self.get_game()
            owner = await self.get_owner(game)
            if user == owner and game.state != 'active':
                await self.delete_game(game)
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {'type': 'game.deleted'}
                )

    async def game_update(self, event):
        await self.send(text_data=json.dumps({
            'type': 'update',
            'board': event['board'],
            'active_player': event['active_player'],
            'state': event['state'],
            'winner': event['winner'],
        }))

    async def game_deleted(self, event):
        await self.send(text_data=json.dumps({'type': 'deleted'}))

    @database_sync_to_async
    def get_game(self):
        return Game.objects.get(room_name=self.room_name)

    @database_sync_to_async
    def get_owner(self, game):
        return game.owner

    @database_sync_to_async
    def save_game(self, game):
        game.save()

    @database_sync_to_async
    def delete_game(self, game):
        game.delete()