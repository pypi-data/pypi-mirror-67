import pandas as pd
import numpy as np

def simple(lex1, lex2): # only takes presence of words into account, not semantic orientation
    n0 = len(set(lex1.word) & set(lex2.word))
    return n0 / (len(lex1) + len(lex2) - n0)

def binary(lex1, lex2): # evaluates if orientation (pos/neg) of so matches
    common_words = list(set(lex1.word) & set(lex2.word))
    dict1 = lex1.set_index("word").so.to_dict()
    dict2 = lex2.set_index("word").so.to_dict()
    n0 = len(common_words)
    word_scores = np.zeros(n0)
    for i, w in enumerate(common_words):
        if dict1[w] == dict2[w]: # Catch cases where both are zero
            word_scores[i] = 1
        else:
            word_scores[i] = int(dict1[w] * dict2[w] > 0)
    los_score = np.sum(word_scores) / (len(lex1) + len(lex2) - n0)
    return los_score

def score(lex1, lex2): # lexicon overlap score
    common_words = list(set(lex1.word) & set(lex2.word))
    dict1 = lex1.set_index("word").so.to_dict()
    dict2 = lex2.set_index("word").so.to_dict()
    n0 = len(common_words)
    word_scores = np.zeros(n0)
    for i, w in enumerate(common_words):
        if dict1[w] == dict2[w]: # Catch cases where both are zero
            word_scores[i] = 1
        else:
            word_scores[i] = dict1[w] / dict2[w] if abs(dict1[w]) <= abs(dict2[w]) else dict2[w] / dict1[w]
    simple_score = n0 / (len(lex1) + len(lex2) - n0)
    los_score = np.sum(word_scores) / (len(lex1) + len(lex2) - n0)
    return los_score

if __name__ == '__main__':
    df1 = pd.DataFrame([("test",   1), ("free",    1), ("other", 1), ("check", 0.5)], columns=["word", "so"])
    df2 = pd.DataFrame([("test", 0.5), ("free",    1)],                               columns=["word", "so"])
    df3 = pd.DataFrame([("test", 0.5), ("free", -0.5)],                               columns=["word", "so"])
    df4 = pd.DataFrame([("test", -0.5), ("free", 0.5)],                               columns=["word", "so"])

    # Identical lexicons should have a score of 1, no matter the los type
    assert simple(df1, df1) == 1
    assert binary(df1, df1) == 1
    assert score(df1, df1) == 1

    # Different values of so will be punished by general los (version 3)
    assert simple(df1, df2) == 0.5
    assert binary(df1, df2) == 0.5
    assert score(df1, df2) == 0.375

    # Different orientation of so will be punished by binary_los
    assert simple(df2, df3) == 1
    assert binary(df2, df3) == 0.5
    assert score(df2, df3) == 0.25

    # Lexicon with same words but opposite so values should be -1 for the los (v3)
    assert score(df3, df4) == -1

    # los scores should be commutative
    assert simple(df1, df2) == simple(df2, df1)
    assert binary(df2, df3) == binary(df3, df2)
    assert score(df2, df3) == score(df3, df2)
    
    print("All assertions succesfull.")