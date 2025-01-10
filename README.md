**Chess game** 

Technologies used: 
* python 3.13 
* pygame 2.6.1

**Description:**

This is a chess game developed using Python and pygame for GUI. The game has two playing modes. You have an opportunity
to play against a human player or against AI. It was implemented using  (Соня допишет).

**Branches:**

Our team consists of 3 people that is why we decided to develop our project on 3 separate branches.
The list of branches:
* interface - Artem Pravotorov. He was responsible for the visual part of the game. 
* move-logic - Akinay Bekmambetova. She was in charge with pieces' logic of movements.
* game_process - Sofiia Grishko. She was responsible for the AI playing mode and check and mate.

**Files description:**

* **imgs directory** - contains all the images of the pieces. 
* **sounds directory** - contains sounds that are being played while making a move and capturing a piece.
* **pieces classes:**
    * piece.py - this file contains a parent class Piece from which the child classes of pieces are inherited. 
    * pawn.py, knight.py, bishop.py, rook.py, queen.py, king.py - are files with classes of the pieces.
* board.py - in this file we created a class of chessBoard and initialize starting positions of the pieces.
* button.py - here is implemented a class Button which is used while choosing a piece in pawn promotion.
* config.py - (Артём допишет)
* const.py - this file contains the dimension of the board and number of rows and columns.
* dragger.py - in this file we developed a class Dragger which is responsible to drag pieces.
* game.py - this file contains a class Game. the initialization of the game takes place in that class.
* main.py - the main file of the application that combines all the features from the other files, along with its own, to implement everything within the pygame interface.
* move.py - this file contains a class Move, which creates moves of the pieces.
* move_operations.py - here we developed a class CalculateMoves which calculates all valid moves for the pieces. 
* sound.py - this file contains a class Sound with a method to play sounds.
* square.py - this file contains a class Square where the squares on the board are created.

**Instructions:**
main.py - entry point, run this file to start a game. then in console you will choose a playing mode.
