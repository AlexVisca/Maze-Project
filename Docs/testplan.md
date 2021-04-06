# Testplan

## Filepath
tests/  
* test_controllers.py  
* test_models.py  
* test_views.py  
* testmap.txt  

## Test plan

Tests|ID#|Description
-----|---|------------
`test_maze`|#01|Test `Maze()` model can return `cells` attribute.
`test_player`|#02|Test `Player()` model has backpack set to int:`0`.
`test_start_controller`|#03|Test `StartController()` controller loop functions.
`test_game_controller`|#04|Test `GameController()` controller functions.
`test_maze_controller`|#05|Test `MazeController()` controller functions.
`test_player_controller`|#06|Test `PlayerController()` controller has `move()` attribute.
`test_end_controller`|#07|Test `EndController()` functions.
`test_game_view`|#08|Test `GameView()` for game timer limit.
