# ChessGame

A Python chess game implementation featuring clean architecture with design patterns for maintainability and extensibility.

## Project Structure

```
chessGame/
├── src/
│   ├── core/           # Core domain objects (Position, Colour, Direction)
│   ├── board/          # Board management
│   ├── pieces/         # Chess piece implementations
│   │   ├── base/       # Abstract Piece class
│   │   ├── concrete/   # Concrete piece classes (Pawn, Knight, etc.)
│   │   └── strategies/ # Movement strategy implementations
│   └── moves/          # Move command pattern implementation
├── tests/              # Unit tests
└── game.py             # Entry point
```

## Architecture

### Design Patterns

**Strategy Pattern**: Movement logic is encapsulated in strategy classes, allowing pieces to delegate move calculation to interchangeable strategies.

```python
from src.pieces import Knight
from src.core import Position, Colour

knight = Knight(Position.from_algebraic("b1"), Colour.WHITE)
legal_moves = knight.get_legal_moves(board)
```

**Command Pattern**: Moves are represented as command objects with `execute()` and `undo()` methods, enabling move history and game state management.

```python
from src.moves import StandardMove, CaptureMove, MoveHistory

# Standard move (no capture)
move = StandardMove(piece, origin, destination)
move.execute(board)  # Apply the move
move.undo(board)     # Revert the move

# Capture move (removes enemy piece)
capture = CaptureMove(knight, origin, enemy_position)
capture.execute(board)  # Captures enemy and moves knight
capture.undo(board)     # Restores both pieces

# Move history with undo/redo
history = MoveHistory()
history.push(move)
move.execute(board)
history.undo(board)  # Undo last move
history.redo(board)  # Redo the move
```

## Modules

### Core (`src/core`)

Fundamental chess domain objects:

- **Position**: Represents a square on the board (file 0-7, rank 0-7) with algebraic notation support (e.g., "e4", "a1")
- **Colour**: Enum for piece colours (WHITE, BLACK) with helper methods
- **Direction**: Movement vector for calculating piece movements

### Board (`src/board`)

- **Board**: Manages piece placement, queries, and movement operations

### Pieces (`src/pieces`)

- **Piece**: Abstract base class for all chess pieces
- **Concrete Pieces**: Pawn, Knight, Bishop, Rook, Queen, King
- **Movement Strategies**: Encapsulated movement logic for each piece type
  - `SlidingStrategy`: Base for pieces that slide (Rook, Bishop, Queen)
  - `KnightStrategy`: L-shaped movement
  - `KingStrategy`: One-square movement in any direction
  - `PawnStrategy`: Forward movement with diagonal captures

### Moves (`src/moves`)

- **Move**: Abstract base class implementing the Command pattern
- **StandardMove**: Basic piece relocation from origin to destination
- **CaptureMove**: Move that captures an enemy piece, storing it for undo
- **MoveHistory**: Manages move history with undo/redo stack operations

## Usage

### Creating a Board with Pieces

```python
from src.board import Board
from src.pieces import Pawn, Knight, Rook
from src.core import Position, Colour

board = Board()

# Add pieces using algebraic notation
pawn = Pawn(Position.from_algebraic("e2"), Colour.WHITE)
knight = Knight(Position.from_algebraic("g1"), Colour.WHITE)

board.add_piece(pawn)
board.add_piece(knight)
```

### Getting Legal Moves

```python
# Get all legal moves for a piece
legal_moves = knight.get_legal_moves(board)

for move in legal_moves:
    print(move.to_algebraic())  # Prints: f3, h3
```

### Querying the Board

```python
# Check if a position is occupied
if board.is_occupied(Position.from_algebraic("e2")):
    piece = board.get_piece_at(Position.from_algebraic("e2"))

# Get all pieces of a colour
white_pieces = board.get_pieces(Colour.WHITE)
```

## Running Tests

```bash
pytest tests/
```

## Requirements

- Python 3.10+

## Roadmap

This project follows the architecture defined in the `shiny-splashing-dove` plan, implementing multiple design patterns for a comprehensive chess engine.

### Implemented

| Component | Patterns | Status |
|-----------|----------|--------|
| Core Domain | Value Objects | Position, Colour, Direction |
| Pieces | Strategy | All 6 pieces with movement strategies |
| Board | Mediator | Basic board with piece management |
| Moves | Command | StandardMove, CaptureMove, MoveHistory |

### To Be Implemented

#### Piece Enhancements
- **Decorators**: `PinnedPiece`, `PromotedPiece`, `CastlingRights` - modify piece behavior based on game state
- **Factory Pattern**: `PieceFactory`, `StandardPieceFactory` - create piece families for variants

#### Board Enhancements
- **Square**: Individual square class (Composite pattern)
- **BoardState**: Immutable snapshots (Memento pattern)
- **BoardBuilder**: Fluent board construction
- **AttackMap**: Cached attack/defense calculations
- **PositionCache**: Flyweight for position lookups

#### Additional Move Types
- **CastleMove**: Kingside/Queenside castling (Composite command)
- **EnPassantMove**: En passant capture
- **PromotionMove**: Pawn promotion
- **Move Notation**: Parser and formatter for algebraic notation

#### Validation Layer (Chain of Responsibility)
- `BoundsValidator` - Position in bounds
- `PieceOwnershipValidator` - Correct colour to move
- `DestinationValidator` - Not capturing own piece
- `PathValidator` - Path not blocked (sliding pieces)
- `CheckValidator` - Move doesn't leave king in check
- `PinValidator` - Pinned piece restrictions
- `CastlingValidator` - Castling conditions
- `EnPassantValidator` - En passant timing

#### Game State Machine (State Pattern)
- `SetupState` - Pre-game setup
- `PlayingState` - Normal play
- `CheckState` - King in check
- `CheckmateState` - Game over
- `StalemateState` - Draw by stalemate
- `DrawState` - Other draw conditions
- `GameClock` - Time controls

#### Event System (Observer Pattern)
- `EventBus` - Singleton event dispatcher
- Events: `MoveEvent`, `CaptureEvent`, `CheckEvent`, `PromotionEvent`, `CastleEvent`, `GameOverEvent`
- Listeners: `NotationListener`, `SoundListener`, `AnalyticsListener`

#### Analysis Layer (Visitor Pattern)
- `MaterialEvaluator` - Count material
- `PositionEvaluator` - Positional analysis
- `MobilityEvaluator` - Movement options
- `ThreatAnalyzer` - Detect threats
- `FenSerializer` - Export to FEN
- `PgnSerializer` - Export to PGN

#### AI/Engine Layer
- Search: Minimax, Alpha-Beta pruning, Iterative Deepening, MTD(f)
- Evaluation: Piece-square tables, Endgame tables
- Transposition: Zobrist hashing, Transposition table
- Opening: Opening book, Polyglot format support

#### Persistence Layer (Repository Pattern)
- Serializers: FEN, PGN, JSON formats
- Storage: File system, SQLite, Cloud adapters

#### UI Layer (Adapter Pattern)
- `CLIAdapter` - Terminal interface
- `GUIAdapter` - Tkinter/PyQt wrapper
- `WebAdapter` - WebSocket interface
- Board and ASCII renderers
