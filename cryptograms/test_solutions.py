from .substitution import *

def test_chapter_one():
    input = "Max vhlm hy max unl wkboxk ingva B nlxw mh ingva fr hpg mktglyxkl"
    output = "the cost of the bus driver punch i used to punch my own transfers"
    assert caesar_shift(input, 7) == output 
    # The punch cost $15.
    
def test_chapter_two():
    input = "Estd mzzv esle elfrse xp szh ez ncplep yph topyetetpd hspy T hld l acp-eppy"
    output = "this book that taught me how to create new identities when i was a pre-teen"
    assert caesar_shift(input, 15) == output
    # The book was "The Paper Trip".

def test_chapter_three():
    input = "pbzfsobp dkfobtpkx lq pbkfi ppbkfpry aoxtolc iixz lq abpr bobt pbzfsba cl bmvq obail bpbeQ"
    output = "these older type of devices were used to call forward business lines to answering services"
    # Caesar shift and reverse can be applied in either order.
    assert caesar_shift(input, 3)[::-1] == output
    # The device is called a diverter.

def test_chapter_four():
    input = "gsvmznvlugsvnzrmuiznvhrszxpvwzgfhxrmgsvzikzmvgwzbh"
    output = "thenameofthemainframesihackedatuscinthearpanetdays"
    assert atbash(input) == output
    # The mainframe was called "Computer System for Mainframe Operations" (CMOS).
