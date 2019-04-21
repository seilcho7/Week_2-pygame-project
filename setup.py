import cx_Freeze

executables = [cx_Freeze.Executable("catch_monster.py")]

cx_Freeze.setup(
    name="Catch Monster",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["images/hero.png", "images/background.png", "images/goblin.png", "images/monster.png", "sounds/ff_background.mp3", "sounds/ff_catch.wav", "sounds/ff_lose.wav", "sounds/ff_victory.mp3"]}},
    executables = executables
)