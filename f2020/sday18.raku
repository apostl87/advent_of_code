#!/opt/homebrew/bin raku
use MONKEY-SEE-NO-EVAL;

sub infix:<•> (\a, \b) is tighter(&infix:<*>) { a + b }
put [+] lines(slurp '18.txt').map: { EVAL S:g/'+'/•/ }
