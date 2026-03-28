from sly import Parser
from components.lexica import PropLogicLexer
from components.ast.prop_logic import PropExpression, PropTrue, PropFalse, PropAnd, PropOr

class PropLogicParser(Parser):
    tokens = PropLogicLexer.tokens

    # https://sly.readthedocs.io/en/latest/sly.html#dealing-with-ambiguous-grammars
    precedence = (
        ("left", OR), # left associative, lower precedence
        ("left", AND), # left associative, higher precedence
    )

    @_("expr")
    def statement(self, p) -> PropExpression:
        return p.expr

    @_("expr OR expr")
    def expr(self, p) -> PropExpression:
        return PropOr(p.expr0, p.expr1)

    @_("expr AND expr")
    def expr(self, p) -> PropExpression:
        return PropAnd(p.expr0, p.expr1)

    @_("TRUE")
    def expr(self, p) -> PropExpression:
        return PropTrue()

    @_("FALSE")
    def expr(self, p) -> PropExpression:
        return PropFalse()

    # https://sly.readthedocs.io/en/latest/sly.html#panic-mode-recovery
    def error(self, p):
        if p:
            print("Syntax error at token", p.type)
            # Just discard the token and tell the parser it's okay.
            self.errok()
        else:
            print("Syntax error at EOF")

# testing lexer + parser (that utilizes the PropExpression AST)
# here the parser respects the precedence as statically defined
if __name__ == "__main__":
    lexer  = PropLogicLexer()
    parser = PropLogicParser()

    result = parser.parse(lexer.tokenize("t ∨ f ∧ f"))
    print(result.run())    # True
    print(result.prefix()) # ∨ t ∧ f f