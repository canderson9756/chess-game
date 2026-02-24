# ChessGame

A Python chess game implementation featuring clean architecture with design patterns for maintainability and extensibility.

## Project Structure

```
chessGame/
├── src/
│   ├── core/           # Core domain objects (Position, Colour, Direction)
│   ├── board/          # Board management and builder
│   ├── pieces/         # Chess piece implementations
│   │   ├── base/       # Abstract Piece class
│   │   ├── concrete/   # Concrete piece classes (Pawn, Knight, etc.)
│   │   └── strategies/ # Movement strategy implementations
│   ├── moves/          # Move command pattern implementation
│   ├── validator/      # Move validation chain
│   ├── game/           # Game controller and state machine
│   │   └── state/      # Game states (Playing, Check, Checkmate, Stalemate)
│   ├── events/         # Event system (Observer pattern)
│   └── ui/             # UI adapter interface
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

**State Pattern**: Game states handle moves differently based on the current situation (normal play, check, checkmate, stalemate).

```python
from src.game import GameFactory

game = GameFactory.create_standard_game()
game.make_move(origin, destination)
print(game.get_status())  # "Playing", "Check", "Checkmate", or "Stalemate"
```

**Observer Pattern**: Event system notifies listeners of game events.

```python
from src.events import EventBus, MoveEvent, EventListener

class MoveLogger(EventListener):
    def on_event(self, event):
        print(f"Piece moved to {event.destination}")

bus = EventBus()
bus.subscribe(MoveEvent, MoveLogger())
```

**Chain of Responsibility**: Validators are chained to validate moves.

```python
from src.validator import CheckValidator

validator = CheckValidator()
is_valid = validator.validate(move, board)
```

**Builder Pattern**: Fluent board construction.

```python
from src.board import BoardBuilder

board = BoardBuilder().with_standard_position().build()
# Or custom setup
board = BoardBuilder().with_piece(king).with_piece(rook).build()
```

## Modules

### Core (`src/core`)

Fundamental chess domain objects:

- **Position**: Represents a square on the board (file 0-7, rank 0-7) with algebraic notation support (e.g., "e4", "a1")
- **Colour**: Enum for piece colours (WHITE, BLACK) with helper methods
- **Direction**: Movement vector for calculating piece movements

### Board (`src/board`)

- **Board**: Manages piece placement, queries, and movement operations
- **BoardBuilder**: Fluent builder for board construction with standard or custom positions

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

### Validator (`src/validator`)

- **Validator**: Abstract base for validation chain (Chain of Responsibility)
- **CheckValidator**: Ensures moves don't leave the king in check

### Game (`src/game`)

- **Game**: Main game controller handling moves, turns, validation, and events
- **GameFactory**: Factory for creating standard games, empty boards, or custom positions
- **Game States** (State Pattern):
  - `PlayingState`: Normal gameplay
  - `CheckState`: King is in check
  - `CheckmateState`: Game over - checkmate
  - `StalemateState`: Game over - stalemate

### Events (`src/events`)

- **EventBus**: Singleton event dispatcher (Observer pattern)
- **EventListener**: Abstract listener interface
- **Events**: `MoveEvent`, `CaptureEvent`, `CheckEvent`, `TurnEvent`, `GameOverEvent`

### UI (`src/ui`)

- **GameAdapter**: Abstract interface for UI implementations (Adapter pattern)

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

### Playing a Full Game

```python
from src.game import GameFactory
from src.core import Position

# Create a standard game
game = GameFactory.create_standard_game()

# Make moves
game.make_move(Position.from_algebraic("e2"), Position.from_algebraic("e4"))
game.make_move(Position.from_algebraic("e7"), Position.from_algebraic("e5"))

# Check game status
print(game.get_status())  # "Playing"
print(game.player_turn)   # Colour.WHITE

# Undo/redo
game.undo()
game.redo()

# Check for game over
if game.is_game_over():
    print(f"Game over: {game.get_status()}")
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
| Board | Mediator, Builder | Board, BoardBuilder with standard positions |
| Moves | Command | StandardMove, CaptureMove, MoveHistory |
| Validation | Chain of Responsibility | CheckValidator |
| Game | State, Factory | Game controller with state machine |
| Game States | State | PlayingState, CheckState, CheckmateState, StalemateState |
| Events | Observer, Singleton | EventBus with MoveEvent, CaptureEvent, CheckEvent, TurnEvent, GameOverEvent |
| UI | Adapter | GameAdapter interface |

### To Be Implemented

#### Piece Enhancements
- **Decorators**: `PinnedPiece`, `PromotedPiece`, `CastlingRights` - modify piece behavior based on game state
- **Factory Pattern**: `PieceFactory`, `StandardPieceFactory` - create piece families for variants

#### Board Enhancements
- **Square**: Individual square class (Composite pattern)
- **BoardState**: Immutable snapshots (Memento pattern)
- **AttackMap**: Cached attack/defense calculations
- **PositionCache**: Flyweight for position lookups

#### Additional Move Types
- **CastleMove**: Kingside/Queenside castling (Composite command)
- **EnPassantMove**: En passant capture
- **PromotionMove**: Pawn promotion
- **Move Notation**: Parser and formatter for algebraic notation

#### Additional Validators
- `BoundsValidator` - Position in bounds
- `PieceOwnershipValidator` - Correct colour to move
- `DestinationValidator` - Not capturing own piece
- `PathValidator` - Path not blocked (sliding pieces)
- `PinValidator` - Pinned piece restrictions
- `CastlingValidator` - Castling conditions
- `EnPassantValidator` - En passant timing

#### Additional Game States
- `SetupState` - Pre-game setup
- `DrawState` - Other draw conditions (50-move rule, threefold repetition, insufficient material)
- `GameClock` - Time controls

#### Event Listeners
- `NotationListener` - Records game in PGN
- `SoundListener` - Plays sounds
- `AnalyticsListener` - Tracks statistics

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

#### UI Implementations
- `CLIAdapter` - Terminal interface
- `GUIAdapter` - Tkinter/PyQt wrapper
- `WebAdapter` - WebSocket interface
- Board and ASCII renderers
