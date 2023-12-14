#include <vector>
#include <string>
#include <sstream>

std::vector<std::vector<char>> initializeGameBoard(int boardSize) {
    std::vector<std::vector<char>> gameBoard(boardSize, std::vector<char>(boardSize, '.'));
    return gameBoard;
}

void flipGamePieces(std::vector<std::vector<char>>& gameBoard, char currentPlayer, int positionX, int positionY) {
    std::vector<std::pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {-1, -1}, {1, -1}, {-1, 1}};
    for (auto [deltaX, deltaY] : directions) {
        int nextX = positionX + deltaX, nextY = positionY + deltaY;
        while (0 <= nextX && nextX < gameBoard.size() && 0 <= nextY && nextY < gameBoard[0].size() && gameBoard[nextX][nextY] != '.') {
            if (gameBoard[nextX][nextY] == currentPlayer) {
                while (std::make_pair(nextX, nextY) != std::make_pair(positionX, positionY)) {
                    gameBoard[nextX][nextY] = currentPlayer;
                    nextX -= deltaX; nextY -= deltaY;
                }
                break;
            }
            nextX += deltaX; nextY += deltaY;
        }
    }
}

std::vector<std::vector<char>> playGameMoves(int boardSize, std::vector<std::string> moves) {
    auto gameBoard = initializeGameBoard(boardSize);
    for (auto move : moves) {
        std::istringstream iss(move);
        std::string currentPlayer; int positionX, positionY;
        iss >> currentPlayer >> positionX >> positionY;
        gameBoard[positionX][positionY] = currentPlayer[0];
        flipGamePieces(gameBoard, currentPlayer[0], positionX, positionY);
    }
    return gameBoard;
}

std::pair<int, int> countGamePieces(std::vector<std::vector<char>> gameBoard) {
    int blackPieceCount = 0, whitePieceCount = 0;
    for (auto row : gameBoard) {
        for (auto cell : row) {
            if (cell == 'B') ++blackPieceCount;
            if (cell == 'W') ++whitePieceCount;
        }
    }
    return {blackPieceCount, whitePieceCount};
}

std::string solution(int n, std::vector<std::string> moves) {
    auto finalGameBoard = playGameMoves(n, moves);
    auto [blackPieces, whitePieces] = countGamePieces(finalGameBoard);
    return std::to_string(blackPieces) + " " + std::to_string(whitePieces);
}