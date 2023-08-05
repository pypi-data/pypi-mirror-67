
from pe.operators import (
    Dot,
    Literal,
    Class,
    Sequence,
    Choice,
    Optional,
    Star,
    Plus,
    Nonterminal,
    And,
    Not,
    Capture,
    Bind,
)
from pe._parse import loads


def eloads(s):
    start, defmap = loads(s)
    return defmap[start]


def test_loads_dot():
    assert eloads('.') == Dot()
    assert eloads('.  # comment') == Dot()


def test_loads_literal():
    assert eloads('"foo"') == Literal('foo')
    assert eloads('"foo"  # comment') == Literal('foo')
    assert eloads('"\\t"') == Literal('\t')
    assert eloads('"\\n"') == Literal('\n')
    assert eloads('"\\v"') == Literal('\v')
    assert eloads('"\\f"') == Literal('\f')
    assert eloads('"\\r"') == Literal('\r')
    assert eloads('"\\""') == Literal('"')
    assert eloads("'\\''") == Literal("'")
    assert eloads("'\\-'") == Literal("-")
    assert eloads("'\\['") == Literal("[")
    assert eloads("'\\\\'") == Literal("\\")
    assert eloads("'\\]'") == Literal("]")
    # TODO: octal, utf8, utf16, utf32, escape errors


def test_loads_class():
    assert eloads('[xyz]') == Class('xyz')
    assert eloads('[xyz]  # comment') == Class('xyz')


def test_loads_nonterminal():
    assert eloads('foo') == Nonterminal('foo')
    assert eloads('foo  # comment') == Nonterminal('foo')


def test_loads_optional():
    assert eloads('"a"?') == Optional('a')
    assert eloads('"a"?  # comment') == Optional('a')


def test_loads_star():
    assert eloads('"a"*') == Star('a')
    assert eloads('"a"*  # comment') == Star('a')


def test_loads_plus():
    assert eloads('"a"+') == Plus('a')
    assert eloads('"a"+  # comment') == Plus('a')


def test_loads_sequence():
    assert eloads('"a" "b"') == Sequence('a', 'b')
    assert eloads('"a" "b"  # comment') == Sequence('a', 'b')


def test_loads_choice():
    assert eloads('"a" / "b"') == Choice('a', 'b')
    assert eloads('"a" / "b"  # comment') == Choice('a', 'b')


def test_loads_and():
    assert eloads('&"a"') == And('a')
    assert eloads('&"a"  # comment') == And('a')


def test_loads_not():
    assert eloads('!"a"') == Not('a')
    assert eloads('!"a"  # comment') == Not('a')


def test_loads_capture():
    assert eloads('~"a"') == Capture('a')
    assert eloads('~"a"  # comment') == Capture('a')


def test_loads_bind():
    assert eloads('x:"a"') == Bind('a', name='x')
    assert eloads('x:"a"  # comment') == Bind('a', name='x')
    assert eloads('x: "a"') == Bind('a', name='x')
    assert eloads('x : "a"') == Bind('a', name='x')


def test_loads_def():
    assert loads('A <- "a"') == ('A', {'A': Literal('a')})
    assert loads('A <- "a"  # comment') == ('A', {'A': Literal('a')})
    assert loads('A <- "a" "b"') == ('A', {'A': Sequence('a', 'b')})
    assert loads('A <- "a" B <- "b"') == ('A', {'A': Literal('a'),
                                                'B': Literal('b')})
    assert loads('''
        A   <- "a" Bee
        Bee <- "b"
    ''') == ('A', {'A': Sequence('a', Nonterminal('Bee')),
                   'Bee': Literal('b')})
