from flask.cli import AppGroup
from app.seeds import (
    seed_developers,
    seed_game_statuses,
    seed_genres,
    seed_platforms,
    seed_publishers,
    seed_users
)


# Create a seed_cli
seed_cli = AppGroup('seed')

# Individual seed commands
@seed_cli.command("developers")
def seed_developers_command():
    seed_developers()

@seed_cli.command("game_statuses")
def seed_game_statuses_command():
    seed_game_statuses()

@seed_cli.command("genres")
def seed_genres_command():
    seed_genres()

@seed_cli.command("platforms")
def seed_platforms_command():
    seed_platforms()

@seed_cli.command("publishers")
def seed_publishers_command():
    seed_publishers()

@seed_cli.command("users")
def seed_users_command():
    seed_users()

# Full seed command
@seed_cli.command("all")
def seed_command():

    seed_developers()
    seed_game_statuses()
    seed_genres()
    seed_platforms()
    seed_publishers()
    seed_users()
    print('Seeds ran successfully!')


# Register the seed_cli with the app
def register_seed_commands(app):
    app.cli.add_command(seed_cli)