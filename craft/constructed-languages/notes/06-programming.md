# S6: Programming Languages as Conlangs

> Code is language design. The most successful constructed languages ever created are the ones that run on silicon.

**Sources:** 8 (P-01 through P-08)
**Adequacy:** Strong. Covers esoteric languages, APL, Brainfuck, natural language programming, Dijkstra's critique, and the conlang-programming parallel.

---

## 1. Code as Constructed Language

Programming languages are, by any reasonable definition, constructed languages. They are formal systems designed by individuals or committees to express meaning (computational instructions) in a structured notation. They have syntax (grammar), semantics (meaning), and pragmatics (how they are used in practice). They are learned, they form communities, and they evolve over time.

Yet the conlang and programming language communities rarely recognize each other. Conlangers create languages for humans to speak; language designers create languages for machines to execute. But the design challenges are remarkably similar:
- How do you balance expressiveness with learnability?
- How do you handle ambiguity?
- How do you build a community of users?
- What does the notation reveal about how its users think?

## 2. APL: Radical Notation (1962)

Kenneth Iverson's APL (A Programming Language) is the most conlang-like programming language ever created. Published in his 1962 book of the same name, APL uses a unique character set that looks nothing like conventional mathematics or programming.

APL's key properties:
- **Custom symbol set**: Uses Greek letters, mathematical operators, and invented symbols. Requires a special keyboard.
- **Array-oriented**: Operates on entire arrays at once, not individual elements
- **Right-to-left evaluation**: No operator precedence — everything evaluates right to left
- **Extreme conciseness**: A single line of APL can replace dozens of lines in other languages

Iverson received the Turing Award in 1979. His lecture was titled "Notation as a Tool of Thought" — a direct engagement with the Sapir-Whorf hypothesis applied to programming. His argument: the notation you use shapes how you think about problems. APL's array notation makes certain mathematical insights visible that procedural languages obscure.

APL influenced the esolang tradition through its willingness to depart completely from conventional syntax. If programming can look like APL, it can look like anything.

## 3. Brainfuck: Minimalism as Art (1993)

Urban Muller, a Swiss student, created Brainfuck in 1993 with a single goal: the smallest possible compiler. The entire language has eight commands:

`> < + - . , [ ]`

That's it. Move a pointer, increment or decrement a memory cell, read input, write output, and loop. It is Turing-complete — theoretically capable of computing anything any other language can compute. In practice, writing even simple programs is agonizing.

Brainfuck is the purest demonstration that a Turing-complete language can be almost impossibly minimal. It is a reductio ad absurdum of language design: how little do you need? The answer is: eight symbols and a tape.

But Brainfuck is more than a joke. It is used to teach computational theory (Turing machines, Church-Turing thesis), to challenge programmers, and as a starting point for compiler writing exercises. It is also, arguably, art — a constructed language that deliberately frustrates its users to make a point about the relationship between notation and thought.

## 4. The Esoteric Language Tradition

INTERCAL (1972) was the first esoteric programming language, created by Don Woods and James M. Lyon as a parody of FORTRAN, COBOL, and APL. Its design philosophy: be as confusing and frustrating as possible. It requires the programmer to say "PLEASE" occasionally (but not too often) or the program refuses to compile.

The esolang tradition that followed includes:
- **Befunge** (1993): Programs written on a 2D grid; execution can go in any direction
- **Shakespeare** (2001): Programs look like Shakespeare plays; characters are variables, dialogue is computation
- **Piet** (2001): Programs are bitmap images; colors encode operations
- **Whitespace** (2003): Only whitespace characters (space, tab, newline) are meaningful; all other characters are ignored
- **LOLCODE** (2007): Programs written in internet cat speak

Over 1,000 esolangs are documented. They form a community that parallels the conlang community in striking ways: hobbyist creators, shared design challenges, aesthetic standards, and an appreciation for the art of language design itself.

## 5. Dijkstra vs. Natural Language Programming

In 1978, Edsger Dijkstra wrote "On the foolishness of 'natural language programming'" (EWD 667). His argument: formal symbolism is essential to precise thought. Greek mathematics stalled because it was verbal and pictorial. Modern science and mathematics emerged only when thinkers like Vieta, Descartes, Leibniz, and Boole developed formal notations. Programming requires the same precision.

The parallel to conlangs: Dijkstra argues that the whole point of a programming language is to be *not* natural. Its formality is its value. Making it resemble natural language (as COBOL attempted) is a step backward, not forward.

Historical attempts at natural language programming:
- **COBOL** (1959): Designed to read like English ("ADD OVERTIME TO BASE-PAY GIVING TOTAL-PAY")
- **SQL** (1970s): English-like syntax for database queries
- **AppleScript** (1993): Tried to be readable as natural English
- **SHRDLU** (Winograd, 1971): Could understand natural English commands about a toy blocks world

All fell short of true natural language understanding. The gap between human ambiguity and computational precision seemed permanent.

Then came LLMs. In 2025-2026, people write code by describing what they want in English. Marc Brooker's response to Dijkstra: "Almost all programs are already specified in natural language. LLMs have made Dijkstra's 'foolishness' partially successful." But he concedes that formal languages remain necessary for precision, verification, and debugging.

## 6. The Parallel: Programming Communities Mirror Conlang Communities

The structural parallels are uncanny:

| Conlangs | Programming Languages |
|----------|---------------------|
| Esperanto (utility-focused, community-driven) | Python (utility-focused, community-driven) |
| Tolkien's Quenya (artistic, deeply elaborated) | Haskell (mathematically beautiful, intellectually deep) |
| Klingon (grew beyond original purpose) | JavaScript (grew beyond original purpose) |
| Volapuk (destroyed by founder control) | Languages that died from governance failures |
| Brainfuck (minimalist art) | Brainfuck (minimalist art) — *it's literally both* |
| Lojban (logical, tests cognition) | Prolog (logical, shapes thinking) |

Both communities:
- Argue endlessly about design philosophy
- Have holy wars (tabs vs. spaces, agglutination vs. isolation)
- Value elegance alongside functionality
- Create things that most people will never use but that push the boundaries of the form

## 7. Regex: The Worst Conlang Ever Created

Regular expressions deserve special mention as a constructed language that is:
- Universally used (every programmer encounters regex)
- Universally hated (famously unreadable)
- Syntactically dense to the point of being a write-only language
- Learned by memorization of arcane symbols
- Essential despite being terrible

Regex is arguably the most successful terrible conlang: billions of lines of code depend on it, but no one would design it this way from scratch. It evolved from theoretical computer science (regular languages in the Chomsky hierarchy) through Unix tools into a practical but horrible notation. It is the Volapuk of programming: it works, but everyone wishes it were better.

## 8. What Sources Agree On

- Programming languages are designed formal systems with syntax and semantics
- APL demonstrates that notation genuinely shapes thought
- Esolangs parallel the conlang tradition as creative/artistic language design
- The natural language programming debate has been transformed by LLMs
- Programming language communities mirror conlang communities structurally

## 9. Where Sources Disagree

- Whether programming languages are "really" languages in the linguistic sense
- Whether Dijkstra's argument against natural language programming has been refuted by LLMs
- Whether esolangs are art, humor, pedagogy, or all three
- Whether the conlang-programming parallel is deep or superficial
